from flask import Blueprint, request, jsonify, render_template
from utils.redis_utils import get_redis_client
from services.embedding_service import buscar_similares_por_embedding
from utils.token_utils import truncate_chunks_by_tokens

chat_embedding = Blueprint("chat_embedding", __name__)

@chat_embedding.route("/chat_embedding", methods=["GET"])
def chat_embedding_page():
    print("[chat_embedding] 💬 Renderizando chat_embedding.html")
    return render_template("chat_embedding.html")


@chat_embedding.route("/api/doc_raw", methods=["GET"])
def get_all_doc_raw():
    r = get_redis_client()
    keys = r.keys("doc_raw:*")

    docs = []

    for key in keys:
        raw = r.hgetall(key)
        if not raw:
            continue

        docs.append({
            # 🔑 claves CANÓNICAS (las que el frontend espera)
            "doc_id": raw.get("doc_id", ""),
            "nombre_original": raw.get("nombre_original", raw.get("filename", "")),
            "filename": raw.get("filename", raw.get("nombre_original", "")),
            "pages_count": raw.get("pages_count", "0"),
            "timestamp": raw.get("timestamp", ""),
        })

    print(f"[chat_embedding] 📄 Documentos encontrados: {len(docs)}")
    return jsonify(docs)


@chat_embedding.route("/api/chat_embedding", methods=["POST"])
def chat_embedding_api():
    data = request.get_json()

    pregunta = data.get("pregunta", "")
    doc_ids = data.get("documentos", [])

    print("[chat_embedding] ================= CHAT EMBEDDING =================")
    print(f"[chat_embedding] ❓ Pregunta: {pregunta}")
    print(f"[chat_embedding] 📄 Docs seleccionados: {doc_ids}")

    if not pregunta or not doc_ids:
        return jsonify({
            "respuesta": "Debe ingresar una pregunta y seleccionar al menos un documento."
        }), 400

    r = get_redis_client()
    all_chunks = []

    for doc_id in doc_ids:
        doc_key = f"doc_raw:{doc_id}"

        if not r.exists(doc_key):
            print(f"[chat_embedding] ⚠️ Documento no encontrado: {doc_key}")
            continue

        pages_count = int(r.hget(doc_key, "pages_count") or 0)
        print(f"[chat_embedding] 📘 Revisando {pages_count} páginas del documento {doc_id}")

        for page in range(1, pages_count + 1):
            page_key = f"doc_raw_page:{doc_id}:p{page}_full"

            if not r.exists(page_key):
                continue

            texto = r.hget(page_key, "texto")
            embedding = r.hget(page_key, "embedding")

            if texto and embedding:
                all_chunks.append(texto)

    if not all_chunks:
        print("[chat_embedding] 🚫 No se encontró ningún chunk útil con embedding.")
        return jsonify({
            "respuesta": "No se encontró contenido embebido para los documentos seleccionados."
        }), 200

    chunks, tokens_utilizados = truncate_chunks_by_tokens(
        all_chunks, max_tokens=6000
    )

    print(f"[chat_embedding] 🧠 Tokens usados: {tokens_utilizados}")
    print(f"[chat_embedding] 🧩 Textos enviados al agente: {len(chunks)}")

    respuesta = buscar_similares_por_embedding(pregunta, chunks)

    print("[chat_embedding] 🤖 Respuesta generada")
    print("================================================")

    return jsonify({
        "respuesta": respuesta
    })


# 🔑 export correcto del Blueprint
chat_embedding_bp = chat_embedding
