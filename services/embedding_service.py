# services/embedding_service.py
import os
import json
import redis
import traceback
from urllib.parse import urlparse
from tqdm import tqdm
from embeddings import generar_embedding
from config import REDIS_URL, MODEL_EMBEDDING
from utils.clean_text import limpiar_texto
from utils.file_utils import normalizar_nombre
from datetime import datetime

# 🔧 Configurar redis sin SSL para Redis Cloud gratuito
redis_url = urlparse(REDIS_URL)
r = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    db=0,
    ssl=False
)

def guardar_hash(clave, embedding, texto):
    try:
        r.hset(clave, mapping={
            "embedding": json.dumps(embedding),
            "texto": texto
        })
    except Exception as e:
        print(f"[❌ ERROR] No se pudo guardar en Redis ({clave}): {e}")

def run_embedding_batch(doc_id):
    ruta = os.path.join("archivos_texto", doc_id)
    if not os.path.exists(ruta):
        print(f"[❌ ERROR] Carpeta no encontrada: {ruta}")
        return

    archivos = [f for f in os.listdir(ruta) if f.endswith(".json") and "_pag_" in f]
    if not archivos:
        print(f"[⚠️] No se encontraron archivos JSON de páginas en {ruta}")
        return

    errores = []
    doc_id_normalizado = normalizar_nombre(doc_id)
    
    # Store parsed data to avoid reading files twice
    parsed_pages_data = []

    for archivo in tqdm(archivos, desc=f"[🔍] Procesando {len(archivos)} páginas"):
        try:
            path_archivo = os.path.join(ruta, archivo)
            print(f"[📄] Leyendo archivo: {path_archivo}")
            with open(path_archivo, encoding="utf-8") as f:
                data = json.load(f)

            pagina = data.get("pagina", -1)
            elementos = data.get("elementos", [])
            
            # Store parsed data for reuse when building complete document text
            parsed_pages_data.append({
                "archivo": archivo,
                "pagina": pagina,
                "elementos": elementos
            })

            print(f"[🔎] Página {pagina} → elementos encontrados: {len(elementos)}")

            if not elementos:
                errores.append((archivo, "❌ Sin elementos"))
                continue

            contenido_total = "\n\n".join([e.get("contenido", "") for e in elementos if e.get("contenido")])
            contenido_total = limpiar_texto(contenido_total)
            print(f"[📄] Contenido total página {pagina}: {len(contenido_total)} caracteres")

            if contenido_total:
                clave_pag = f"doc_raw_page:{doc_id_normalizado}:p{pagina}"
                embedding = generar_embedding(contenido_total, model=MODEL_EMBEDDING)
                guardar_hash(clave_pag, embedding, contenido_total)
                print(f"[✅] Embedding página {pagina} guardado en Redis → clave: {clave_pag}")
            else:
                print(f"⚠️ Página {pagina} sin contenido válido para embedding")

            for i, elem in enumerate(elementos):
                contenido = elem.get("contenido", "")
                if not contenido:
                    print(f"⚠️ Elemento {i+1} sin contenido, se omite")
                    continue
                contenido = limpiar_texto(contenido)
                if not contenido:
                    print(f"⚠️ Elemento {i+1} con contenido vacío luego de limpieza, se omite")
                    continue

                clave_elem = f"doc_raw_page:{doc_id_normalizado}:p{pagina}_e{i+1}"
                embedding = generar_embedding(contenido, model=MODEL_EMBEDDING)
                guardar_hash(clave_elem, embedding, contenido)
                print(f"[✅] Embedding elemento {i+1} guardado en Redis → clave: {clave_elem}")

        except Exception as e:
            errores.append((archivo, f"❌ Error: {e}"))
            traceback.print_exc()

    try:
        # Reuse parsed data instead of reading files again
        texto_partes = []
        for page_data in parsed_pages_data:
            elementos = page_data["elementos"]
            contenido_pagina = "\n\n".join([e.get("contenido", "") for e in elementos if e.get("contenido")])
            if contenido_pagina:
                texto_partes.append(contenido_pagina)
        
        texto_completo = limpiar_texto("\n".join(texto_partes).strip())
        if texto_completo:
            emb_doc = generar_embedding(texto_completo, model=MODEL_EMBEDDING)
            r.hset(f"doc_raw:{doc_id_normalizado}", mapping={
                "nombre_original": doc_id,
                "doc_id": doc_id_normalizado,
                "texto": texto_completo,
                "content": texto_completo,  # clave usada por chat_service
                "embedding": json.dumps(emb_doc),
                "pages_count": len(archivos),
                "filename": doc_id,
                "timestamp": datetime.now().isoformat()
            })
            print("[✅] Embedding completo del documento guardado en Redis")
    except Exception as e:
        print(f"[❌ ERROR] Fallo embedding documento completo: {e}")
        traceback.print_exc()

    if errores:
        log_path = os.path.join(ruta, "errores_embedding.log")
        with open(log_path, "w", encoding="utf-8") as f:
            for archivo, error in errores:
                f.write(f"{archivo}: {error}\n")
        print(f"[⚠️] Errores registrados en: {log_path}")
    else:
        print("✅ Embeddings generados correctamente para todas las páginas")

def list_raw_docs():
    claves = r.keys("doc_raw:*")
    nombres = [k.decode().replace("doc_raw:", "") for k in claves]
    return sorted(nombres)

def run_chat_embedding(user_id, mensaje, docs_normalizados, top_k=5):
    """
    Realiza búsqueda vectorial en Redis para encontrar las páginas más relevantes.
    
    Args:
        user_id: ID del usuario
        mensaje: Pregunta del usuario
        docs_normalizados: Lista de doc_ids seleccionados
        top_k: Número de mejores resultados a devolver (default: 5)
    
    Returns:
        dict con user_id, message, resultados (top-K ordenados por distancia)
    """
    import numpy as np

    vector_consulta = generar_embedding(mensaje, model=MODEL_EMBEDDING)
    if not vector_consulta:
        print("[chat_embedding] Error: No se pudo generar embedding para la consulta")
        return {
            "user_id": user_id,
            "message": mensaje,
            "resultados": []
        }
    
    print(f"[chat_embedding] Vector consulta generado (dim={len(vector_consulta)})")

    # Recolectar todos los resultados de todos los documentos
    todos_resultados = []

    for doc_id in docs_normalizados:
        # Buscar solo claves con sufijo _full (páginas completas)
        patron = f"doc_raw_page:{doc_id}:*_full"
        claves = list(r.scan_iter(match=patron))
        print(f"[chat_embedding] Buscando en Redis con patrón: {patron} -> {len(claves)} claves encontradas")

        for k in claves:
            k_str = k.decode() if isinstance(k, bytes) else k
            datos = r.hgetall(k)
            if not datos:
                continue

            try:
                emb = json.loads(datos.get(b"embedding", b"[]").decode())
                txt = datos.get(b"texto", b"").decode()
                pagina = datos.get(b"pagina", b"0").decode()
                tipo = datos.get(b"tipo", b"").decode()
                
                if not emb:
                    continue
                    
                dist = np.linalg.norm(np.array(vector_consulta) - np.array(emb))

                todos_resultados.append({
                    "documento": doc_id,
                    "clave": k_str,
                    "distancia": float(dist),
                    "contenido": txt,
                    "pagina": int(pagina) if pagina.isdigit() else 0,
                    "tipo": tipo
                })
            except Exception as e:
                print(f"[chat_embedding] Error procesando clave {k_str}: {e}")
                continue

    # Ordenar por distancia (menor es mejor) y tomar top-K
    todos_resultados.sort(key=lambda x: x["distancia"])
    mejores_resultados = todos_resultados[:top_k]
    
    print(f"[chat_embedding] Total resultados encontrados: {len(todos_resultados)}, devolviendo top-{top_k}")
    for i, res in enumerate(mejores_resultados):
        print(f"[chat_embedding]   #{i+1}: doc={res['documento']}, pag={res['pagina']}, dist={res['distancia']:.4f}")

    return {
        "user_id": user_id,
        "message": mensaje,
        "resultados": mejores_resultados
    }


def get_doc_pdf_filename(doc_id):
    """
    Obtiene el nombre del archivo PDF original desde Redis.
    
    Args:
        doc_id: ID del documento
    
    Returns:
        str: nombre del archivo PDF o None si no se encuentra
    """
    try:
        doc_data = r.hgetall(f"doc_raw:{doc_id}")
        if doc_data:
            filename = doc_data.get(b"filename", b"").decode()
            nombre_original = doc_data.get(b"nombre_original", b"").decode()
            # Preferir nombre_original si tiene extensión .pdf
            if nombre_original and nombre_original.lower().endswith(".pdf"):
                return nombre_original
            if filename:
                # Agregar .pdf si no lo tiene
                if not filename.lower().endswith(".pdf"):
                    return f"{filename}.pdf"
                return filename
        return None
    except Exception as e:
        print(f"[chat_embedding] Error obteniendo filename para {doc_id}: {e}")
        return None
