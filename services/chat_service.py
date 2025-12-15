# services/chat_service.py
import json
import redis
import faiss
import numpy as np
import config
from openai import OpenAI
from embeddings import generar_embedding  # ✅ Solo importar lo necesario

redis_client = redis.Redis.from_url(config.REDIS_URL)
oai = OpenAI(api_key=config.API_KEY)

FAISS_INDEX = 'faiss_index.bin'
MAX_CONTEXT_CHARS = 50000


def run_chat(user_id, message, doc_ids, embedding_mode, contenido_manual=None):
    """
    Orquesta el flujo de chat para:
    - contenido_manual: usar texto ya armado (por ejemplo desde chat_embedding).
    - embedding_mode=True: búsqueda vectorial en FAISS + chunks en Redis.
    - embedding_mode=False y doc_ids: usar contenido completo del campo 'texto' o 'content' de doc_raw:<doc_id>.
    - sin docs ni contenido_manual: responde solo con el modelo (sin contexto externo).
    """
    print(f"[chat_service] 🗣️ Usuario: {message}")
    system_content = ""

    # 1) Contenido manual (por ejemplo, chunks concatenados desde embedding_service)
    if contenido_manual:
        print("[chat_service] 📄 Usando contenido manual entregado por Redis.")
        system_content = contenido_manual

    # 2) Modo búsqueda vectorial (FAISS) - se mantiene para compatibilidad
    elif embedding_mode and doc_ids:
        print("[chat_service] 🔎 Modo: búsqueda vectorial (FAISS)")
        query_emb = generar_embedding(message)
        if not query_emb:
            print("[chat_service] ❌ No se pudo generar embedding para la consulta.")
            return "No se pudo generar la representación vectorial de la pregunta.", 0, 0

        try:
            idx = faiss.read_index(FAISS_INDEX)
        except Exception as e:
            print(f"[chat_service] ❌ Error al leer índice FAISS: {e}")
            return "No se pudo acceder al índice vectorial para buscar información.", 0, 0

        D, I = idx.search(np.array([np.array(query_emb, dtype='float32')]), 10)
        print(f"[chat_service] → Comparando contra {len(I[0])} chunks FAISS")

        seen = set()
        chunks_agregados = 0

        for doc_id in doc_ids:
            for i in I[0]:
                if i < 0:
                    continue
                if (doc_id, int(i)) in seen:
                    continue
                seen.add((doc_id, int(i)))

                txt = redis_client.hget(f"chunk:{doc_id}:{int(i)}", 'text')
                if txt:
                    decoded = txt.decode('utf-8', errors='ignore')
                    system_content += decoded + "\n\n"
                    chunks_agregados += 1
                    print(f"[chat_service] 🔹 Chunk {int(i)} incluido del doc {doc_id}:")
                    print(decoded[:200] + "...\n")
                if chunks_agregados >= 5:
                    break
            if chunks_agregados >= 5:
                break

        if chunks_agregados == 0:
            print("[chat_service] ⚠️ No se encontraron chunks relevantes en Redis.")

    # 3) Modo sin embeddings: usar contenido completo por documento
    elif doc_ids:
        print("[chat_service] 📟 Modo: contenido completo por documento")
        for doc_id in doc_ids:
            rec = redis_client.hgetall(f"doc_raw:{doc_id}")
            if not rec:
                print(f"[chat_service] ⚠️ No se encontró contenido en Redis para doc_raw:{doc_id}")
                continue

            # ✅ Preferir campo 'texto' (lo que tú usas), con fallback a 'content'
            raw_bytes = rec.get(b'texto') or rec.get(b'content') or b''
            content = raw_bytes.decode('utf-8', errors='ignore')
            print(f"[chat_service] → Texto cargado (len={len(content)})")

            if len(content) > MAX_CONTEXT_CHARS:
                print(f"[chat_service] ⚠️ Documento demasiado largo (len={len(content)}). Usando chunks como respaldo.")
                for i in range(10):
                    chunk = redis_client.hget(f"chunk:{doc_id}:{i}", 'text')
                    if chunk:
                        system_content += chunk.decode('utf-8', errors='ignore') + "\n\n"
            else:
                print(f"[chat_service] → Usando texto de doc_raw:{doc_id} (len={len(content)})")
                system_content += content + "\n\n"

    # 4) Sin contexto externo: solo conversación libre
    else:
        print("[chat_service] 💬 Modo sin documentos asociados (conversación general).")
        system_content = ""

    if not system_content.strip():
        print("[chat_service] ❌ No se pudo construir contexto para enviar al modelo.")
        return "No se obtuvo contexto relevante para responder la consulta.", 0, 0

    prompt_base = (
        "Responde siempre en español. "
        "Eres un asistente experto en análisis de documentos públicos, legales y técnicos. "
        "Tu tarea es ayudar al usuario a entender los documentos proporcionados, "
        "utilizando **solo** la información que estos contienen.\n\n"
        "### Instrucciones estrictas:\n"
        "- No puedes inventar datos que no estén explícitamente en el documento.\n"
        "- Usa solo el contenido que te proporcionamos como sistema (texto del/los documentos).\n"
        "- Si no encuentras información suficiente, responde claramente que no se encontró esa información.\n"
        "- Si el contenido proviene de una tabla, extrae su contenido y preséntalo en formato claro para el usuario.\n"
        "- Siempre que sea posible, cita o referencia el nombre del archivo o sección del documento que utilizas.\n"
        "- Si el usuario pide un resumen, entrégalo de forma ordenada y fácil de leer (títulos, viñetas, etc.).\n"
        "- Asegúrate de que cada respuesta sea útil, clara y avance en la conversación.\n"
        "- Copia y pega el parrafo en caso del que usuario te lo solicite.\n"
    )

    history = [{'role': 'system', 'content': prompt_base}]
    if system_content.strip():
        history.append({'role': 'system', 'content': system_content})
    history.append({'role': 'user', 'content': message})

    try:
        print("[chat_service] 🧠 Enviando solicitud al modelo GPT...")
        resp = oai.chat.completions.create(
            model="gpt-4o-mini",
            messages=history
        )

        reply = resp.choices[0].message.content
        token_in = resp.usage.prompt_tokens
        token_out = resp.usage.completion_tokens

        print(f"[chat_service] ✅ Respuesta generada con éxito")
        print(f"[chat_service] 📊 Tokens usados → input: {token_in}, output: {token_out}")
        print(f"[chat_service] 📝 Respuesta del modelo:")
        print(reply)

        redis_client.rpush(
            f"chat_history:{user_id}",
            json.dumps({'role': 'assistant', 'content': reply}, ensure_ascii=False)
        )
        print("[chat_service] 📤 Payload enviado al frontend: {'role': 'assistant', 'content': ...}")
        return reply, token_in, token_out

    except Exception as e:
        print(f"[chat_service] ❌ Error al llamar a OpenAI: {e}")
        return "Ocurrió un error al procesar la consulta con el modelo de lenguaje.", 0, 0
