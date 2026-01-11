# services/pdf_service.py
import os
import json
import uuid
from datetime import datetime
from utils.pdf_utils import extraer_paginas_pdf
from .processor import process_pages
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

    resultados = process_pages(destino, carpeta, paginas, read_all, nombre_sin_extension) # process_pages ya normaliza internamente para SU uso, pero aquí necesitamos usar el ID normalizado para lo siguiente

    # Normalizar para el resto del servicio
    doc_id_normalized = normalizar_nombre(nombre_sin_extension)
    print(f"[pdf_service] → Usando ID normalizado: {doc_id_normalized}")

    try:
        print(f"[guardar_archivos] → Guardando JSON en {doc_id_normalized}_resultado_paginas.json")
        # Recargamos resultados desde processor si fuera necesario, pero aquí 'resultados'
        # es el return de process_pages. Ojo: process_pages guarda en Redis usando el ID normalizado.
        
        guardar_resultados(resultados, carpeta, nombre_base=doc_id_normalized)

        # Guardar JSON por página
        for pagina in resultados:
            num_pagina = pagina.get("pagina", "desconocida")
            archivo_pagina = os.path.join(carpeta, f"{doc_id_normalized}_pag_{num_pagina}.json")
            with open(archivo_pagina, "w", encoding="utf-8") as f:
                json.dump(pagina, f, ensure_ascii=False, indent=2)
            print(f"[📄] Archivo de página guardado: {archivo_pagina}")

    except Exception as e:
        print(f"[❌ ERROR] Error durante guardado de resultados: {e}")

    print(f"[embedding] 🧠 Iniciando cálculo de embedding global para {len(resultados)} páginas")

    # NOTA: process_pages YA guarda los embeddings de elementos y páginas en Redis.
    # Aquí solo agregamos el texto para el embedding DEL DOCUMENTO COMPLETO.
    
    texto_documento = ""
    for pagina in resultados:
        # Concatenamos texto de todos los elementos para el doc completo
        elementos = pagina.get("elementos", [])
        for elem in elementos:
            # Asegurar que es string
            contenido_raw = elem.get("contenido", "")
            if isinstance(contenido_raw, list):
                 # Si es tabla (lista de listas), lo aplanamos un poco para texto
                 texto = " ".join([str(item) for sublist in contenido_raw for item in (sublist if isinstance(sublist, list) else [sublist])])
            else:
                 texto = str(contenido_raw)

            if texto and texto.strip():
                texto_documento += texto.strip() + "\n"

    # Generar Embedding Nivel Documento
    if texto_documento.strip():
        try:
            emb_doc = generar_embedding(texto_documento)
            # Usar la clave normalizada
            redis_client.hset(f"doc_raw:{doc_id_normalized}", mapping={
                "nombre_original": nombre_archivo,
                "doc_id": doc_id_normalized,
                "texto": texto_documento.strip(),
                "embedding": json.dumps(emb_doc),
                "pages_count": len(resultados),
                "filename": nombre_archivo,
                "timestamp": datetime.now().isoformat()
            })
            print(f"[embedding] ✅ Embedding de documento completo generado para: {doc_id_normalized}")
        except Exception as e:
            print(f"[❌ error] Fallo embedding documento completo: {e}")
            registrar_error_reproceso(doc_id_normalized, -1)

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
