# embedding_from_json.py
import os
import json
import re
from tqdm import tqdm
from redis import Redis
from embeddings import generar_embedding
from config import REDIS_URL, MODEL_EMBEDDING

# Conexión a Redis
redis_conn = Redis.from_url(REDIS_URL)

# Ruta base donde están los documentos procesados
BASE_DIR = "archivos_texto"

def normalizar_nombre(nombre):
    return re.sub(r'\W+', '_', nombre).strip('_')

def procesar_archivos():
    print("[🔍] Buscando archivos JSON...")
    archivos = []

    for carpeta, _, files in os.walk(BASE_DIR):
        for archivo in files:
            if archivo.endswith(".json") and "_resultado" not in archivo and "_tokens" not in archivo:
                archivos.append(os.path.join(carpeta, archivo))

    print(f"[🔍] Archivos detectados: {len(archivos)}")

    for ruta_json in tqdm(archivos):
        try:
            with open(ruta_json, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "elementos" not in data:
                print(f"[⚠️  SKIP] {ruta_json} no contiene elementos.")
                continue

            nombre_documento = os.path.basename(ruta_json).split("_pag_")[0]
            nombre_documento = os.path.relpath(nombre_documento, BASE_DIR)
            doc_id = normalizar_nombre(nombre_documento)

            for elemento in data["elementos"]:
                if not isinstance(elemento, dict):
                    continue

                # Solo procesamos texto o tabla
                if elemento.get("tipo") not in ["texto", "tabla"]:
                    continue

                contenido = ""
                if elemento["tipo"] == "texto":
                    contenido = elemento.get("contenido", "").strip()
                elif elemento["tipo"] == "tabla":
                    filas = elemento.get("contenido", [])
                    if isinstance(filas, list):
                        contenido = "\n".join([" | ".join(str(cell) for cell in fila) for fila in filas])

                if not contenido or not isinstance(contenido, str):
                    continue

                try:
                    embedding = generar_embedding(contenido, modelo=MODEL_EMBEDDING)
                except Exception as e:
                    print(f"[⚠️ ERROR] No se pudo generar embedding para {ruta_json}:{elemento.get('id')} → {e}")
                    continue

                clave_redis = f"doc_raw_page:{doc_id}:{elemento['id']}"
                redis_conn.hset(clave_redis, mapping={
                    "contenido": contenido,
                    "embedding": json.dumps(embedding)
                })

        except Exception as e:
            print(f"[⚠️ ERROR] No se pudo procesar {ruta_json}: {e}")

if __name__ == "__main__":
    procesar_archivos()
    print("[✅] Proceso finalizado.")
