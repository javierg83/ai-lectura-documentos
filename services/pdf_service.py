# services/pdf_service.py
import os
import json
import uuid
from datetime import datetime
from utils.pdf_utils import extraer_paginas_pdf
from processor import process_pages
from utils.file_utils import guardar_resultados, normalizar_nombre
from embeddings import generar_embedding
from services.embedding_service import run_embedding_batch
import redis
import config

redis_client = redis.Redis.from_url(config.REDIS_URL)

def process_pdf(file_path, tipo_extraccion="ia", paginas=None, read_all=True, carpeta_destino=None):
    print("[pdf_service] → Archivo recibido:", os.path.basename(file_path))

    nombre_archivo = os.path.basename(file_path)  # incluye extensión
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
    carpeta = carpeta_destino or os.path.join("archivos_texto", nombre_sin_extension)
    os.makedirs(carpeta, exist_ok=True)

    destino = os.path.join(carpeta, nombre_archivo)
    os.rename(file_path, destino)

    print("[pdf_service] → PDF guardado en:", destino)
    print("[pdf_service] → Parámetros: read_all =", read_all, ", páginas específicas =", paginas)
    print("[pdf_service] → Tipo de extracción seleccionado:", tipo_extraccion)

    resultados = process_pages(destino, carpeta, paginas, read_all, nombre_sin_extension)

    try:
        print(f"[guardar_archivos] → Guardando JSON en {nombre_sin_extension}_resultado_paginas.json")
        guardar_resultados(resultados, carpeta, nombre_base=nombre_sin_extension)

        # Guardar también un JSON por cada página (requerido por run_embedding_batch)
        for pagina in resultados:
            num_pagina = pagina.get("pagina", "desconocida")
            archivo_pagina = os.path.join(carpeta, f"{nombre_sin_extension}_pag_{num_pagina}.json")
            with open(archivo_pagina, "w", encoding="utf-8") as f:
                json.dump(pagina, f, ensure_ascii=False, indent=2)
            print(f"[📄] Archivo de página guardado: {archivo_pagina}")

    except Exception as e:
        print(f"[❌ ERROR] Error durante guardado de resultados: {e}")

    print(f"[embedding] 🧠 Iniciando embedding para {len(resultados)} páginas")

    texto_documento = ""
    for pagina in resultados:
        num_pagina = pagina["pagina"]
        print(f"[embedding] → Procesando página {num_pagina}")
        contenido_pagina = ""
        key_base = f"doc_raw_page:{nombre_sin_extension}:p{num_pagina}"

        elementos = pagina.get("elementos", [])
        print(f"[embedding]   • Elementos detectados: {len(elementos)}")

        if not elementos:
            print(f"⚠️ Página {num_pagina} no contiene elementos, se omite")
            continue

        for idx, elem in enumerate(elementos):
            texto = str(elem.get("contenido", "")).strip()
            print(f"[embedding]     • Elem {idx+1}: '{texto[:50]}'... (len={len(texto)})")

            if not texto:
                continue

            try:
                emb = generar_embedding(texto)
                key_elem = f"{key_base}_e{idx+1}"
                redis_client.hset(key_elem, mapping={
                    "pagina": str(num_pagina),
                    "elemento": str(idx+1),
                    "texto": texto,
                    "embedding": json.dumps(emb)
                })
                contenido_pagina += texto + "\n"
            except Exception as e:
                print(f"[❌ error] Fallo embedding en p{num_pagina}_e{idx+1}: {e}")
                registrar_error_reproceso(nombre_sin_extension, num_pagina, idx+1)

        if contenido_pagina.strip():
            try:
                emb_pagina = generar_embedding(contenido_pagina)
                redis_client.hset(key_base, mapping={
                    "pagina": str(num_pagina),
                    "texto": contenido_pagina.strip(),
                    "embedding": json.dumps(emb_pagina)
                })
                texto_documento += contenido_pagina + "\n"
                print(f"[embedding] ✅ Página {num_pagina} embebida")
            except Exception as e:
                print(f"[❌ error] Fallo embedding página {num_pagina}: {e}")
                registrar_error_reproceso(nombre_sin_extension, num_pagina)

    if texto_documento.strip():
        try:
            emb_doc = generar_embedding(texto_documento)
            redis_client.hset(f"doc_raw:{nombre_sin_extension}", mapping={
                "nombre_original": nombre_archivo,
                "doc_id": nombre_sin_extension,
                "texto": texto_documento.strip(),
                "embedding": json.dumps(emb_doc),
                "pages_count": len(resultados),
                "filename": nombre_archivo,
                "timestamp": datetime.now().isoformat()
            })
            print("[embedding] ✅ Embedding de documento completo generado")
        except Exception as e:
            print(f"[❌ error] Fallo embedding documento completo: {e}")
            registrar_error_reproceso(nombre_sin_extension, -1)

    print("[embedding] ➕ Ejecutando refuerzo batch embedding con run_embedding_batch()")
    run_embedding_batch(nombre_sin_extension)

    return len(resultados)

def registrar_error_reproceso(doc_id, pagina, elemento=None):
    carpeta = os.path.join("archivos_texto", doc_id)
    os.makedirs(carpeta, exist_ok=True)

    archivo_log = os.path.join(carpeta, "log_errores.txt")
    with open(archivo_log, "a", encoding="utf-8") as f:
        if elemento:
            f.write(f"{doc_id}:p{pagina}_e{elemento}\n")
        elif pagina == -1:
            f.write(f"{doc_id}:DOCUMENTO\n")
        else:
            f.write(f"{doc_id}:p{pagina}\n")
