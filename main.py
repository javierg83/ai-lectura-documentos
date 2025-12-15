# main.py
from pathlib import Path
import os
from processor import process_pages
from orquestador_documental import classify_document
from ai_esp_licitaciones import handle_licitaciones
from ai_esp_hipotecarios import handle_hipotecarios
from ai_esp_credito_consumo import handle_credito_consumo
from redis_uploader import upload_json_to_redis

#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/licitacion-imagenes-1pag.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/licitacion-imagenes.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/bono-foto-pdf.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/cheque-pdf.pdf"
PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/Promesa-CV-Javier.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/informe de titulos GALLARDO JIMENEZ.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/paginas_extraidas.pdf"
#PDF_PATH=r"C:/Desarrollo/IA/Proyectos/ai-lectura-documentos/archivos/paginas_extraidas-10.pdf"

READ_ALL=True
PAGES=[48,49]
UPLOAD_TO_REDIS=os.getenv('UPLOAD_TO_REDIS','true').lower() in ('1','true','yes')

if __name__=='__main__':
    res=process_pages(PDF_PATH,READ_ALL,PAGES)
    print(f"Procesadas {len(res)} páginas.")
    base=Path(PDF_PATH).stem
    JSON_PATH=f"{base}_resultado_paginas.json"
    REDIS_KEY=f"{base}:resultado"

    doc_type=classify_document(JSON_PATH)
    import unicodedata
    norm=unicodedata.normalize('NFD',doc_type).encode('ascii','ignore').decode('ascii').lower()
    if norm in ('licitacion','licitación'):
        handle_licitaciones(JSON_PATH)
    elif norm=='hipotecario':
        handle_hipotecarios(JSON_PATH)
    elif norm=='credito_consumo':
        handle_credito_consumo(JSON_PATH)
    else:
        print(f"Tipo no reconocido: {doc_type}")

    if UPLOAD_TO_REDIS:
        print(f"Subiendo {JSON_PATH} a Redis ({REDIS_KEY})...")
        try:
            upload_json_to_redis(JSON_PATH,REDIS_KEY)
            print("Subida completada.")
        except Exception as e:
            print(f"Error subida Redis: {e}")
    else:
        print("Subida Redis desactivada.")