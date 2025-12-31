# Project Plan — Resumen de Componentes

_Generado automáticamente el 2025-12-31 22:14 UTC_

- **Raíz analizada:** `C:\Desarrollo\IA\Proyectos\ai-lectura-documentos`
- **Archivos (texto y binarios):** 173
- **LOC (estimado):** 16310

## Lenguajes / Tipos (conteo)
- Python: 72
- JSON: 59
- Text: 13
- Other: 11
- HTML: 7
- SQL: 6
- CSS: 2
- Markdown: 2
- Config: 1

## Árbol del proyecto (resumido)
```
  └─ 📄 .env
  └─ 📄 .gitignore
  └─ 📄 a_extraccion_paginas_pdf.py
  └─ 📄 ai_esp_credito_consumo.py
  └─ 📄 ai_esp_hipotecarios.py
  └─ 📄 ai_esp_hipotecarios_estudio_titulo.py
  └─ 📄 ai_esp_licitaciones.py
  └─ 📄 ai_extractor_pdf.py
  └─ 📄 app.py
  └─ 📄 borrar_claves_redis.py
  └─ 📄 borrar_todo_redis.py
  └─ 📄 CI-Javier_resultado_paginas.json
  └─ 📄 config.py
  └─ 📄 create_index.py
  └─ 📄 debug_llm_raw_items_licitacion_20251231_214746.json
  └─ 📄 debug_llm_raw_items_licitacion_20251231_215056.json
  └─ 📄 documento_reconstruido copy.pdf
  └─ 📄 documento_reconstruido.docx
  └─ 📄 documento_reconstruido.pdf
  └─ 📄 docx_generator.py
  └─ 📄 eliminar_claves_incompletas.py
  └─ 📄 embedding_from_json.py
  └─ 📄 embeddings.py
  └─ 📄 extract_project_structure.py
  └─ 📄 extraer_paginas_pdf.py
  └─ 📄 faiss_index.bin
  └─ 📄 generar_excel.py
  └─ 📄 index_documents.py
  └─ 📄 main.py
  └─ 📄 ocr_utils.py
  └─ 📄 orquestador_documental.py
  └─ 📄 pdf_generator.py
  └─ 📄 pdf_selectable.py
  └─ 📄 pdf_utils.py
  └─ 📄 processor.py
  └─ 📄 project_plan.json
  └─ 📄 PROJECT_PLAN.md
  └─ 📄 prueba_convolucion_img.py
  └─ 📄 pyvenv.cfg
  └─ 📄 README.md
  └─ 📄 redis_uploader.py
  └─ 📄 redis_vector_demo.py
  └─ 📄 requirements.txt
  └─ 📄 salida_items_BASES_ADMINISTRATIVAS_ESPECIALES__15.json
  └─ 📄 salida_items_normalizados.json
  └─ 📄 validar_embedding_redis.py
  └─ 📄 validar_embeddings_generico.py
📁 /
📁 Imagenes Ejemplo Convolucion/
    └─ 📄 pag2.jpg
    └─ 📄 salida_convolucion.png
    └─ 📄 salida_gris.png
📁 Include/
📁 db/
📁 debug_homologacion/
    └─ 📄 resp_homologacion_6e5a09ad-0b71-4cc0-adb7-a8494a267523.json
📁 manual/
📁 productos/
    └─ 📄 productos.xlsx
📁 prompts/
📁 routes/
    └─ 📄 __init__.py
    └─ 📄 chat.py
    └─ 📄 chat_embedding.py
    └─ 📄 extraction.py
📁 salida_json/
  📁 1_bases_5300_44_l125__10/
      └─ 📄 datos_basicos_licitacion_20251229_142011.json
      └─ 📄 finanzas_licitacion_20251229_143051.json
      └─ 📄 items_licitacion_20251229_142547.json
  📁 1_bases_5300_44_l125__11/
      └─ 📄 datos_basicos_licitacion_20251229_152706.json
      └─ 📄 finanzas_licitacion_20251229_153733.json
  📁 1_bases_5300_44_l125__12/
      └─ 📄 datos_basicos_licitacion_20251229_155900.json
      └─ 📄 finanzas_licitacion_20251229_161000.json
  📁 1_bases_5300_44_l125__13/
      └─ 📄 datos_basicos_licitacion_20251229_190253.json
      └─ 📄 finanzas_licitacion_20251229_191427.json
      └─ 📄 items_licitacion_20251229_190901.json
      └─ 📄 items_licitacion_20251229_193027.json
  📁 1_bases_5300_44_l125__14/
      └─ 📄 datos_basicos_licitacion_20251229_201507.json
      └─ 📄 finanzas_licitacion_20251229_202622.json
      └─ 📄 items_licitacion_20251229_202104.json
      └─ 📄 items_licitacion_20251229_211835.json
  📁 1_bases_5300_44_l125__15/
      └─ 📄 datos_basicos_licitacion_20251229_214853.json
      └─ 📄 finanzas_licitacion_20251229_220035.json
      └─ 📄 items_licitacion_20251229_215502.json
  📁 1_bases_5300_44_l125__16/
  📁 1_bases_5300_44_l125__17/
      └─ 📄 datos_basicos_licitacion_20251230_011604.json
      └─ 📄 finanzas_licitacion_20251230_012930.json
      └─ 📄 items_licitacion_20251230_012310.json
  📁 1_bases_5300_44_l125__18/
      └─ 📄 datos_basicos_licitacion_20251230_030605.json
      └─ 📄 finanzas_licitacion_20251230_032222.json
      └─ 📄 items_licitacion_20251230_031430.json
  📁 1_bases_5300_44_l125__19/
      └─ 📄 datos_basicos_licitacion_20251230_125736.json
      └─ 📄 finanzas_licitacion_20251230_131201.json
      └─ 📄 items_licitacion_20251230_130516.json
  📁 1_bases_5300_44_l125__20/
      └─ 📄 datos_basicos_licitacion_20251230_143646.json
      └─ 📄 finanzas_licitacion_20251230_145154.json
      └─ 📄 items_licitacion_20251230_144450.json
  📁 1_bases_5300_44_l125__21/
      └─ 📄 datos_basicos_licitacion_20251230_165036.json
      └─ 📄 finanzas_licitacion_20251230_170557.json
      └─ 📄 items_licitacion_20251230_165843.json
  📁 1_bases_5300_44_l125__5/
      └─ 📄 finanzas_licitacion_20251228_223453.json
  📁 1_bases_5300_44_l125__6/
      └─ 📄 finanzas_licitacion_20251229_000545.json
      └─ 📄 items_licitacion_20251229_000102.json
  📁 1_bases_5300_44_l125__7/
      └─ 📄 finanzas_licitacion_20251229_014742.json
      └─ 📄 items_licitacion_20251229_014309.json
  📁 1_bases_5300_44_l125__8/
      └─ 📄 finanzas_licitacion_20251229_021500.json
      └─ 📄 items_licitacion_20251229_021009.json
  📁 6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/
      └─ 📄 homologacion_productos-4o-mini.json
      └─ 📄 homologacion_productos.json
      └─ 📄 prompt_generado-4o-mini.txt
      └─ 📄 prompt_generado.txt
      └─ 📄 resp_llm_homologacion.json
  📁 6e5a09ad-0b71-4cc0-adb7-a8494a267523-old2/
      └─ 📄 homologacion_productos.json
      └─ 📄 prompt_generado.txt
      └─ 📄 resp_llm_homologacion.json
  📁 6e5a09ad-0b71-4cc0-adb7-a8494a267523/
      └─ 📄 homologacion_productos.json
      └─ 📄 prompt_generado.txt
      └─ 📄 resp_llm_homologacion.json
  📁 bases_administrativas_especiales__26/
      └─ 📄 finanzas_licitacion_20251228_213756.json
      └─ 📄 items_licitacion_20251228_213418.json
  📁 bases_administrativas_especiales__27/
      └─ 📄 datos_basicos_licitacion_20251230_182258.json
📁 services/
  📁 homologacion/
    📁 models/
        └─ 📄 __init__.py
        └─ 📄 schema.py
    📁 prompts/
        └─ 📄 prompt_homologacion_v1.txt
        └─ 📄 prompt_homologacion_v2.txt
        └─ 📄 prompt_homologacion_v3.txt
      └─ 📄 __init__.py
      └─ 📄 homologacion_db.py
      └─ 📄 homologacion_model.py
      └─ 📄 homologador.py
      └─ 📄 models.py
      └─ 📄 product_loader.py
  📁 semantic_extraction/
    📁 extractors/
      📁 datos_basicos_licitacion/
          └─ 📄 datos_basicos_extractor.py
          └─ 📄 normalizer.py
          └─ 📄 schema.py
      📁 finanzas_licitacion/
          └─ 📄 finanzas_licitacion_extractor.py
          └─ 📄 normalizer.py
          └─ 📄 schema.py
      📁 items_licitacion/
        📁 tests/
          └─ 📄 items_licitacion_extractor.py
          └─ 📄 normalizer.py
          └─ 📄 schema.py
        └─ 📄 base_extractor.py
    📁 prompts/
      📁 datos_basicos_licitacion/
          └─ 📄 prompt_datos_basicos_licitacion_v1.txt
      📁 finanzas_licitacion/
          └─ 📄 prompt_finanzas_licitacion_v1.txt
      📁 items_licitacion/
          └─ 📄 prompt_items_licitacion_v1.txt
          └─ 📄 prompt_items_licitacion_v2.txt
          └─ 📄 prompt_items_licitacion_v3.txt
    📁 utils/
        └─ 📄 semantic_utils.py
      └─ 📄 __init__.py
      └─ 📄 debug_llm_raw_items_licitacion_20251226_234850.json
      └─ 📄 debug_semantic_ITEMS_LICITACION_20251226_234850.json
      └─ 📄 registry.py
      └─ 📄 runner.py
    └─ 📄 __init__.py
    └─ 📄 chat_service.py
    └─ 📄 embedding_service.py
    └─ 📄 licitacion_service.py
    └─ 📄 llm_service.py
    └─ 📄 pdf_service.py
📁 share/
  📁 man/
    📁 man1/
        └─ 📄 ttx.1
📁 sql/
    └─ 📄 1-finanzas_licitacion.sql
    └─ 📄 2-item_licitacion_especificaciones.sql
    └─ 📄 3-licitacion_add_campos.sql
    └─ 📄 4-finanzas_licitacion_add_campos.sql
    └─ 📄 5-homologacion_productos.sql
    └─ 📄 create-inicial.sql
📁 static/
  📁 css/
      └─ 📄 style.css
      └─ 📄 theme-glass.css
📁 templates/
    └─ 📄 chat.html
    └─ 📄 chat_embedding.html
    └─ 📄 detalle_licitacion.html
    └─ 📄 extraccion.html
    └─ 📄 home.html
    └─ 📄 licitaciones.html
    └─ 📄 listado.html
📁 tests/
  📁 manual/
      └─ 📄 base_extractor_simplificado.py
      └─ 📄 items_extractor_manual.py
      └─ 📄 runner_homologacion_manual.py
      └─ 📄 test_extract_items_manual.py
      └─ 📄 test_runner_semantic_only.py
📁 utils/
    └─ 📄 clean_text.py
    └─ 📄 file_utils.py
    └─ 📄 pdf_utils.py
    └─ 📄 redis_utils.py
```

## Dependencias & Infra (resumen)
**requirements.txt (top)**
```
a n n o t a t e d - t y p e s = = 0 . 7 . 0 
 
 a n y i o = = 4 . 9 . 0 
 
 b l i n k e r = = 1 . 9 . 0 
 
 c e r t i f i = = 2 0 2 5 . 1 . 3 1 
 
 c f f i = = 1 . 1 7 . 1 
 
 c h a r s e t - n o r m a l i z e r = = 3 . 4 . 1 
 
 c l i c k = = 8 . 1 . 8 
 
 c o l o r a m a = = 0 . 4 . 6 
 
 c r y p t o g r a p h y = = 4 4 . 0 . 2 
 
 d e f u s e d x m l = = 0 . 7 . 1 
 
...
```

## Componentes y propósito (por archivo)
### `.env`
- Tech: Flask (API web), Redis (cache/colas) | tamaño: 1311 bytes

### `.gitignore`
- Archivo | tamaño: 1125 bytes

### `ai_esp_credito_consumo.py`
- Python | tamaño: 702 bytes | LOC aprox: 23
- Funciones: handle_credito_consumo

### `ai_esp_hipotecarios.py`
- Python | tamaño: 4698 bytes | LOC aprox: 111
- Funciones: handle_hipotecarios

### `ai_esp_hipotecarios_estudio_titulo.py`
- Python | tamaño: 5038 bytes | LOC aprox: 168
- Funciones: handle_hipotecarios

### `ai_esp_licitaciones.py`
- Python | tamaño: 1607 bytes | LOC aprox: 47
- Funciones: handle_licitaciones

### `ai_extractor_pdf.py`
- Python | tamaño: 6029 bytes | LOC aprox: 131
- Funciones: count_tokens, analyze_page_with_gpt

### `app.py`
- Python — Punto de entrada de la app/servidor — Tech: Flask (API web) | tamaño: 2776 bytes | LOC aprox: 72
- Funciones: home, serve_archivos_texto, licitaciones, api_licitaciones, detalle_licitacion

### `a_extraccion_paginas_pdf.py`
- Python | tamaño: 1308 bytes | LOC aprox: 40
- Funciones: seleccion_paginas_extraccion

### `borrar_claves_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 1460 bytes | LOC aprox: 48
- Funciones: borrar_doc_raw_y_paginas

### `borrar_todo_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 877 bytes | LOC aprox: 29
- Funciones: borrar_todo_redis

### `CI-Javier_resultado_paginas.json`
- JSON | tamaño: 158 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
[
```

### `config.py`
- Python — Configuración — Tech: Redis (cache/colas) | tamaño: 1052 bytes | LOC aprox: 31

### `create_index.py`
- Python — Tech: Redis (cache/colas) | tamaño: 963 bytes | LOC aprox: 31

### `debug_llm_raw_items_licitacion_20251231_214746.json`
- JSON | tamaño: 2375 bytes | LOC aprox: 3
**Encabezado/comentario (snippet):**
```
{
```

### `debug_llm_raw_items_licitacion_20251231_215056.json`
- JSON | tamaño: 2375 bytes | LOC aprox: 3
**Encabezado/comentario (snippet):**
```
{
```

### `documento_reconstruido copy.pdf`
- Archivo | tamaño: 4909 bytes

### `documento_reconstruido.docx`
- Archivo | tamaño: 36633 bytes

### `documento_reconstruido.pdf`
- Archivo | tamaño: 4909 bytes

### `docx_generator.py`
- Python | tamaño: 1876 bytes | LOC aprox: 46
- Funciones: build_docx_from_json

### `eliminar_claves_incompletas.py`
- Python — Tech: Redis (cache/colas) | tamaño: 752 bytes | LOC aprox: 26

### `embeddings.py`
- Python | tamaño: 1438 bytes | LOC aprox: 49
- Funciones: generar_embedding, get_embeddings

### `embedding_from_json.py`
- Python — Tech: Redis (cache/colas) | tamaño: 2908 bytes | LOC aprox: 79
- Funciones: normalizar_nombre, procesar_archivos

### `extract_project_structure.py`
- Python — Modelo/ORM SQLAlchemy; Modelo/Validación Pydantic; Render de templates Jinja2 — Tech: Alembic (migraciones), Celery (jobs/worker), Django (framework web), FastAPI (API web), Flask (API web), Gunicorn (WSGI/ASGI server), HTMX (interacción HTML), HTTPX (cliente HTTP), Jinja2 (templates), Pydantic (modelos/validación), Pytest (tests), Redis (cache/colas), Requests (cliente HTTP), SQLAlchemy (ORM), Unittest (tests), Uvicorn (ASGI server) | tamaño: 21195 bytes | LOC aprox: 547
**Docstring módulo (resumen):**
> extract_project_structure.py
> Genera un "plan de proyecto" para que una IA entienda la estructura y propósito de cada componente
> sin leer archivos completos. Pensado para ejecutarse desde la raíz del proyecto (cwd por defecto).
> 
> Salidas:
> - Markdown: PROJECT_PLAN.md (árbol + resúmenes)
> - JSON:     project_plan.json (estructura detallada para IA)
> 
> Uso:
>     # desde la raíz del repo
>     python extract_...
- Funciones: norm_ext, is_probably_text, sha1_of_string, safe_read_head, count_loc, extract_python_docstring_and_symbols, first_comment_lines

### `extraer_paginas_pdf.py`
- Python | tamaño: 1485 bytes | LOC aprox: 39

### `faiss_index.bin`
- Archivo | tamaño: 3131458 bytes

### `generar_excel.py`
- Python | tamaño: 4116 bytes | LOC aprox: 68

### `index_documents.py`
- Python — Tech: Redis (cache/colas) | tamaño: 1163 bytes | LOC aprox: 31

### `main.py`
- Python — Punto de entrada de la app/servidor — Tech: Redis (cache/colas) | tamaño: 2272 bytes | LOC aprox: 51

### `ocr_utils.py`
- Python — Utilidades | tamaño: 225 bytes | LOC aprox: 8
- Funciones: image_to_text

### `orquestador_documental.py`
- Python | tamaño: 1013 bytes | LOC aprox: 28
- Funciones: classify_document

### `pdf_generator.py`
- Python | tamaño: 938 bytes | LOC aprox: 27
- Funciones: build_pdf_from_json

### `pdf_selectable.py`
- Python | tamaño: 1660 bytes | LOC aprox: 44
- Funciones: analyze_page_selectable

### `pdf_utils.py`
- Python — Utilidades | tamaño: 483 bytes | LOC aprox: 15
- Funciones: get_page_count, extract_page_image

### `processor.py`
- Python — Tech: Redis (cache/colas) | tamaño: 5348 bytes | LOC aprox: 118
- Funciones: convertir_pagina_a_base64, process_pages, guardar_resultados

### `project_plan.json`
- JSON | tamaño: 106208 bytes | LOC aprox: 3388
**Encabezado/comentario (snippet):**
```
{
```

### `PROJECT_PLAN.md`
- Markdown — Tech: Redis (cache/colas) | tamaño: 38287 bytes | LOC aprox: 1182
**Encabezado/comentario (snippet):**
```
# Project Plan — Resumen de Componentes
## Lenguajes / Tipos (conteo)
## Árbol del proyecto (resumido)
```

### `prueba_convolucion_img.py`
- Python | tamaño: 2528 bytes | LOC aprox: 75
- Funciones: rgb_to_gray_manual, convolve2d_gray

### `pyvenv.cfg`
- Config | tamaño: 399 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
home = C:\Users\javie\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0
```

### `README.md`
- Markdown — Documentación | tamaño: 69 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
# ai-lectura-documentos
```

### `redis_uploader.py`
- Python — Tech: Redis (cache/colas) | tamaño: 947 bytes | LOC aprox: 28
- Funciones: upload_json_to_redis

### `redis_vector_demo.py`
- Python — Tech: Redis (cache/colas) | tamaño: 220 bytes | LOC aprox: 8

### `requirements.txt`
- Text — Dependencias | tamaño: 2196 bytes | LOC aprox: 123
**Encabezado/comentario (snippet):**
```
a n n o t a t e d - t y p e s = = 0 . 7 . 0 
```

### `salida_items_BASES_ADMINISTRATIVAS_ESPECIALES__15.json`
- JSON | tamaño: 15080 bytes | LOC aprox: 344
**Encabezado/comentario (snippet):**
```
{
```

### `salida_items_normalizados.json`
- JSON | tamaño: 1329 bytes | LOC aprox: 42
**Encabezado/comentario (snippet):**
```
{
```

### `validar_embeddings_generico.py`
- Python — Tech: Redis (cache/colas) | tamaño: 1261 bytes | LOC aprox: 45

### `validar_embedding_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 2577 bytes | LOC aprox: 79
- Funciones: validar_claves

### `debug_homologacion/resp_homologacion_6e5a09ad-0b71-4cc0-adb7-a8494a267523.json`
- JSON | tamaño: 1491 bytes | LOC aprox: 41
**Encabezado/comentario (snippet):**
```
[
```

### `Imagenes Ejemplo Convolucion/pag2.jpg`
- Archivo | tamaño: 246409 bytes

### `Imagenes Ejemplo Convolucion/salida_convolucion.png`
- Archivo | tamaño: 367068 bytes

### `Imagenes Ejemplo Convolucion/salida_gris.png`
- Archivo | tamaño: 381364 bytes

### `productos/productos.xlsx`
- Archivo | tamaño: 10391 bytes

### `routes/chat.py`
- Python — Tech: Flask (API web), Redis (cache/colas) | tamaño: 3669 bytes | LOC aprox: 102
- Funciones: chat_page, api_docs, api_chat

### `routes/chat_embedding.py`
- Python — Tech: Flask (API web), Redis (cache/colas) | tamaño: 3709 bytes | LOC aprox: 95
- Funciones: obtener_docs_detalle, page, api_doc_raw, api_chat_embedding

### `routes/extraction.py`
- Python — Tech: Flask (API web) | tamaño: 2643 bytes | LOC aprox: 68
- Funciones: mostrar_formulario_extraccion, extraer_documento

### `routes/__init__.py`
- Python | tamaño: 0 bytes

### `salida_json/1_bases_5300_44_l125__10/datos_basicos_licitacion_20251229_142011.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__10/finanzas_licitacion_20251229_143051.json`
- JSON | tamaño: 358 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__10/items_licitacion_20251229_142547.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2057 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__11/datos_basicos_licitacion_20251229_152706.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__11/finanzas_licitacion_20251229_153733.json`
- JSON | tamaño: 253 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__12/datos_basicos_licitacion_20251229_155900.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__12/finanzas_licitacion_20251229_161000.json`
- JSON | tamaño: 253 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__13/datos_basicos_licitacion_20251229_190253.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__13/finanzas_licitacion_20251229_191427.json`
- JSON | tamaño: 253 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__13/items_licitacion_20251229_190901.json`
- JSON | tamaño: 183 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__13/items_licitacion_20251229_193027.json`
- JSON | tamaño: 183 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__14/datos_basicos_licitacion_20251229_201507.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__14/finanzas_licitacion_20251229_202622.json`
- JSON | tamaño: 253 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__14/items_licitacion_20251229_202104.json`
- JSON | tamaño: 356 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__14/items_licitacion_20251229_211835.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2207 bytes | LOC aprox: 71
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__15/datos_basicos_licitacion_20251229_214853.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__15/finanzas_licitacion_20251229_220035.json`
- JSON | tamaño: 893 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__15/items_licitacion_20251229_215502.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2200 bytes | LOC aprox: 71
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__17/datos_basicos_licitacion_20251230_011604.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__17/finanzas_licitacion_20251230_012930.json`
- JSON | tamaño: 911 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__17/items_licitacion_20251230_012310.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2634 bytes | LOC aprox: 84
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__18/datos_basicos_licitacion_20251230_030605.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__18/finanzas_licitacion_20251230_032222.json`
- JSON | tamaño: 700 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__18/items_licitacion_20251230_031430.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2638 bytes | LOC aprox: 83
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__19/datos_basicos_licitacion_20251230_125736.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__19/finanzas_licitacion_20251230_131201.json`
- JSON | tamaño: 893 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__19/items_licitacion_20251230_130516.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2260 bytes | LOC aprox: 71
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__20/datos_basicos_licitacion_20251230_143646.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__20/finanzas_licitacion_20251230_145154.json`
- JSON | tamaño: 893 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__20/items_licitacion_20251230_144450.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2256 bytes | LOC aprox: 71
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__21/datos_basicos_licitacion_20251230_165036.json`
- JSON | tamaño: 478 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__21/finanzas_licitacion_20251230_170557.json`
- JSON | tamaño: 893 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__21/items_licitacion_20251230_165843.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2268 bytes | LOC aprox: 71
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__5/finanzas_licitacion_20251228_223453.json`
- JSON | tamaño: 452 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__6/finanzas_licitacion_20251229_000545.json`
- JSON | tamaño: 819 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__6/items_licitacion_20251229_000102.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2049 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__7/finanzas_licitacion_20251229_014742.json`
- JSON | tamaño: 819 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__7/items_licitacion_20251229_014309.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 2056 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__8/finanzas_licitacion_20251229_021500.json`
- JSON | tamaño: 744 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/1_bases_5300_44_l125__8/items_licitacion_20251229_021009.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 1746 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523/homologacion_productos.json`
- JSON | tamaño: 2655 bytes | LOC aprox: 57
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523/prompt_generado.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 8417 bytes | LOC aprox: 222
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos para licitaciones públicas.
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523/resp_llm_homologacion.json`
- JSON | tamaño: 2237 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
[
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/homologacion_productos-4o-mini.json`
- JSON | tamaño: 4467 bytes | LOC aprox: 106
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/homologacion_productos.json`
- JSON | tamaño: 4390 bytes | LOC aprox: 82
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/prompt_generado-4o-mini.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 8138 bytes | LOC aprox: 171
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos en el contexto de licitaciones públicas. Se te entregará un listado de ítems detectados en una licitación y un catálogo de productos disponibles. Tu tarea es comparar semánticamente cada ítem contra los productos y devolver los 3 productos más similares por cada ítem, ordenados por un score de similitud (entre 0 y 1).
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/prompt_generado.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 8138 bytes | LOC aprox: 171
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos en el contexto de licitaciones públicas. Se te entregará un listado de ítems detectados en una licitación y un catálogo de productos disponibles. Tu tarea es comparar semánticamente cada ítem contra los productos y devolver los 3 productos más similares por cada ítem, ordenados por un score de similitud (entre 0 y 1).
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old/resp_llm_homologacion.json`
- JSON | tamaño: 3926 bytes | LOC aprox: 70
**Encabezado/comentario (snippet):**
```
[
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old2/homologacion_productos.json`
- JSON | tamaño: 3469 bytes | LOC aprox: 82
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old2/prompt_generado.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 8138 bytes | LOC aprox: 171
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos en el contexto de licitaciones públicas. Se te entregará un listado de ítems detectados en una licitación y un catálogo de productos disponibles. Tu tarea es comparar semánticamente cada ítem contra los productos y devolver los 3 productos más similares por cada ítem, ordenados por un score de similitud (entre 0 y 1).
```

### `salida_json/6e5a09ad-0b71-4cc0-adb7-a8494a267523-old2/resp_llm_homologacion.json`
- JSON | tamaño: 3000 bytes | LOC aprox: 70
**Encabezado/comentario (snippet):**
```
[
```

### `salida_json/bases_administrativas_especiales__26/finanzas_licitacion_20251228_213756.json`
- JSON | tamaño: 184 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/bases_administrativas_especiales__26/items_licitacion_20251228_213418.json`
- JSON | tamaño: 13581 bytes | LOC aprox: 295
**Encabezado/comentario (snippet):**
```
{
```

### `salida_json/bases_administrativas_especiales__27/datos_basicos_licitacion_20251230_182258.json`
- JSON | tamaño: 534 bytes | LOC aprox: 10
**Encabezado/comentario (snippet):**
```
{
```

### `services/chat_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 7274 bytes | LOC aprox: 155

### `services/embedding_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 10365 bytes | LOC aprox: 289

### `services/licitacion_service.py`
- Python — Servicios/Lógica de negocio | tamaño: 10809 bytes | LOC aprox: 324

### `services/llm_service.py`
- Python — Servicios/Lógica de negocio | tamaño: 3787 bytes | LOC aprox: 116
- Funciones: _guardar_llm_raw_json, run_llm_raw, run_llm_raw_with_tokens

### `services/pdf_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 5782 bytes | LOC aprox: 132
- Funciones: process_pdf, registrar_error_reproceso

### `services/__init__.py`
- Python | tamaño: 0 bytes

### `services/homologacion/homologacion_db.py`
- Python | tamaño: 5952 bytes | LOC aprox: 132
- Funciones: save_homologacion_result

### `services/homologacion/homologacion_model.py`
- Python — Modelo/Validación Pydantic; Modelos/Esquemas — Tech: Pydantic (modelos/validación) | tamaño: 1087 bytes | LOC aprox: 42
- Clases: ProductoHomologado, CandidatoHomologacion, ResultadoHomologacion, ResumenHomologacionProductos, RespuestaHomologacionProductos

### `services/homologacion/homologador.py`
- Python | tamaño: 4467 bytes | LOC aprox: 98
- Funciones: homologar_productos_para_licitacion

### `services/homologacion/models.py`
- Python — Modelos/Esquemas | tamaño: 1199 bytes | LOC aprox: 40
- Clases: ProductoBase, ItemDetectado, ProductoHomologado, ResultadoHomologacion, ResultadoHomologacionLicitacion

### `services/homologacion/product_loader.py`
- Python | tamaño: 1586 bytes | LOC aprox: 40
- Funciones: cargar_productos_catalogo

### `services/homologacion/__init__.py`
- Python | tamaño: 2 bytes | LOC aprox: 1

### `services/homologacion/models/schema.py`
- Python | tamaño: 1046 bytes | LOC aprox: 45
- Clases: ProductoCatalogo, ItemLicitacion, ProductoHomologado, CandidatoHomologacion, ResultadoHomologacion, ResultadoHomologacionLicitacion

### `services/homologacion/models/__init__.py`
- Python | tamaño: 2 bytes | LOC aprox: 1

### `services/homologacion/prompts/prompt_homologacion_v1.txt`
- Text | tamaño: 3743 bytes | LOC aprox: 122
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos para procesos de compra pública.
### FORMATO DE SALIDA (OBLIGATORIO)
```

### `services/homologacion/prompts/prompt_homologacion_v2.txt`
- Text | tamaño: 2862 bytes | LOC aprox: 69
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos en el contexto de licitaciones públicas. Se te entregará un listado de ítems detectados en una licitación y un catálogo de productos disponibles. Tu tarea es comparar semánticamente cada ítem contra los productos y devolver los 3 productos más similares por cada ítem, ordenados por un score de similitud (entre 0 y 1).
```

### `services/homologacion/prompts/prompt_homologacion_v3.txt`
- Text | tamaño: 3141 bytes | LOC aprox: 120
**Encabezado/comentario (snippet):**
```
Eres un asistente experto en homologación de productos para licitaciones públicas.
```

### `services/semantic_extraction/debug_llm_raw_items_licitacion_20251226_234850.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 6812 bytes | LOC aprox: 130
**Encabezado/comentario (snippet):**
```
{
```

### `services/semantic_extraction/debug_semantic_ITEMS_LICITACION_20251226_234850.json`
- JSON | tamaño: 10630 bytes | LOC aprox: 229
**Encabezado/comentario (snippet):**
```
{
```

### `services/semantic_extraction/registry.py`
- Python | tamaño: 1877 bytes | LOC aprox: 55
- Funciones: register_extractor, get_extractor

### `services/semantic_extraction/runner.py`
- Python — Tech: Redis (cache/colas) | tamaño: 9680 bytes | LOC aprox: 262

### `services/semantic_extraction/__init__.py`
- Python | tamaño: 31 bytes | LOC aprox: 1

### `services/semantic_extraction/extractors/base_extractor.py`
- Python | tamaño: 6295 bytes | LOC aprox: 189

### `services/semantic_extraction/extractors/datos_basicos_licitacion/datos_basicos_extractor.py`
- Python | tamaño: 3615 bytes | LOC aprox: 112
- Clases: DatosBasicosLicitacionExtractor
- Funciones: build_queries, build_prompt, parse_output

### `services/semantic_extraction/extractors/datos_basicos_licitacion/normalizer.py`
- Python | tamaño: 1180 bytes | LOC aprox: 36
- Funciones: normalize_datos_basicos_licitacion, _clean

### `services/semantic_extraction/extractors/datos_basicos_licitacion/schema.py`
- Python | tamaño: 2629 bytes | LOC aprox: 88
- Clases: DatosBasicosLicitacionSchemaError
- Funciones: _strip_markdown_code_block, validate_datos_basicos_licitacion_schema

### `services/semantic_extraction/extractors/finanzas_licitacion/finanzas_licitacion_extractor.py`
- Python | tamaño: 4049 bytes | LOC aprox: 111
- Clases: FinanzasLicitacionExtractor
- Funciones: build_queries, build_prompt, parse_output, persist_resultado

### `services/semantic_extraction/extractors/finanzas_licitacion/normalizer.py`
- Python | tamaño: 877 bytes | LOC aprox: 29
- Funciones: normalize_finanzas_licitacion, _clean

### `services/semantic_extraction/extractors/finanzas_licitacion/schema.py`
- Python | tamaño: 1912 bytes | LOC aprox: 73
- Clases: FinanzasLicitacionSchemaError
- Funciones: _strip_markdown_code_block, validate_finanzas_licitacion_schema

### `services/semantic_extraction/extractors/items_licitacion/items_licitacion_extractor.py`
- Python | tamaño: 7140 bytes | LOC aprox: 227
- Clases: ItemsLicitacionExtractor
- Funciones: clean_json_output, build_queries, build_prompt, parse_output

### `services/semantic_extraction/extractors/items_licitacion/normalizer.py`
- Python — Tech: Redis (cache/colas) | tamaño: 4395 bytes | LOC aprox: 138
- Funciones: _normalize_text, _build_fuente_resumen, _detect_embedded_items, normalize_items_licitacion

### `services/semantic_extraction/extractors/items_licitacion/schema.py`
- Python — Tech: Redis (cache/colas) | tamaño: 6457 bytes | LOC aprox: 166

### `services/semantic_extraction/prompts/datos_basicos_licitacion/prompt_datos_basicos_licitacion_v1.txt`
- Text | tamaño: 1472 bytes | LOC aprox: 55
**Encabezado/comentario (snippet):**
```
==============================
```

### `services/semantic_extraction/prompts/finanzas_licitacion/prompt_finanzas_licitacion_v1.txt`
- Text | tamaño: 630 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
==============================
```

### `services/semantic_extraction/prompts/items_licitacion/prompt_items_licitacion_v1.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 3761 bytes | LOC aprox: 134
**Encabezado/comentario (snippet):**
```
==============================
```

### `services/semantic_extraction/prompts/items_licitacion/prompt_items_licitacion_v2.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 5130 bytes | LOC aprox: 166
**Encabezado/comentario (snippet):**
```
==============================
```

### `services/semantic_extraction/prompts/items_licitacion/prompt_items_licitacion_v3.txt`
- Text — Tech: Redis (cache/colas) | tamaño: 4697 bytes | LOC aprox: 158
**Encabezado/comentario (snippet):**
```
==============================
```

### `services/semantic_extraction/utils/semantic_utils.py`
- Python — Utilidades | tamaño: 0 bytes

### `share/man/man1/ttx.1`
- Archivo | tamaño: 5601 bytes

### `sql/1-finanzas_licitacion.sql`
- SQL | tamaño: 2215 bytes | LOC aprox: 70
**Encabezado/comentario (snippet):**
```
-- =========================================================
```

### `sql/2-item_licitacion_especificaciones.sql`
- SQL | tamaño: 1875 bytes | LOC aprox: 40

### `sql/3-licitacion_add_campos.sql`
- SQL | tamaño: 66 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
ALTER TABLE licitaciones
```

### `sql/4-finanzas_licitacion_add_campos.sql`
- SQL | tamaño: 184 bytes | LOC aprox: 6
**Encabezado/comentario (snippet):**
```
ALTER TABLE finanzas_licitacion
```

### `sql/5-homologacion_productos.sql`
- SQL | tamaño: 1386 bytes | LOC aprox: 36
**Encabezado/comentario (snippet):**
```
-- ==============================================
```

### `sql/create-inicial.sql`
- SQL — Tech: Redis (cache/colas) | tamaño: 6629 bytes | LOC aprox: 161
**Encabezado/comentario (snippet):**
```
-- ==========================================
```

### `static/css/style.css`
- CSS — Archivos estáticos (CSS/JS/Imágenes) | tamaño: 6129 bytes | LOC aprox: 301
**Encabezado/comentario (snippet):**
```
:root {
/* Navegación principal y secundaria */
```

### `static/css/theme-glass.css`
- CSS — Archivos estáticos (CSS/JS/Imágenes) | tamaño: 2612 bytes | LOC aprox: 113
**Encabezado/comentario (snippet):**
```
/* ======== Variables de color y fondo ======== */
/* ======== Reset básico ======== */
/* ======== Contenedores ======== */
/* ======== Input ======== */
```

### `templates/chat.html`
- HTML — Templates HTML — Tech: Redis (cache/colas) | tamaño: 4954 bytes | LOC aprox: 149
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
  <!-- Usa url_for para que funcione aunque cambie el prefijo de la app -->
```

### `templates/chat_embedding.html`
- HTML — Templates HTML | tamaño: 7156 bytes | LOC aprox: 185
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
```

### `templates/detalle_licitacion.html`
- HTML — Templates HTML | tamaño: 6590 bytes | LOC aprox: 226
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
```

### `templates/extraccion.html`
- HTML — Templates HTML | tamaño: 2399 bytes | LOC aprox: 74
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
```

### `templates/home.html`
- HTML — Templates HTML | tamaño: 768 bytes | LOC aprox: 23
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
    <!-- Podrías poner aquí un banner o instrucciones generales -->
```

### `templates/licitaciones.html`
- HTML — Templates HTML | tamaño: 6575 bytes | LOC aprox: 224
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
    /* Estilos específicos del listado */
```

### `templates/listado.html`
- HTML — Templates HTML | tamaño: 350 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
  <!-- Lista de documentos disponibles -->
```

### `tests/manual/base_extractor_simplificado.py`
- Python | tamaño: 602 bytes | LOC aprox: 20
- Clases: BaseExtractor
- Funciones: concepto, build_queries, build_prompt, parse_output, run

### `tests/manual/items_extractor_manual.py`
- Python | tamaño: 751 bytes | LOC aprox: 23
- Clases: ItemsLicitacionExtractor
- Funciones: concepto, build_queries, build_prompt, parse_output

### `tests/manual/runner_homologacion_manual.py`
- Python | tamaño: 1659 bytes | LOC aprox: 43
- Funciones: main

### `tests/manual/test_extract_items_manual.py`
- Python — Pruebas | tamaño: 1453 bytes | LOC aprox: 38

### `tests/manual/test_runner_semantic_only.py`
- Python — Pruebas — Tech: Redis (cache/colas) | tamaño: 3844 bytes | LOC aprox: 111
- Funciones: obtener_claves_paginas, datetime_converter

### `utils/clean_text.py`
- Python | tamaño: 197 bytes | LOC aprox: 8
- Funciones: limpiar_texto

### `utils/file_utils.py`
- Python — Utilidades | tamaño: 2404 bytes | LOC aprox: 62
- Funciones: guardar_resultados, normalizar_nombre

### `utils/pdf_utils.py`
- Python — Utilidades | tamaño: 1152 bytes | LOC aprox: 32
- Funciones: extraer_paginas_pdf

### `utils/redis_utils.py`
- Python — Utilidades — Tech: Redis (cache/colas) | tamaño: 3756 bytes | LOC aprox: 120
- Funciones: guardar_en_redis, leer_hash, get_redis_connection
