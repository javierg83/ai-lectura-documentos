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

# 🔥 NUEVO: registro de licitación
from services.licitacion_service import get_or_create_licitacion


# ==========================================================
# REDIS CLIENT
# ==========================================================
redis_url = urlparse(REDIS_URL)
r = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    db=0,
    ssl=False
)


# ==========================================================
# HELPERS
# ==========================================================
def _contenido_a_texto(valor):
    """
    Normaliza el contenido a string.
    Soporta:
    - str
    - list[str]
    - otros tipos -> ""
    """
    if isinstance(valor, list):
        return "\n".join(str(v) for v in valor if v)
    if isinstance(valor, str):
        return valor
    return ""


def guardar_hash(clave, embedding, texto):
    try:
        r.hset(clave, mapping={
            "embedding": json.dumps(embedding),
            "texto": texto
        })
    except Exception as e:
        print(f"[❌ ERROR] No se pudo guardar en Redis ({clave}): {e}")


# ==========================================================
# EMBEDDINGS DESDE JSON
# ==========================================================
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
    #doc_id_normalizado = normalizar_nombre(doc_id)
    doc_id_normalizado = doc_id

    

    # ==========================================================
    # 🔑 NUEVO PASO 0: REGISTRAR LICITACIÓN EN BD
    # ==========================================================
    try:
        print("[📌] Registrando / obteniendo licitación antes de extracción semántica…")
        licitacion_uuid = get_or_create_licitacion(doc_id)
        print(f"[✅] Licitación activa → UUID: {licitacion_uuid}")
    except Exception as e:
        print("[❌ ERROR] No se pudo registrar la licitación")
        traceback.print_exc()
        return

    # ==========================================================
    # EMBEDDINGS POR PÁGINA
    # ==========================================================
    for archivo in tqdm(archivos, desc=f"[🔍] Procesando {len(archivos)} páginas"):
        try:
            path_archivo = os.path.join(ruta, archivo)
            print(f"[📄] Leyendo archivo: {path_archivo}")
            with open(path_archivo, encoding="utf-8") as f:
                data = json.load(f)

            pagina = data.get("pagina", -1)
            elementos = data.get("elementos", [])

            print(f"[🔎] Página {pagina} → elementos encontrados: {len(elementos)}")

            if not elementos:
                errores.append((archivo, "❌ Sin elementos"))
                continue

            # 🔧 FIX: normalizar contenido (str | list)
            contenido_total = "\n\n".join(
                _contenido_a_texto(e.get("contenido"))
                for e in elementos
                if _contenido_a_texto(e.get("contenido"))
            )

            contenido_total = limpiar_texto(contenido_total)
            print(f"[📄] Contenido total página {pagina}: {len(contenido_total)} caracteres")

            if contenido_total:
                clave_pag = f"doc_raw_page:{doc_id_normalizado}:p{pagina}_full"
                embedding = generar_embedding(contenido_total, model=MODEL_EMBEDDING)
                guardar_hash(clave_pag, embedding, contenido_total)
                print(f"[✅] Embedding página {pagina} guardado en Redis → clave: {clave_pag}")
            else:
                print(f"⚠️ Página {pagina} sin contenido válido para embedding")

            # -----------------------------
            # ELEMENTOS INDIVIDUALES (NO USADOS POR EXTRACTOR)
            # -----------------------------
            for i, elem in enumerate(elementos):
                contenido = _contenido_a_texto(elem.get("contenido"))
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

    # ==========================================================
    # EMBEDDING DOCUMENTO COMPLETO
    # ==========================================================
    try:
        texto_completo = ""
        for archivo in archivos:
            path_archivo = os.path.join(ruta, archivo)
            with open(path_archivo, encoding="utf-8") as f:
                data = json.load(f)

            elementos = data.get("elementos", [])

            texto_completo += "\n\n".join(
                _contenido_a_texto(e.get("contenido"))
                for e in elementos
                if _contenido_a_texto(e.get("contenido"))
            ) + "\n"

        texto_completo = limpiar_texto(texto_completo.strip())
        if texto_completo:
            emb_doc = generar_embedding(texto_completo, model=MODEL_EMBEDDING)
            r.hset(
                f"doc_raw:{doc_id_normalizado}",
                mapping={
                    "nombre_original": doc_id,
                    "doc_id": doc_id_normalizado,
                    "texto": texto_completo,
                    "content": texto_completo,  # usado por chat_service
                    "embedding": json.dumps(emb_doc),
                    "pages_count": len(archivos),
                    "filename": doc_id,
                    "timestamp": datetime.now().isoformat(),
                },
            )
            print("[✅] Embedding completo del documento guardado en Redis")

    except Exception as e:
        print(f"[❌ ERROR] Fallo embedding documento completo: {e}")
        traceback.print_exc()

    # ==========================================================
    # 🔥 EXTRACCIÓN SEMÁNTICA (YA CON UUID REAL)
    # ==========================================================
    try:
        print("[🧠] Iniciando extracción semántica: ITEMS_LICITACION")

        from services.semantic_extraction.runner import run_semantic_extraction

        run_semantic_extraction(
            licitacion_id=licitacion_uuid,          # ✅ UUID REAL
            concepto="ITEMS_LICITACION",
            documento_ids=[doc_id_normalizado],
            top_k=30,
            min_score=0.15,
            prompt_version="prompt_items_licitacion_v1",
            extractor_version="semantic_extractor_v1",
        )

        print("[✅] Extracción semántica ITEMS_LICITACION ejecutada")

    except Exception:
        print("[❌ ERROR] Fallo en extracción semántica ITEMS_LICITACION")
        traceback.print_exc()

    # ==========================================================
    # LOG DE ERRORES
    # ==========================================================
    if errores:
        log_path = os.path.join(ruta, "errores_embedding.log")
        with open(log_path, "w", encoding="utf-8") as f:
            for archivo, error in errores:
                f.write(f"{archivo}: {error}\n")
        print(f"[⚠️] Errores registrados en: {log_path}")
    else:
        print("✅ Embeddings generados correctamente para todas las páginas")


# ==========================================================
# UTILIDADES EXISTENTES (SIN CAMBIOS)
# ==========================================================
def list_raw_docs():
    claves = r.keys("doc_raw:*")
    nombres = [k.decode().replace("doc_raw:", "") for k in claves]
    return sorted(nombres)


def run_chat_embedding(user_id, mensaje, docs_normalizados, top_k=5):
    """
    Realiza búsqueda vectorial en Redis para encontrar las páginas más relevantes.
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

    todos_resultados = []

    for doc_id in docs_normalizados:
        patron = f"doc_raw_page:{doc_id}:*"
        claves = list(r.scan_iter(match=patron))

        for k in claves:
            k_str = k.decode() if isinstance(k, bytes) else k
            datos = r.hgetall(k)
            if not datos:
                continue

            try:
                emb = json.loads(datos.get(b"embedding", b"[]").decode())
                txt = datos.get(b"texto", b"").decode()
                if not emb:
                    continue

                dist = np.linalg.norm(
                    json.loads(json.dumps(vector_consulta)) - json.loads(json.dumps(emb))
                )

                todos_resultados.append({
                    "documento": doc_id,
                    "clave": k_str,
                    "distancia": float(dist),
                    "contenido": txt
                })
            except Exception:
                continue

    todos_resultados.sort(key=lambda x: x["distancia"])
    return {
        "user_id": user_id,
        "message": mensaje,
        "resultados": todos_resultados[:top_k]
    }


def get_doc_pdf_filename(doc_id):
    """
    Obtiene el nombre del archivo PDF original desde Redis.
    """
    try:
        doc_data = r.hgetall(f"doc_raw:{doc_id}")
        if doc_data:
            nombre_original = doc_data.get(b"nombre_original", b"").decode()
            filename = doc_data.get(b"filename", b"").decode()
            if nombre_original.lower().endswith(".pdf"):
                return nombre_original
            if filename:
                return f"{filename}.pdf" if not filename.lower().endswith(".pdf") else filename
        return None
    except Exception as e:
        print(f"[chat_embedding] Error obteniendo filename para {doc_id}: {e}")
        return None
