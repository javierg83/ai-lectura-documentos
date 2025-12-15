# Project Plan — Resumen de Componentes

_Generado automáticamente el 2025-12-13 18:49 UTC_

- **Raíz analizada:** `C:\Desarrollo\IA\Proyectos\ai-lectura-documentos`
- **Archivos (texto y binarios):** 642
- **LOC (estimado):** 57767

## Lenguajes / Tipos (conteo)
- JSON: 404
- Other: 106
- Text: 65
- Python: 57
- HTML: 5
- Batch: 2
- CSS: 1
- Config: 1
- PowerShell: 1

## Árbol del proyecto (resumido)
```
📁 ai-lectura-documentos/
  └─ 📄 .env
  └─ 📄 a_extraccion_paginas_pdf.py
  └─ 📄 ai_esp_credito_consumo.py
  └─ 📄 ai_esp_hipotecarios.py
  └─ 📄 ai_esp_hipotecarios_estudio_titulo.py
  └─ 📄 ai_esp_licitaciones.py
  └─ 📄 ai_extractor_pdf copy 2.py
  └─ 📄 ai_extractor_pdf copy 3.py
  └─ 📄 ai_extractor_pdf copy 4.py
  └─ 📄 ai_extractor_pdf copy 5.py
  └─ 📄 ai_extractor_pdf copy.py
  └─ 📄 ai_extractor_pdf.py
  └─ 📄 app copy.py
  └─ 📄 app.py
  └─ 📄 borrar_claves_redis.py
  └─ 📄 borrar_todo_redis.py
  └─ 📄 CI-Javier.txt
  └─ 📄 CI-Javier_resultado_paginas.json
  └─ 📄 CI-Javier_tokens.txt
  └─ 📄 config.py
  └─ 📄 create_index.py
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
  └─ 📄 informe de titulos GALLARDO JIMENEZ.txt
  └─ 📄 informe de titulos GALLARDO JIMENEZ_resultado_paginas.json
  └─ 📄 informe de titulos GALLARDO JIMENEZ_tokens.txt
  └─ 📄 licitacion-imagenes-1pag.txt
  └─ 📄 licitacion-imagenes-1pag_resultado_paginas.json
  └─ 📄 licitacion-imagenes-1pag_tokens.txt
  └─ 📄 main copy.py
  └─ 📄 main.py
  └─ 📄 ocr_utils.py
  └─ 📄 orquestador_documental.py
  └─ 📄 paginas_extraidas-10.txt
  └─ 📄 paginas_extraidas-10_resultado_paginas.json
  └─ 📄 paginas_extraidas-10_tokens.txt
  └─ 📄 paginas_extraidas-4o-mini.txt
  └─ 📄 paginas_extraidas-4o.txt
  └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla.txt
  └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json
  └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt
  └─ 📄 paginas_extraidas1.txt
  └─ 📄 paginas_extraidas_resultado_paginas-4o-mini.json
  └─ 📄 paginas_extraidas_resultado_paginas-4o.json
  └─ 📄 paginas_extraidas_resultado_paginas1.json
  └─ 📄 paginas_extraidas_tokens-4o-mini.txt
  └─ 📄 paginas_extraidas_tokens-4o.txt
  └─ 📄 paginas_extraidas_tokens1.txt
  └─ 📄 pdf_generator.py
  └─ 📄 pdf_selectable.py
  └─ 📄 pdf_utils.py
  └─ 📄 processor.py
  └─ 📄 Promesa-CV-Javier-4o-mini.txt
  └─ 📄 Promesa-CV-Javier.txt
  └─ 📄 Promesa-CV-Javier_resultado_paginas-4o-mini.json
  └─ 📄 Promesa-CV-Javier_resultado_paginas.json
  └─ 📄 Promesa-CV-Javier_tokens-4o-mini.txt
  └─ 📄 Promesa-CV-Javier_tokens.txt
  └─ 📄 prueba_convolucion_img.py
  └─ 📄 pyvenv.cfg
  └─ 📄 redis_uploader.py
  └─ 📄 redis_vector_demo.py
  └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red.txt
  └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_resultado_paginas.json
  └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_tokens.txt
  └─ 📄 reporte_embeddings_general.xlsx
  └─ 📄 reporte_validacion_embeddings.csv
  └─ 📄 tabla_acreditacion.xlsx
  └─ 📄 tabla_exacta_refundida.xlsx
  └─ 📄 test copy 2.py
  └─ 📄 test copy 3.py
  └─ 📄 test copy.py
  └─ 📄 test.py
  └─ 📄 test_redis.py
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla.txt
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt
  └─ 📄 validar_embedding_redis.py
  └─ 📄 validar_embeddings_generico.py
📁 Imagenes Ejemplo Convolucion/
  └─ 📄 pag2.jpg
  └─ 📄 salida_convolucion.png
  └─ 📄 salida_gris.png
📁 Include/
📁 Scripts/
  └─ 📄 activate
  └─ 📄 activate.bat
  └─ 📄 Activate.ps1
  └─ 📄 deactivate.bat
  └─ 📄 distro.exe
  └─ 📄 dotenv.exe
  └─ 📄 dumppdf.py
  └─ 📄 f2py.exe
  └─ 📄 flask.exe
  └─ 📄 fonttools.exe
  └─ 📄 httpx.exe
  └─ 📄 normalizer.exe
  └─ 📄 numpy-config.exe
  └─ 📄 openai.exe
  └─ 📄 pdf2txt.py
  └─ 📄 pdfplumber.exe
  └─ 📄 pip.exe
  └─ 📄 pip3.12.exe
  └─ 📄 pip3.exe
  └─ 📄 pyftmerge.exe
  └─ 📄 pyftsubset.exe
  └─ 📄 pymupdf.exe
  └─ 📄 pypdfium2.exe
  └─ 📄 pytesseract.exe
  └─ 📄 python.exe
  └─ 📄 pythonw.exe
  └─ 📄 tqdm.exe
  └─ 📄 ttx.exe
📁 archivos/
  └─ 📄 archivo_cortado.pdf
  └─ 📄 ASME B31.8 2007_Gas_Transmission.pdf
  └─ 📄 ASME B31.8-2007_archivo_cortado.pdf
  └─ 📄 ASME B31.8-2007_archivo_cortado_1.pdf
  └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf
  └─ 📄 bono-foto-pdf.pdf
  └─ 📄 cheque-ejemplo.jpeg
  └─ 📄 cheque-pdf.pdf
  └─ 📄 cheque2.jpeg
  └─ 📄 CI-Javier.pdf
  └─ 📄 ec-master-nacional.pdf
  └─ 📄 ec-visa-nacional.pdf
  └─ 📄 ec-visa-nacional_desbloqueado.pdf
  └─ 📄 eecc-texto.txt
  └─ 📄 ejemplo-cheque.pdf
  └─ 📄 ejemplo-con-check-imagenes-titulos.pdf
  └─ 📄 ejemplo_con_checkbox.pdf
  └─ 📄 informe de titulos GALLARDO JIMENEZ.pdf
  └─ 📄 licitacion-imagenes-1pag.pdf
  └─ 📄 licitacion-imagenes.pdf
  └─ 📄 paginas_extraidas-2-pag.pdf
  └─ 📄 paginas_extraidas-2paginas.pdf
  └─ 📄 paginas_extraidas-energia-tablas-formulas.pdf
  └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla.pdf
  └─ 📄 Promesa-CV-Javier-1pag.pdf
  └─ 📄 Promesa-CV-Javier.pdf
  └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red.pdf
  └─ 📄 texto_extraido.txt
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf
📁 archivos_entrada_temp/
  └─ 📄 bono-foto-pdf.pdf
  └─ 📄 cheque-ejemplo.jpeg
  └─ 📄 cheque-pdf.pdf
  └─ 📄 cheque2.jpeg
  └─ 📄 ec-master-nacional.pdf
  └─ 📄 ec-visa-nacional.pdf
  └─ 📄 ec-visa-nacional_desbloqueado.pdf
  └─ 📄 eecc-texto.txt
  └─ 📄 ejemplo-cheque.pdf
  └─ 📄 ejemplo-con-check-imagenes-titulos.pdf
  └─ 📄 ejemplo_con_checkbox.pdf
  └─ 📄 informe de titulos GALLARDO JIMENEZ.pdf
  └─ 📄 licitacion-imagenes-1pag.pdf
  └─ 📄 licitacion-imagenes.pdf
  └─ 📄 Promesa-CV-Javier-1pag.pdf
  └─ 📄 Promesa-CV-Javier.pdf
  └─ 📄 texto_extraido.txt
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf
📁 archivos_texto/
  └─ 📄 archivo_cortado.txt
  └─ 📄 archivo_cortado_resultado_paginas.json
  └─ 📄 archivo_cortado_tokens.txt
  └─ 📄 CI-Javier.txt
  └─ 📄 CI-Javier_resultado_paginas.json
  └─ 📄 CI-Javier_tokens.txt
  └─ 📄 ejemplo-con-check-imagenes-titulos.txt
  └─ 📄 ejemplo-con-check-imagenes-titulos_resultado_paginas.json
  └─ 📄 ejemplo-con-check-imagenes-titulos_tokens.txt
  └─ 📄 ejemplo_con_checkbox.txt
  └─ 📄 ejemplo_con_checkbox_resultado_paginas copy.json
  └─ 📄 ejemplo_con_checkbox_tokens.txt
  └─ 📄 informe de titulos GALLARDO JIMENEZ_resultado_paginas.json
  └─ 📄 paginas_extraidas-2-pag.txt
  └─ 📄 paginas_extraidas-2-pag_resultado_paginas.json
  └─ 📄 paginas_extraidas-2-pag_tokens.txt
  └─ 📄 paginas_extraidas-2paginas.txt
  └─ 📄 paginas_extraidas-2paginas_resultado_paginas.json
  └─ 📄 paginas_extraidas-2paginas_tokens.txt
  └─ 📄 paginas_extraidas-energia-tablas-formulas.txt
  └─ 📄 paginas_extraidas-energia-tablas-formulas_resultado_paginas.json
  └─ 📄 paginas_extraidas-energia-tablas-formulas_tokens.txt
  └─ 📄 paginas_extraidas.txt
  └─ 📄 paginas_extraidas_resultado_paginas.json
  └─ 📄 paginas_extraidas_tokens.txt
  └─ 📄 Promesa-CV-Javier-1pag.txt
  └─ 📄 Promesa-CV-Javier-1pag_resultado_paginas.json
  └─ 📄 Promesa-CV-Javier-1pag_tokens.txt
  └─ 📄 Promesa-CV-Javier.txt
  └─ 📄 Promesa-CV-Javier_resultado_paginas.json
  └─ 📄 Promesa-CV-Javier_tokens.txt
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json
  └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_raw.json
📁 prompts/
📁 routes/
  └─ 📄 __init__.py
  └─ 📄 chat.py
  └─ 📄 chat_embedding.py
  └─ 📄 extraction.py
📁 services/
  └─ 📄 __init__.py
  └─ 📄 chat_service.py
  └─ 📄 embedding_service.py
  └─ 📄 pdf_service.py
📁 share/
📁 static/
📁 templates/
  └─ 📄 chat.html
  └─ 📄 chat_embedding.html
  └─ 📄 extraccion.html
  └─ 📄 home.html
  └─ 📄 listado.html
📁 utils/
  └─ 📄 clean_text.py
  └─ 📄 file_utils.py
  └─ 📄 pdf_utils.py
  └─ 📄 redis_utils.py
  📁 CI-Javier/
    └─ 📄 CI-Javier-Atras.jpeg
    └─ 📄 CI-Javier-Frente.jpeg
    └─ 📄 CI-Javier.docx
    └─ 📄 CI-Javier.pdf
    └─ 📄 debug_con_rectangulo.png
    └─ 📄 firma_recortada.png
  📁 doc energia/
    └─ 📄 49 CFR ch.1 Pt. 192 (10-1-07 Edition).pdf
    └─ 📄 ASME B31.8 2007_Gas_Transmission.pdf
    └─ 📄 ASME B31.8-2007_archivo_cortado.pdf
    └─ 📄 ASME B31.8-2007_archivo_cortado_1.pdf
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf
    └─ 📄 paginas_extraidas-energia-tablas-formulas.pdf
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red.pdf
  📁 ASME B31.8 2007_Gas_Transmission/
    └─ 📄 ASME B31.8 2007_Gas_Transmission.pdf
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_1.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_10.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_100.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_101.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_102.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_103.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_104.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_105.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_106.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_107.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_108.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_109.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_11.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_110.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_111.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_112.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_113.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_114.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_115.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_116.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_117.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_118.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_119.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_12.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_120.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_121.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_122.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_123.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_124.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_125.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_126.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_127.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_128.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_129.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_13.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_130.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_131.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_132.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_133.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_134.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_135.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_136.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_137.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_138.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_139.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_14.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_140.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_141.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_142.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_143.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_144.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_145.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_146.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_147.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_148.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_149.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_15.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_150.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_151.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_152.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_153.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_154.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_155.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_156.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_157.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_158.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_159.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_16.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_160.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_161.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_162.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_163.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_164.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_165.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_166.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_167.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_168.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_169.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_17.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_170.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_171.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_172.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_173.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_174.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_175.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_176.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_177.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_178.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_179.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_18.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_180.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_181.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_182.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_183.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_184.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_185.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_186.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_187.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_188.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_189.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_19.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_190.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_191.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_192.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_193.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_194.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_195.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_196.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_197.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_198.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_199.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_2.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_20.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_200.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_201.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_202.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_21.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_22.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_23.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_24.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_25.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_26.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_27.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_28.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_29.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_3.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_30.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_31.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_32.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_33.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_34.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_35.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_36.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_37.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_38.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_39.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_4.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_40.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_41.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_42.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_43.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_44.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_45.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_46.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_47.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_48.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_49.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_5.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_50.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_51.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_52.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_53.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_54.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_55.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_56.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_57.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_58.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_59.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_6.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_60.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_61.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_62.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_63.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_64.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_65.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_66.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_67.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_68.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_69.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_7.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_70.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_71.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_72.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_73.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_74.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_75.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_76.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_77.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_78.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_79.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_8.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_80.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_81.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_82.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_83.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_84.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_85.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_86.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_87.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_88.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_89.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_9.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_90.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_91.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_92.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_93.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_94.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_95.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_96.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_97.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_98.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_pag_99.json
    └─ 📄 ASME B31.8 2007_Gas_Transmission_raw_data.json
  📁 ASME B31.8-2007_archivo_cortado_1/
    └─ 📄 ASME B31.8-2007_archivo_cortado_1.pdf
    └─ 📄 ASME B31.8-2007_archivo_cortado_1_pag_1.json
    └─ 📄 ASME B31.8-2007_archivo_cortado_1_pag_2.json
    └─ 📄 ASME B31.8-2007_archivo_cortado_1_pag_3.json
    └─ 📄 ASME B31.8-2007_archivo_cortado_1_pag_4.json
    └─ 📄 ASME B31.txt
    └─ 📄 ASME B31_resultado_paginas.json
    └─ 📄 ASME B31_tokens.txt
  📁 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_1.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_10.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_11.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_12.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_13.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_14.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_15.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_16.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_17.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_18.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_19.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_2.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_20.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_21.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_22.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_23.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_24.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_25.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_26.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_27.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_28.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_29.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_3.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_30.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_31.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_32.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_33.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_34.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_35.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_36.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_37.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_38.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_39.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_4.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_40.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_41.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_42.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_43.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_44.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_45.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_46.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_47.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_48.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_49.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_5.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_50.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_51.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_52.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_53.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_54.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_55.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_56.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_57.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_58.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_59.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_6.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_60.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_61.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_62.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_63.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_64.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_65.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_66.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_67.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_68.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_69.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_7.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_70.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_8.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_9.json
    └─ 📄 ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_raw_data.json
  📁 BASES_ADMINISTRATIVAS_ESPECIALES/
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES.pdf
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES.txt
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES_pag_1.json
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES_pag_2.json
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES_resultado_paginas.json
    └─ 📄 BASES_ADMINISTRATIVAS_ESPECIALES_tokens.txt
    └─ 📄 errores_embedding.log
  📁 Basesadministrativas (6)/
    └─ 📄 Basesadministrativas (6).pdf
    └─ 📄 Basesadministrativas (6).txt
    └─ 📄 Basesadministrativas (6)_pag_1.json
    └─ 📄 Basesadministrativas (6)_pag_2.json
    └─ 📄 Basesadministrativas (6)_pag_3.json
    └─ 📄 Basesadministrativas (6)_pag_4.json
    └─ 📄 Basesadministrativas (6)_resultado_paginas.json
    └─ 📄 Basesadministrativas (6)_tokens.txt
  📁 CI-Javier/
    └─ 📄 CI-Javier_pag_1.json
    └─ 📄 CI-Javier_resultado.json
  📁 DOMINIO/
    └─ 📄 DOMINIO.PDF
    └─ 📄 DOMINIO.txt
    └─ 📄 DOMINIO_pag_1.json
    └─ 📄 DOMINIO_pag_2.json
    └─ 📄 DOMINIO_resultado_paginas.json
    └─ 📄 DOMINIO_tokens.txt
  📁 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/
    └─ 📄 errores_embedding.log
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768.pdf
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768.txt
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_pag_1.json
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_pag_2.json
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_resultado_paginas.json
    └─ 📄 Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_tokens.txt
  📁 Promesa-CV-Javier/
    └─ 📄 Promesa-CV-Javier_page_1.json
    └─ 📄 Promesa-CV-Javier_page_2.json
    └─ 📄 Promesa-CV-Javier_page_3.json
    └─ 📄 Promesa-CV-Javier_page_4.json
    └─ 📄 Promesa-CV-Javier_page_5.json
    └─ 📄 Promesa-CV-Javier_page_6.json
    └─ 📄 Promesa-CV-Javier_page_7.json
    └─ 📄 Promesa-CV-Javier_page_8.json
    └─ 📄 Promesa-CV-Javier_page_9.json
    └─ 📄 Promesa-CV-Javier_raw_data.json
  📁 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/
    └─ 📄 errores_embedding.log
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1).pdf
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1).txt
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_1.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_10.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_11.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_12.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_13.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_14.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_15.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_16.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_17.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_18.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_19.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_2.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_20.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_21.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_22.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_23.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_24.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_25.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_26.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_27.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_28.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_29.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_3.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_30.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_31.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_32.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_33.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_34.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_35.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_36.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_37.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_38.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_39.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_4.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_40.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_41.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_42.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_43.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_44.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_45.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_46.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_47.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_48.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_49.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_5.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_50.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_6.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_7.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_8.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_9.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_resultado_paginas.json
    └─ 📄 RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_tokens.txt
  📁 Reglamento N°280 Seguridad Transp. Dist. Gas Red/
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_1.json
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_2.json
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_3.json
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_4.json
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_raw_data.json
    └─ 📄 Reglamento N°280 Seguridad Transp. Dist. Gas Red_tokens.txt
  📁 informe de titulos GALLARDO JIMENEZ/
    └─ 📄 informe de titulos GALLARDO JIMENEZ.pdf
    └─ 📄 informe de titulos GALLARDO JIMENEZ.txt
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_1.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_2.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_3.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_4.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_5.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_6.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_7.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_pag_8.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_raw_data.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_resultado_paginas.json
    └─ 📄 informe de titulos GALLARDO JIMENEZ_tokens.txt
  📁 paginas_extraidas-licitacion-2-pag-con-tabla/
    └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json
    └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json
    └─ 📄 paginas_extraidas-licitacion-2-pag-con-tabla_resultado.json
  📁 v3-paginas_extraidas-licitacion-2-pag-con-tabla/
    └─ 📄 errores_embedding.log
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla.txt
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_raw_data.json
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json
    └─ 📄 v3-paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt
  📁 man/
  📁 css/
    └─ 📄 style.css
    📁 man1/
      └─ 📄 ttx.1
```

## Dependencias & Infra (resumen)

## Componentes y propósito (por archivo)
### `.env`
- Tech: Flask (API web), Redis (cache/colas) | tamaño: 1197 bytes

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

### `ai_extractor_pdf copy 2.py`
- Python | tamaño: 2188 bytes | LOC aprox: 64
- Funciones: count_tokens, analyze_page_with_gpt

### `ai_extractor_pdf copy 3.py`
- Python | tamaño: 2505 bytes | LOC aprox: 71
- Funciones: count_tokens, analyze_page_with_gpt

### `ai_extractor_pdf copy 4.py`
- Python | tamaño: 3462 bytes | LOC aprox: 85
- Funciones: count_tokens, analyze_page_with_gpt

### `ai_extractor_pdf copy 5.py`
- Python | tamaño: 4889 bytes | LOC aprox: 107
- Funciones: count_tokens, analyze_page_with_gpt

### `ai_extractor_pdf copy.py`
- Python | tamaño: 2030 bytes | LOC aprox: 51
- Funciones: count_tokens, analyze_page_with_gpt

### `ai_extractor_pdf.py`
- Python | tamaño: 6029 bytes | LOC aprox: 131
- Funciones: count_tokens, analyze_page_with_gpt

### `app copy.py`
- Python — Tech: Flask (API web), Redis (cache/colas) | tamaño: 5382 bytes | LOC aprox: 151
- Funciones: home, extraccion_page, chat_page, chat_embedding_page, api_doc_raw, api_chat_embedding

### `app.py`
- Python — Punto de entrada de la app/servidor — Tech: Flask (API web) | tamaño: 1225 bytes | LOC aprox: 34
- Funciones: home, serve_archivos_texto

### `a_extraccion_paginas_pdf.py`
- Python | tamaño: 1308 bytes | LOC aprox: 40
- Funciones: seleccion_paginas_extraccion

### `borrar_claves_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 1117 bytes | LOC aprox: 32
- Funciones: cargar_claves_a_borrar, borrar_claves_en_redis

### `borrar_todo_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 877 bytes | LOC aprox: 29
- Funciones: borrar_todo_redis

### `CI-Javier.txt`
- Text | tamaño: 58 bytes | LOC aprox: 3
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `CI-Javier_resultado_paginas.json`
- JSON | tamaño: 158 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
[
```

### `CI-Javier_tokens.txt`
- Text | tamaño: 84 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1625 output=9
```

### `config.py`
- Python — Configuración — Tech: Redis (cache/colas) | tamaño: 1052 bytes | LOC aprox: 31

### `create_index.py`
- Python — Tech: Redis (cache/colas) | tamaño: 963 bytes | LOC aprox: 31

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
- Python — Modelo/ORM SQLAlchemy; Modelo/Validación Pydantic; Render de templates Jinja2 — Tech: Alembic (migraciones), Celery (jobs/worker), Django (framework web), FastAPI (API web), Flask (API web), Gunicorn (WSGI/ASGI server), HTMX (interacción HTML), HTTPX (cliente HTTP), Jinja2 (templates), Pydantic (modelos/validación), Pytest (tests), Redis (cache/colas), Requests (cliente HTTP), SQLAlchemy (ORM), Unittest (tests), Uvicorn (ASGI server) | tamaño: 20356 bytes | LOC aprox: 521
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

### `informe de titulos GALLARDO JIMENEZ.txt`
- Text | tamaño: 14792 bytes | LOC aprox: 146
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `informe de titulos GALLARDO JIMENEZ_resultado_paginas.json`
- JSON | tamaño: 22440 bytes | LOC aprox: 372
**Encabezado/comentario (snippet):**
```
[
```

### `informe de titulos GALLARDO JIMENEZ_tokens.txt`
- Text | tamaño: 329 bytes | LOC aprox: 11
**Encabezado/comentario (snippet):**
```
Página 1: input=1285 output=782
```

### `licitacion-imagenes-1pag.txt`
- Text | tamaño: 2409 bytes | LOC aprox: 29
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `licitacion-imagenes-1pag_resultado_paginas.json`
- JSON | tamaño: 2594 bytes | LOC aprox: 14
**Encabezado/comentario (snippet):**
```
[
```

### `licitacion-imagenes-1pag_tokens.txt`
- Text | tamaño: 88 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=718
```

### `main copy.py`
- Python — Tech: Redis (cache/colas) | tamaño: 2077 bytes | LOC aprox: 48

### `main.py`
- Python — Punto de entrada de la app/servidor — Tech: Redis (cache/colas) | tamaño: 2272 bytes | LOC aprox: 51

### `ocr_utils.py`
- Python — Utilidades | tamaño: 225 bytes | LOC aprox: 8
- Funciones: image_to_text

### `orquestador_documental.py`
- Python | tamaño: 1013 bytes | LOC aprox: 28
- Funciones: classify_document

### `paginas_extraidas-10.txt`
- Text | tamaño: 3400 bytes | LOC aprox: 40
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `paginas_extraidas-10_resultado_paginas.json`
- JSON | tamaño: 6032 bytes | LOC aprox: 122
**Encabezado/comentario (snippet):**
```
[
```

### `paginas_extraidas-10_tokens.txt`
- Text | tamaño: 123 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=838
```

### `paginas_extraidas-4o-mini.txt`
- Text | tamaño: 48326 bytes | LOC aprox: 282
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `paginas_extraidas-4o.txt`
- Text | tamaño: 49027 bytes | LOC aprox: 321
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `paginas_extraidas-licitacion-2-pag-con-tabla.txt`
- Text | tamaño: 4038 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json`
- JSON | tamaño: 8112 bytes | LOC aprox: 211
**Encabezado/comentario (snippet):**
```
[
```

### `paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt`
- Text | tamaño: 124 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
Página 1: input=1625 output=1271
```

### `paginas_extraidas1.txt`
- Text | tamaño: 28893 bytes | LOC aprox: 188
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `paginas_extraidas_resultado_paginas-4o-mini.json`
- JSON | tamaño: 72412 bytes | LOC aprox: 1319
**Encabezado/comentario (snippet):**
```
[
```

### `paginas_extraidas_resultado_paginas-4o.json`
- JSON | tamaño: 61143 bytes | LOC aprox: 641
**Encabezado/comentario (snippet):**
```
[
```

### `paginas_extraidas_resultado_paginas1.json`
- JSON | tamaño: 37769 bytes | LOC aprox: 454
**Encabezado/comentario (snippet):**
```
[
```

### `paginas_extraidas_tokens-4o-mini.txt`
- Text | tamaño: 636 bytes | LOC aprox: 19
**Encabezado/comentario (snippet):**
```
Página 1: input=36914 output=985
```

### `paginas_extraidas_tokens-4o.txt`
- Text | tamaño: 611 bytes | LOC aprox: 19
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=718
```

### `paginas_extraidas_tokens1.txt`
- Text | tamaño: 400 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=720
```

### `pdf_generator.py`
- Python | tamaño: 938 bytes | LOC aprox: 27
- Funciones: build_pdf_from_json

### `pdf_selectable.py`
- Python | tamaño: 1660 bytes | LOC aprox: 44
- Funciones: analyze_page_selectable

### `pdf_utils.py`
- Python — Utilidades | tamaño: 477 bytes | LOC aprox: 14
- Funciones: get_page_count, extract_page_image

### `processor.py`
- Python — Tech: Redis (cache/colas) | tamaño: 5227 bytes | LOC aprox: 116
- Funciones: convertir_pagina_a_base64, process_pages, guardar_resultados

### `Promesa-CV-Javier-4o-mini.txt`
- Text | tamaño: 13119 bytes | LOC aprox: 52
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `Promesa-CV-Javier.txt`
- Text | tamaño: 13296 bytes | LOC aprox: 76
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `Promesa-CV-Javier_resultado_paginas-4o-mini.json`
- JSON | tamaño: 16985 bytes | LOC aprox: 230
**Encabezado/comentario (snippet):**
```
[
```

### `Promesa-CV-Javier_resultado_paginas.json`
- JSON | tamaño: 15565 bytes | LOC aprox: 133
**Encabezado/comentario (snippet):**
```
[
```

### `Promesa-CV-Javier_tokens-4o-mini.txt`
- Text | tamaño: 371 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
Página 1: input=36914 output=472
```

### `Promesa-CV-Javier_tokens.txt`
- Text | tamaño: 361 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
Página 1: input=1625 output=407
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

### `redis_uploader.py`
- Python — Tech: Redis (cache/colas) | tamaño: 947 bytes | LOC aprox: 28
- Funciones: upload_json_to_redis

### `redis_vector_demo.py`
- Python — Tech: Redis (cache/colas) | tamaño: 220 bytes | LOC aprox: 8

### `Reglamento N°280 Seguridad Transp. Dist. Gas Red.txt`
- Text | tamaño: 12942 bytes | LOC aprox: 60
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `Reglamento N°280 Seguridad Transp. Dist. Gas Red_resultado_paginas.json`
- JSON | tamaño: 17710 bytes | LOC aprox: 236
**Encabezado/comentario (snippet):**
```
[
```

### `Reglamento N°280 Seguridad Transp. Dist. Gas Red_tokens.txt`
- Text | tamaño: 188 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
Página 1: input=1425 output=1190
```

### `reporte_embeddings_general.xlsx`
- Archivo | tamaño: 21137 bytes

### `reporte_validacion_embeddings.csv`
- Archivo | tamaño: 76450 bytes

### `tabla_acreditacion.xlsx`
- Archivo | tamaño: 5873 bytes

### `tabla_exacta_refundida.xlsx`
- Archivo | tamaño: 5874 bytes

### `test copy 2.py`
- Python | tamaño: 670 bytes | LOC aprox: 17

### `test copy 3.py`
- Python — Tech: Redis (cache/colas) | tamaño: 138 bytes | LOC aprox: 4

### `test copy.py`
- Python | tamaño: 5512 bytes | LOC aprox: 145
- Funciones: contar_tokens, extraer_pagina_como_imagen, imagen_a_base64, hacer_ocr, enviar_imagen_a_gpt

### `test.py`
- Python | tamaño: 5385 bytes | LOC aprox: 140
- Funciones: contar_tokens, extraer_pagina_como_imagen, imagen_a_base64, hacer_ocr, enviar_imagen_a_gpt

### `test_redis.py`
- Python — Pruebas — Tech: Redis (cache/colas) | tamaño: 219 bytes | LOC aprox: 6

### `v3-paginas_extraidas-licitacion-2-pag-con-tabla.txt`
- Text | tamaño: 3832 bytes | LOC aprox: 41
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `v3-paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json`
- JSON | tamaño: 6947 bytes | LOC aprox: 167
**Encabezado/comentario (snippet):**
```
[
```

### `v3-paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt`
- Text | tamaño: 124 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
Página 1: input=1625 output=1068
```

### `validar_embeddings_generico.py`
- Python — Tech: Redis (cache/colas) | tamaño: 1261 bytes | LOC aprox: 45

### `validar_embedding_redis.py`
- Python — Tech: Redis (cache/colas) | tamaño: 2577 bytes | LOC aprox: 79
- Funciones: validar_claves

### `archivos/archivo_cortado.pdf`
- Archivo | tamaño: 209733 bytes

### `archivos/ASME B31.8 2007_Gas_Transmission.pdf`
- Archivo | tamaño: 2017548 bytes

### `archivos/ASME B31.8-2007_archivo_cortado.pdf`
- Archivo | tamaño: 209733 bytes

### `archivos/ASME B31.8-2007_archivo_cortado_1.pdf`
- Archivo | tamaño: 73847 bytes

### `archivos/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf`
- Archivo | tamaño: 828030 bytes

### `archivos/bono-foto-pdf.pdf`
- Archivo | tamaño: 159801 bytes

### `archivos/cheque-ejemplo.jpeg`
- Archivo | tamaño: 107887 bytes

### `archivos/cheque-pdf.pdf`
- Archivo | tamaño: 129296 bytes

### `archivos/cheque2.jpeg`
- Archivo | tamaño: 113618 bytes

### `archivos/CI-Javier.pdf`
- Archivo | tamaño: 91662 bytes

### `archivos/ec-master-nacional.pdf`
- Archivo | tamaño: 273929 bytes

### `archivos/ec-visa-nacional.pdf`
- Archivo | tamaño: 277014 bytes

### `archivos/ec-visa-nacional_desbloqueado.pdf`
- Archivo | tamaño: 277014 bytes

### `archivos/eecc-texto.txt`
- Text | tamaño: 5456 bytes | LOC aprox: 136
**Encabezado/comentario (snippet):**
```
= LATAM
```

### `archivos/ejemplo-cheque.pdf`
- Archivo | tamaño: 2543426 bytes

### `archivos/ejemplo-con-check-imagenes-titulos.pdf`
- Archivo | tamaño: 280199 bytes

### `archivos/ejemplo_con_checkbox.pdf`
- Archivo | tamaño: 195857 bytes

### `archivos/informe de titulos GALLARDO JIMENEZ.pdf`
- Archivo | tamaño: 239346 bytes

### `archivos/licitacion-imagenes-1pag.pdf`
- Archivo | tamaño: 184725 bytes

### `archivos/licitacion-imagenes.pdf`
- Archivo | tamaño: 8690205 bytes

### `archivos/paginas_extraidas-2-pag.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos/paginas_extraidas-2paginas.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos/paginas_extraidas-energia-tablas-formulas.pdf`
- Archivo | tamaño: 185883 bytes

### `archivos/paginas_extraidas-licitacion-2-pag-con-tabla.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos/Promesa-CV-Javier-1pag.pdf`
- Archivo | tamaño: 91873 bytes

### `archivos/Promesa-CV-Javier.pdf`
- Archivo | tamaño: 369533 bytes

### `archivos/Reglamento N°280 Seguridad Transp. Dist. Gas Red.pdf`
- Archivo | tamaño: 5542538 bytes

### `archivos/texto_extraido.txt`
- Text | tamaño: 118006 bytes | LOC aprox: 2851
**Encabezado/comentario (snippet):**
```
=== Página 1 ===
```

### `archivos/v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos_entrada_temp/bono-foto-pdf.pdf`
- Archivo | tamaño: 159801 bytes

### `archivos_entrada_temp/cheque-ejemplo.jpeg`
- Archivo | tamaño: 107887 bytes

### `archivos_entrada_temp/cheque-pdf.pdf`
- Archivo | tamaño: 129296 bytes

### `archivos_entrada_temp/cheque2.jpeg`
- Archivo | tamaño: 113618 bytes

### `archivos_entrada_temp/ec-master-nacional.pdf`
- Archivo | tamaño: 273929 bytes

### `archivos_entrada_temp/ec-visa-nacional.pdf`
- Archivo | tamaño: 277014 bytes

### `archivos_entrada_temp/ec-visa-nacional_desbloqueado.pdf`
- Archivo | tamaño: 277014 bytes

### `archivos_entrada_temp/eecc-texto.txt`
- Text | tamaño: 5456 bytes | LOC aprox: 136
**Encabezado/comentario (snippet):**
```
= LATAM
```

### `archivos_entrada_temp/ejemplo-cheque.pdf`
- Archivo | tamaño: 2543426 bytes

### `archivos_entrada_temp/ejemplo-con-check-imagenes-titulos.pdf`
- Archivo | tamaño: 280199 bytes

### `archivos_entrada_temp/ejemplo_con_checkbox.pdf`
- Archivo | tamaño: 195857 bytes

### `archivos_entrada_temp/informe de titulos GALLARDO JIMENEZ.pdf`
- Archivo | tamaño: 239346 bytes

### `archivos_entrada_temp/licitacion-imagenes-1pag.pdf`
- Archivo | tamaño: 184725 bytes

### `archivos_entrada_temp/licitacion-imagenes.pdf`
- Archivo | tamaño: 8690205 bytes

### `archivos_entrada_temp/Promesa-CV-Javier-1pag.pdf`
- Archivo | tamaño: 91873 bytes

### `archivos_entrada_temp/Promesa-CV-Javier.pdf`
- Archivo | tamaño: 369533 bytes

### `archivos_entrada_temp/texto_extraido.txt`
- Text | tamaño: 118006 bytes | LOC aprox: 2851
**Encabezado/comentario (snippet):**
```
=== Página 1 ===
```

### `archivos_entrada_temp/v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos_entrada_temp/CI-Javier/CI-Javier-Atras.jpeg`
- Archivo | tamaño: 73670 bytes

### `archivos_entrada_temp/CI-Javier/CI-Javier-Frente.jpeg`
- Archivo | tamaño: 75005 bytes

### `archivos_entrada_temp/CI-Javier/CI-Javier.docx`
- Archivo | tamaño: 162923 bytes

### `archivos_entrada_temp/CI-Javier/CI-Javier.pdf`
- Archivo | tamaño: 91662 bytes

### `archivos_entrada_temp/CI-Javier/debug_con_rectangulo.png`
- Archivo | tamaño: 404130 bytes

### `archivos_entrada_temp/CI-Javier/firma_recortada.png`
- Archivo | tamaño: 24263 bytes

### `archivos_entrada_temp/doc energia/49 CFR ch.1 Pt. 192 (10-1-07 Edition).pdf`
- Archivo | tamaño: 1497992 bytes

### `archivos_entrada_temp/doc energia/ASME B31.8 2007_Gas_Transmission.pdf`
- Archivo | tamaño: 2017548 bytes

### `archivos_entrada_temp/doc energia/ASME B31.8-2007_archivo_cortado.pdf`
- Archivo | tamaño: 209733 bytes

### `archivos_entrada_temp/doc energia/ASME B31.8-2007_archivo_cortado_1.pdf`
- Archivo | tamaño: 73847 bytes

### `archivos_entrada_temp/doc energia/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf`
- Archivo | tamaño: 828030 bytes

### `archivos_entrada_temp/doc energia/paginas_extraidas-energia-tablas-formulas.pdf`
- Archivo | tamaño: 185883 bytes

### `archivos_entrada_temp/doc energia/Reglamento N°280 Seguridad Transp. Dist. Gas Red.pdf`
- Archivo | tamaño: 5542538 bytes

### `archivos_texto/archivo_cortado.txt`
- Text | tamaño: 5821 bytes | LOC aprox: 87
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/archivo_cortado_resultado_paginas.json`
- JSON | tamaño: 8150 bytes | LOC aprox: 106
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/archivo_cortado_tokens.txt`
- Text | tamaño: 191 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
Página 1: input=1002 output=177
```

### `archivos_texto/CI-Javier.txt`
- Text | tamaño: 97 bytes | LOC aprox: 3
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/CI-Javier_resultado_paginas.json`
- JSON | tamaño: 198 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/CI-Javier_tokens.txt`
- Text | tamaño: 86 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1625 output=14
```

### `archivos_texto/ejemplo-con-check-imagenes-titulos.txt`
- Text | tamaño: 1691 bytes | LOC aprox: 31
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/ejemplo-con-check-imagenes-titulos_resultado_paginas.json`
- JSON | tamaño: 3934 bytes | LOC aprox: 114
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/ejemplo-con-check-imagenes-titulos_tokens.txt`
- Text | tamaño: 90 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1285 output=1007
```

### `archivos_texto/ejemplo_con_checkbox.txt`
- Text | tamaño: 1720 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/ejemplo_con_checkbox_resultado_paginas copy.json`
- JSON | tamaño: 4836 bytes | LOC aprox: 207
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/ejemplo_con_checkbox_tokens.txt`
- Text | tamaño: 88 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1055 output=871
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ_resultado_paginas.json`
- JSON | tamaño: 18868 bytes | LOC aprox: 223
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-2-pag.txt`
- Text | tamaño: 4134 bytes | LOC aprox: 31
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/paginas_extraidas-2-pag_resultado_paginas.json`
- JSON | tamaño: 6482 bytes | LOC aprox: 147
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-2-pag_tokens.txt`
- Text | tamaño: 123 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=946
```

### `archivos_texto/paginas_extraidas-2paginas.txt`
- Text | tamaño: 3079 bytes | LOC aprox: 31
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/paginas_extraidas-2paginas_resultado_paginas.json`
- JSON | tamaño: 6554 bytes | LOC aprox: 149
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-2paginas_tokens.txt`
- Text | tamaño: 123 bytes | LOC aprox: 5
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=946
```

### `archivos_texto/paginas_extraidas-energia-tablas-formulas.txt`
- Text | tamaño: 13346 bytes | LOC aprox: 175
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/paginas_extraidas-energia-tablas-formulas_resultado_paginas.json`
- JSON | tamaño: 17444 bytes | LOC aprox: 224
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-energia-tablas-formulas_tokens.txt`
- Text | tamaño: 193 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
Página 1: input=1002 output=363
```

### `archivos_texto/paginas_extraidas.txt`
- Text | tamaño: 28834 bytes | LOC aprox: 175
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/paginas_extraidas_resultado_paginas.json`
- JSON | tamaño: 36993 bytes | LOC aprox: 414
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas_tokens.txt`
- Text | tamaño: 398 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=720
```

### `archivos_texto/Promesa-CV-Javier-1pag.txt`
- Text | tamaño: 1298 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/Promesa-CV-Javier-1pag_resultado_paginas.json`
- JSON | tamaño: 1483 bytes | LOC aprox: 14
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Promesa-CV-Javier-1pag_tokens.txt`
- Text | tamaño: 88 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=361
```

### `archivos_texto/Promesa-CV-Javier.txt`
- Text | tamaño: 13173 bytes | LOC aprox: 59
**Encabezado/comentario (snippet):**
```
--- Página 1 ---
```

### `archivos_texto/Promesa-CV-Javier_resultado_paginas.json`
- JSON | tamaño: 16110 bytes | LOC aprox: 180
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Promesa-CV-Javier_tokens.txt`
- Text | tamaño: 361 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
Página 1: input=1184 output=361
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json`
- JSON | tamaño: 4440 bytes | LOC aprox: 105
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json`
- JSON | tamaño: 2628 bytes | LOC aprox: 90
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla_raw.json`
- JSON | tamaño: 7467 bytes | LOC aprox: 197
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission.pdf`
- Archivo | tamaño: 2017548 bytes

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_1.json`
- JSON | tamaño: 1905 bytes | LOC aprox: 65
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_10.json`
- JSON | tamaño: 4281 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_100.json`
- JSON | tamaño: 6286 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_101.json`
- JSON | tamaño: 4979 bytes | LOC aprox: 21
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_102.json`
- JSON | tamaño: 5761 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_103.json`
- JSON | tamaño: 5879 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_104.json`
- JSON | tamaño: 5897 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_105.json`
- JSON | tamaño: 5896 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_106.json`
- JSON | tamaño: 2038 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_107.json`
- JSON | tamaño: 4436 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_108.json`
- JSON | tamaño: 2450 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_109.json`
- JSON | tamaño: 4967 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_11.json`
- JSON | tamaño: 3897 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_110.json`
- JSON | tamaño: 5390 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_111.json`
- JSON | tamaño: 5803 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_112.json`
- JSON | tamaño: 5024 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_113.json`
- JSON | tamaño: 5540 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_114.json`
- JSON | tamaño: 5342 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_115.json`
- JSON | tamaño: 4847 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_116.json`
- JSON | tamaño: 6094 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_117.json`
- JSON | tamaño: 5922 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_118.json`
- JSON | tamaño: 5943 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_119.json`
- JSON | tamaño: 5701 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_12.json`
- JSON | tamaño: 2416 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_120.json`
- JSON | tamaño: 5653 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_121.json`
- JSON | tamaño: 6224 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_122.json`
- JSON | tamaño: 4502 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_123.json`
- JSON | tamaño: 5037 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_124.json`
- JSON | tamaño: 5182 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_125.json`
- JSON | tamaño: 5172 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_126.json`
- JSON | tamaño: 3884 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_127.json`
- JSON | tamaño: 4681 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_128.json`
- JSON | tamaño: 4150 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_129.json`
- JSON | tamaño: 1049 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_13.json`
- JSON — Tech: Requests (cliente HTTP) | tamaño: 5454 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_130.json`
- JSON | tamaño: 4589 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_131.json`
- JSON | tamaño: 4988 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_132.json`
- JSON | tamaño: 2910 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_133.json`
- JSON | tamaño: 1231 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_134.json`
- JSON | tamaño: 4296 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_135.json`
- JSON | tamaño: 4245 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_136.json`
- JSON | tamaño: 2260 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_137.json`
- JSON | tamaño: 2755 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_138.json`
- JSON | tamaño: 1162 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_139.json`
- JSON | tamaño: 2325 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_14.json`
- JSON — Tech: Requests (cliente HTTP) | tamaño: 2460 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_140.json`
- JSON | tamaño: 2144 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_141.json`
- JSON | tamaño: 1147 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_142.json`
- JSON | tamaño: 4719 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_143.json`
- JSON | tamaño: 2111 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_144.json`
- JSON | tamaño: 4239 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_145.json`
- JSON | tamaño: 3635 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_146.json`
- JSON | tamaño: 1187 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_147.json`
- JSON | tamaño: 1075 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_148.json`
- JSON | tamaño: 1128 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_149.json`
- JSON | tamaño: 1084 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_15.json`
- JSON | tamaño: 2343 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_150.json`
- JSON | tamaño: 4534 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_151.json`
- JSON | tamaño: 3286 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_152.json`
- JSON | tamaño: 4741 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_153.json`
- JSON | tamaño: 1243 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_154.json`
- JSON | tamaño: 1419 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_155.json`
- JSON | tamaño: 1467 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_156.json`
- JSON | tamaño: 1131 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_157.json`
- JSON | tamaño: 1201 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_158.json`
- JSON | tamaño: 1117 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_159.json`
- JSON | tamaño: 3747 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_16.json`
- JSON | tamaño: 2461 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_160.json`
- JSON | tamaño: 2139 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_161.json`
- JSON | tamaño: 1996 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_162.json`
- JSON | tamaño: 2484 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_163.json`
- JSON | tamaño: 2784 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_164.json`
- JSON | tamaño: 5107 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_165.json`
- JSON | tamaño: 4794 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_166.json`
- JSON | tamaño: 2904 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_167.json`
- JSON | tamaño: 4905 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_168.json`
- JSON | tamaño: 5805 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_169.json`
- JSON | tamaño: 5561 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_17.json`
- JSON | tamaño: 1324 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_170.json`
- JSON | tamaño: 4751 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_171.json`
- JSON | tamaño: 3479 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_172.json`
- JSON | tamaño: 4014 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_173.json`
- JSON | tamaño: 5166 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_174.json`
- JSON | tamaño: 3901 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_175.json`
- JSON — Tech: Requests (cliente HTTP) | tamaño: 3857 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_176.json`
- JSON | tamaño: 1171 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_177.json`
- JSON | tamaño: 1234 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_178.json`
- JSON | tamaño: 1207 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_179.json`
- JSON | tamaño: 1199 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_18.json`
- JSON | tamaño: 4373 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_180.json`
- JSON | tamaño: 3107 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_181.json`
- JSON | tamaño: 1174 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_182.json`
- JSON | tamaño: 3744 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_183.json`
- JSON | tamaño: 4242 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_184.json`
- JSON | tamaño: 4727 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_185.json`
- JSON | tamaño: 4291 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_186.json`
- JSON | tamaño: 4236 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_187.json`
- JSON | tamaño: 4200 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_188.json`
- JSON | tamaño: 4351 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_189.json`
- JSON | tamaño: 4070 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_19.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5753 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_190.json`
- JSON | tamaño: 3960 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_191.json`
- JSON | tamaño: 1048 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_192.json`
- JSON | tamaño: 2193 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_193.json`
- JSON | tamaño: 2048 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_194.json`
- JSON | tamaño: 2236 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_195.json`
- JSON | tamaño: 3407 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_196.json`
- JSON | tamaño: 2877 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_197.json`
- JSON | tamaño: 2471 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_198.json`
- JSON | tamaño: 2756 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_199.json`
- JSON | tamaño: 2466 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_2.json`
- JSON | tamaño: 1247 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_20.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5740 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_200.json`
- JSON | tamaño: 1044 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_201.json`
- JSON | tamaño: 133 bytes | LOC aprox: 8
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_202.json`
- JSON | tamaño: 1629 bytes | LOC aprox: 65
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_21.json`
- JSON | tamaño: 5382 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_22.json`
- JSON | tamaño: 5242 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_23.json`
- JSON | tamaño: 5913 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_24.json`
- JSON | tamaño: 4654 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_25.json`
- JSON | tamaño: 4965 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_26.json`
- JSON | tamaño: 5286 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_27.json`
- JSON | tamaño: 5916 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_28.json`
- JSON | tamaño: 3885 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_29.json`
- JSON | tamaño: 4226 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_3.json`
- JSON | tamaño: 3183 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_30.json`
- JSON | tamaño: 5202 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_31.json`
- JSON | tamaño: 5555 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_32.json`
- JSON | tamaño: 2438 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_33.json`
- JSON | tamaño: 4510 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_34.json`
- JSON | tamaño: 6301 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_35.json`
- JSON | tamaño: 6088 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_36.json`
- JSON | tamaño: 6235 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_37.json`
- JSON | tamaño: 6213 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_38.json`
- JSON | tamaño: 6062 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_39.json`
- JSON | tamaño: 5253 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_4.json`
- JSON | tamaño: 4645 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_40.json`
- JSON | tamaño: 4790 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_41.json`
- JSON | tamaño: 4630 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_42.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 4949 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_43.json`
- JSON | tamaño: 5391 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_44.json`
- JSON | tamaño: 2244 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_45.json`
- JSON | tamaño: 5806 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_46.json`
- JSON | tamaño: 6388 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_47.json`
- JSON | tamaño: 5583 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_48.json`
- JSON | tamaño: 6321 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_49.json`
- JSON | tamaño: 4130 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_5.json`
- JSON | tamaño: 5118 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_50.json`
- JSON | tamaño: 5016 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_51.json`
- JSON | tamaño: 6350 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_52.json`
- JSON | tamaño: 5737 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_53.json`
- JSON | tamaño: 5729 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_54.json`
- JSON | tamaño: 6092 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_55.json`
- JSON | tamaño: 6118 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_56.json`
- JSON | tamaño: 6097 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_57.json`
- JSON | tamaño: 4766 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_58.json`
- JSON | tamaño: 5264 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_59.json`
- JSON | tamaño: 5526 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_6.json`
- JSON | tamaño: 5591 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_60.json`
- JSON | tamaño: 4047 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_61.json`
- JSON | tamaño: 4573 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_62.json`
- JSON | tamaño: 5999 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_63.json`
- JSON | tamaño: 5445 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_64.json`
- JSON | tamaño: 5991 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_65.json`
- JSON | tamaño: 5803 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_66.json`
- JSON | tamaño: 6252 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_67.json`
- JSON | tamaño: 5856 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_68.json`
- JSON | tamaño: 4972 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_69.json`
- JSON | tamaño: 5920 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_7.json`
- JSON | tamaño: 3053 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_70.json`
- JSON | tamaño: 4923 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_71.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5792 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_72.json`
- JSON | tamaño: 6338 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_73.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5930 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_74.json`
- JSON | tamaño: 5913 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_75.json`
- JSON | tamaño: 6216 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_76.json`
- JSON | tamaño: 5695 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_77.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5866 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_78.json`
- JSON | tamaño: 6198 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_79.json`
- JSON | tamaño: 5945 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_8.json`
- JSON | tamaño: 5022 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_80.json`
- JSON | tamaño: 6262 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_81.json`
- JSON | tamaño: 6058 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_82.json`
- JSON | tamaño: 4175 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_83.json`
- JSON | tamaño: 4910 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_84.json`
- JSON | tamaño: 6216 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_85.json`
- JSON | tamaño: 6099 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_86.json`
- JSON | tamaño: 6050 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_87.json`
- JSON | tamaño: 6140 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_88.json`
- JSON | tamaño: 6020 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_89.json`
- JSON | tamaño: 5936 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_9.json`
- JSON | tamaño: 2992 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_90.json`
- JSON | tamaño: 6071 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_91.json`
- JSON | tamaño: 6198 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_92.json`
- JSON | tamaño: 6085 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_93.json`
- JSON — Tech: Redis (cache/colas) | tamaño: 5740 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_94.json`
- JSON | tamaño: 5918 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_95.json`
- JSON | tamaño: 6087 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_96.json`
- JSON | tamaño: 5014 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_97.json`
- JSON | tamaño: 5801 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_98.json`
- JSON | tamaño: 2215 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_pag_99.json`
- JSON | tamaño: 5426 bytes | LOC aprox: 43
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8 2007_Gas_Transmission/ASME B31.8 2007_Gas_Transmission_raw_data.json`
- JSON | tamaño: 885274 bytes | LOC aprox: 8675
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.8-2007_archivo_cortado_1.pdf`
- Archivo | tamaño: 73847 bytes

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.8-2007_archivo_cortado_1_pag_1.json`
- JSON | tamaño: 11045 bytes | LOC aprox: 210
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.8-2007_archivo_cortado_1_pag_2.json`
- JSON | tamaño: 13387 bytes | LOC aprox: 244
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.8-2007_archivo_cortado_1_pag_3.json`
- JSON | tamaño: 12414 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.8-2007_archivo_cortado_1_pag_4.json`
- JSON | tamaño: 12618 bytes | LOC aprox: 105
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31.txt`
- Text | tamaño: 16628 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
['Location Class', 'Design Factor, F'] ['Location Class 1, Division 1', '0.80'] ['Location Class 1, Division 2', '0.72'] ['Location Class 2', '0.60'] ['Location Class 3', '0.50'] ['Location Class 4', '0.40']
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31_resultado_paginas.json`
- JSON | tamaño: 50673 bytes | LOC aprox: 599
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/ASME B31.8-2007_archivo_cortado_1/ASME B31_tokens.txt`
- Text | tamaño: 92 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8.pdf`
- Archivo | tamaño: 828030 bytes

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_1.json`
- JSON | tamaño: 1533 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_10.json`
- JSON | tamaño: 5420 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_11.json`
- JSON | tamaño: 6002 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_12.json`
- JSON | tamaño: 3490 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_13.json`
- JSON | tamaño: 1584 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_14.json`
- JSON | tamaño: 6410 bytes | LOC aprox: 44
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_15.json`
- JSON | tamaño: 5928 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_16.json`
- JSON | tamaño: 4930 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_17.json`
- JSON | tamaño: 3766 bytes | LOC aprox: 58
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_18.json`
- JSON | tamaño: 5183 bytes | LOC aprox: 49
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_19.json`
- JSON | tamaño: 5214 bytes | LOC aprox: 109
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_2.json`
- JSON | tamaño: 1446 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_20.json`
- JSON | tamaño: 4328 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_21.json`
- JSON | tamaño: 5499 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_22.json`
- JSON | tamaño: 5777 bytes | LOC aprox: 140
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_23.json`
- JSON | tamaño: 6137 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_24.json`
- JSON | tamaño: 3978 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_25.json`
- JSON | tamaño: 5998 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_26.json`
- JSON | tamaño: 6585 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_27.json`
- JSON | tamaño: 5527 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_28.json`
- JSON | tamaño: 6976 bytes | LOC aprox: 78
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_29.json`
- JSON | tamaño: 5507 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_3.json`
- JSON | tamaño: 2697 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_30.json`
- JSON | tamaño: 4073 bytes | LOC aprox: 233
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_31.json`
- JSON | tamaño: 1735 bytes | LOC aprox: 91
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_32.json`
- JSON | tamaño: 3506 bytes | LOC aprox: 26
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_33.json`
- JSON | tamaño: 7357 bytes | LOC aprox: 108
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_34.json`
- JSON | tamaño: 6270 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_35.json`
- JSON | tamaño: 6820 bytes | LOC aprox: 68
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_36.json`
- JSON | tamaño: 6160 bytes | LOC aprox: 189
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_37.json`
- JSON | tamaño: 4617 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_38.json`
- JSON — Tech: Requests (cliente HTTP) | tamaño: 5176 bytes | LOC aprox: 59
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_39.json`
- JSON | tamaño: 5216 bytes | LOC aprox: 99
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_4.json`
- JSON | tamaño: 4446 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_40.json`
- JSON | tamaño: 5427 bytes | LOC aprox: 121
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_41.json`
- JSON | tamaño: 5757 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_42.json`
- JSON | tamaño: 5430 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_43.json`
- JSON | tamaño: 2856 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_44.json`
- JSON | tamaño: 5639 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_45.json`
- JSON | tamaño: 5245 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_46.json`
- JSON | tamaño: 3609 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_47.json`
- JSON | tamaño: 208 bytes | LOC aprox: 8
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_48.json`
- JSON | tamaño: 4989 bytes | LOC aprox: 58
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_49.json`
- JSON | tamaño: 2138 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_5.json`
- JSON | tamaño: 607 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_50.json`
- JSON | tamaño: 4984 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_51.json`
- JSON | tamaño: 2110 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_52.json`
- JSON | tamaño: 6451 bytes | LOC aprox: 88
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_53.json`
- JSON | tamaño: 587 bytes | LOC aprox: 21
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_54.json`
- JSON | tamaño: 5929 bytes | LOC aprox: 68
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_55.json`
- JSON | tamaño: 2156 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_56.json`
- JSON | tamaño: 4916 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_57.json`
- JSON | tamaño: 1830 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_58.json`
- JSON | tamaño: 6899 bytes | LOC aprox: 118
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_59.json`
- JSON | tamaño: 2110 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_6.json`
- JSON | tamaño: 2586 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_60.json`
- JSON | tamaño: 1882 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_61.json`
- JSON | tamaño: 4844 bytes | LOC aprox: 18
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_62.json`
- JSON | tamaño: 2220 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_63.json`
- JSON | tamaño: 6421 bytes | LOC aprox: 89
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_64.json`
- JSON | tamaño: 1280 bytes | LOC aprox: 28
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_65.json`
- JSON | tamaño: 4777 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_66.json`
- JSON | tamaño: 6518 bytes | LOC aprox: 65
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_67.json`
- JSON | tamaño: 5979 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_68.json`
- JSON | tamaño: 3580 bytes | LOC aprox: 38
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_69.json`
- JSON — Tech: Requests (cliente HTTP) | tamaño: 3796 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_7.json`
- JSON | tamaño: 3877 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_70.json`
- JSON | tamaño: 762 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_8.json`
- JSON | tamaño: 3532 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_pag_9.json`
- JSON | tamaño: 3058 bytes | LOC aprox: 159
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8/ASME B31.8S-2004 - Managing System Integrity of Gas Pipelines - Supplement to ASME B31.8_raw_data.json`
- JSON | tamaño: 307801 bytes | LOC aprox: 3656
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6).pdf`
- Archivo | tamaño: 547650 bytes

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6).txt`
- Text | tamaño: 11504 bytes | LOC aprox: 55
**Encabezado/comentario (snippet):**
```
1.1 Identificación adquirente.
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_pag_1.json`
- JSON | tamaño: 7929 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_pag_2.json`
- JSON | tamaño: 7468 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_pag_3.json`
- JSON | tamaño: 7671 bytes | LOC aprox: 47
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_pag_4.json`
- JSON | tamaño: 9814 bytes | LOC aprox: 78
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_resultado_paginas.json`
- JSON | tamaño: 33339 bytes | LOC aprox: 223
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Basesadministrativas (6)/Basesadministrativas (6)_tokens.txt`
- Text | tamaño: 92 bytes | LOC aprox: 4
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES.pdf`
- Archivo | tamaño: 333618 bytes

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES.txt`
- Text | tamaño: 3542 bytes | LOC aprox: 22
**Encabezado/comentario (snippet):**
```
ASEO Y ORNATO Huechuraba.
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES_pag_1.json`
- JSON | tamaño: 5180 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES_pag_2.json`
- JSON | tamaño: 5072 bytes | LOC aprox: 54
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES_resultado_paginas.json`
- JSON | tamaño: 10435 bytes | LOC aprox: 89
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/BASES_ADMINISTRATIVAS_ESPECIALES_tokens.txt`
- Text | tamaño: 46 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/BASES_ADMINISTRATIVAS_ESPECIALES/errores_embedding.log`
- Archivo | tamaño: 108 bytes

### `archivos_texto/CI-Javier/CI-Javier_pag_1.json`
- JSON | tamaño: 158 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/CI-Javier/CI-Javier_resultado.json`
- JSON | tamaño: 158 bytes | LOC aprox: 9
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/DOMINIO/DOMINIO.PDF`
- Archivo | tamaño: 407739 bytes

### `archivos_texto/DOMINIO/DOMINIO.txt`
- Text | tamaño: 2717 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
Calle Lanín N° 107, Comuna de Los Lagos Casilla 9-D, Los Lagos - CHILE Fono-Fax +56 63 2461434 E-mail: conservadorloslagos@gmail.com Web: http://www.cbrchile.cl
```

### `archivos_texto/DOMINIO/DOMINIO_pag_1.json`
- JSON | tamaño: 8283 bytes | LOC aprox: 108
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/DOMINIO/DOMINIO_pag_2.json`
- JSON | tamaño: 4371 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/DOMINIO/DOMINIO_resultado_paginas.json`
- JSON | tamaño: 12985 bytes | LOC aprox: 163
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/DOMINIO/DOMINIO_tokens.txt`
- Text | tamaño: 46 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ.pdf`
- Archivo | tamaño: 239346 bytes

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ.txt`
- Text | tamaño: 14580 bytes | LOC aprox: 115
**Encabezado/comentario (snippet):**
```
Santiago, 24 de abril del año 2025
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_1.json`
- JSON | tamaño: 5290 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_2.json`
- JSON | tamaño: 8389 bytes | LOC aprox: 73
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_3.json`
- JSON | tamaño: 5343 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_4.json`
- JSON | tamaño: 7719 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_5.json`
- JSON | tamaño: 4798 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_6.json`
- JSON | tamaño: 5281 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_7.json`
- JSON | tamaño: 7607 bytes | LOC aprox: 93
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_pag_8.json`
- JSON | tamaño: 2193 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_raw_data.json`
- JSON | tamaño: 22440 bytes | LOC aprox: 372
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_resultado_paginas.json`
- JSON | tamaño: 47485 bytes | LOC aprox: 421
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/informe de titulos GALLARDO JIMENEZ/informe de titulos GALLARDO JIMENEZ_tokens.txt`
- Text | tamaño: 184 bytes | LOC aprox: 8
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/errores_embedding.log`
- Archivo | tamaño: 290 bytes

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768.pdf`
- Archivo | tamaño: 71725 bytes

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768.txt`
- Text | tamaño: 2399 bytes | LOC aprox: 12
**Encabezado/comentario (snippet):**
```
['Sucursal', 'BANCA UNICA'] ['Numero Cuenta de Gastos', '02634237611'] ['Ejecutivo de Cuenta', 'EJECUTIVO BANCA UNICA'] ['Numero de Operacion', '500050717685'] ['Banco Acreedor', 'SIN BANCO ACREEDOR']
```

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_pag_1.json`
- JSON | tamaño: 10612 bytes | LOC aprox: 286
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_pag_2.json`
- JSON | tamaño: 2907 bytes | LOC aprox: 54
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_resultado_paginas.json`
- JSON | tamaño: 14208 bytes | LOC aprox: 342
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768/Liquidación Hipotecaria - JAVIER ANDRES GALLARDO JIMENEZ 00157375768_tokens.txt`
- Text | tamaño: 46 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/paginas_extraidas-licitacion-2-pag-con-tabla/paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json`
- JSON | tamaño: 5437 bytes | LOC aprox: 143
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-licitacion-2-pag-con-tabla/paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json`
- JSON | tamaño: 2678 bytes | LOC aprox: 70
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/paginas_extraidas-licitacion-2-pag-con-tabla/paginas_extraidas-licitacion-2-pag-con-tabla_resultado.json`
- JSON | tamaño: 8112 bytes | LOC aprox: 211
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_1.json`
- JSON | tamaño: 1536 bytes | LOC aprox: 16
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_2.json`
- JSON | tamaño: 2108 bytes | LOC aprox: 16
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_3.json`
- JSON | tamaño: 2199 bytes | LOC aprox: 16
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_4.json`
- JSON | tamaño: 1873 bytes | LOC aprox: 15
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_5.json`
- JSON | tamaño: 2124 bytes | LOC aprox: 15
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_6.json`
- JSON | tamaño: 2169 bytes | LOC aprox: 15
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_7.json`
- JSON | tamaño: 2087 bytes | LOC aprox: 16
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_8.json`
- JSON | tamaño: 824 bytes | LOC aprox: 15
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_page_9.json`
- JSON | tamaño: 353 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Promesa-CV-Javier/Promesa-CV-Javier_raw_data.json`
- JSON | tamaño: 15565 bytes | LOC aprox: 133
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_1.json`
- JSON | tamaño: 4687 bytes | LOC aprox: 47
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_2.json`
- JSON | tamaño: 9375 bytes | LOC aprox: 69
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_3.json`
- JSON | tamaño: 3063 bytes | LOC aprox: 111
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_pag_4.json`
- JSON | tamaño: 102 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_raw_data.json`
- JSON | tamaño: 17710 bytes | LOC aprox: 236
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/Reglamento N°280 Seguridad Transp. Dist. Gas Red/Reglamento N°280 Seguridad Transp. Dist. Gas Red_tokens.txt`
- Text | tamaño: 188 bytes | LOC aprox: 7
**Encabezado/comentario (snippet):**
```
Página 1: input=1425 output=1190
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/errores_embedding.log`
- Archivo | tamaño: 1200 bytes

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1).pdf`
- Archivo | tamaño: 8690205 bytes

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1).txt`
- Text | tamaño: 107574 bytes | LOC aprox: 620
**Encabezado/comentario (snippet):**
```
APRUEBA BASES ADMINISTRATIVAS, REQUERIMIENTOS TÉCNICOS Y ANEXOS DE LICITACIÓN PÚBLICA, Y DESIGNA COMISIÓN EVALUADORA PARA EL “SUMINISTRO DE CALEFONES, TERMOS ELÉCTRICOS E INSUMOS RELACIONADOS, PARA LOS INMUEBLES UBICADOS EN LA REGIÓN METROPOLITANA, ADMINISTRADO POR EL DEPARTAMENTO DE GESTIÓN INMOBILIARIA B.2, DE LA DIRECCIÓN DE BIENESTAR DE CARABINEROS”.
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_1.json`
- JSON | tamaño: 6797 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_10.json`
- JSON | tamaño: 9490 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_11.json`
- JSON | tamaño: 8085 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_12.json`
- JSON | tamaño: 9010 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_13.json`
- JSON | tamaño: 7478 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_14.json`
- JSON | tamaño: 7888 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_15.json`
- JSON | tamaño: 8365 bytes | LOC aprox: 111
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_16.json`
- JSON | tamaño: 7048 bytes | LOC aprox: 52
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_17.json`
- JSON | tamaño: 8720 bytes | LOC aprox: 89
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_18.json`
- JSON | tamaño: 3622 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_19.json`
- JSON | tamaño: 8575 bytes | LOC aprox: 113
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_2.json`
- JSON | tamaño: 7664 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_20.json`
- JSON | tamaño: 7674 bytes | LOC aprox: 106
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_21.json`
- JSON | tamaño: 3508 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_22.json`
- JSON | tamaño: 7247 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_23.json`
- JSON | tamaño: 4855 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_24.json`
- JSON | tamaño: 5612 bytes | LOC aprox: 133
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_25.json`
- JSON | tamaño: 8510 bytes | LOC aprox: 252
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_26.json`
- JSON | tamaño: 4250 bytes | LOC aprox: 67
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_27.json`
- JSON | tamaño: 3370 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_28.json`
- JSON | tamaño: 2919 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_29.json`
- JSON | tamaño: 4433 bytes | LOC aprox: 58
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_3.json`
- JSON | tamaño: 6853 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_30.json`
- JSON | tamaño: 4866 bytes | LOC aprox: 68
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_31.json`
- JSON | tamaño: 4666 bytes | LOC aprox: 68
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_32.json`
- JSON | tamaño: 3985 bytes | LOC aprox: 58
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_33.json`
- JSON | tamaño: 5162 bytes | LOC aprox: 73
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_34.json`
- JSON | tamaño: 4544 bytes | LOC aprox: 73
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_35.json`
- JSON | tamaño: 5704 bytes | LOC aprox: 93
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_36.json`
- JSON | tamaño: 6283 bytes | LOC aprox: 68
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_37.json`
- JSON | tamaño: 6231 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_38.json`
- JSON | tamaño: 7334 bytes | LOC aprox: 32
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_39.json`
- JSON | tamaño: 8126 bytes | LOC aprox: 45
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_4.json`
- JSON | tamaño: 7452 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_40.json`
- JSON | tamaño: 7492 bytes | LOC aprox: 32
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_41.json`
- JSON | tamaño: 4202 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_42.json`
- JSON | tamaño: 4726 bytes | LOC aprox: 105
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_43.json`
- JSON | tamaño: 3683 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_44.json`
- JSON | tamaño: 10578 bytes | LOC aprox: 103
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_45.json`
- JSON | tamaño: 7322 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_46.json`
- JSON | tamaño: 8036 bytes | LOC aprox: 53
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_47.json`
- JSON | tamaño: 7897 bytes | LOC aprox: 48
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_48.json`
- JSON | tamaño: 7223 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_49.json`
- JSON | tamaño: 8694 bytes | LOC aprox: 101
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_5.json`
- JSON | tamaño: 7271 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_50.json`
- JSON | tamaño: 4677 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_6.json`
- JSON | tamaño: 7643 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_7.json`
- JSON | tamaño: 8919 bytes | LOC aprox: 63
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_8.json`
- JSON | tamaño: 8386 bytes | LOC aprox: 33
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_pag_9.json`
- JSON | tamaño: 10264 bytes | LOC aprox: 73
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_resultado_paginas.json`
- JSON | tamaño: 339750 bytes | LOC aprox: 3131
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)/RESOLUCIÓN_EXENTA_N°188_APRUEBA_BASES (1)_tokens.txt`
- Text | tamaño: 1191 bytes | LOC aprox: 50
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/errores_embedding.log`
- Archivo | tamaño: 246 bytes

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla.pdf`
- Archivo | tamaño: 336121 bytes

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla.txt`
- Text | tamaño: 4213 bytes | LOC aprox: 35
**Encabezado/comentario (snippet):**
```
Además, declara(n) que el oferente ha leído íntegramente las bases de licitación, las ha entendido y se somete a ellas. La presente declaración se entenderá aceptada con la sola presentación de la propuesta.
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_1.json`
- JSON | tamaño: 9282 bytes | LOC aprox: 116
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla_pag_2.json`
- JSON | tamaño: 5533 bytes | LOC aprox: 75
**Encabezado/comentario (snippet):**
```
{
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla_raw_data.json`
- JSON | tamaño: 6947 bytes | LOC aprox: 167
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla_resultado_paginas.json`
- JSON | tamaño: 15206 bytes | LOC aprox: 193
**Encabezado/comentario (snippet):**
```
[
```

### `archivos_texto/v3-paginas_extraidas-licitacion-2-pag-con-tabla/v3-paginas_extraidas-licitacion-2-pag-con-tabla_tokens.txt`
- Text | tamaño: 46 bytes | LOC aprox: 2
**Encabezado/comentario (snippet):**
```
Página 1: N/A tokens
```

### `Imagenes Ejemplo Convolucion/pag2.jpg`
- Archivo | tamaño: 246409 bytes

### `Imagenes Ejemplo Convolucion/salida_convolucion.png`
- Archivo | tamaño: 367068 bytes

### `Imagenes Ejemplo Convolucion/salida_gris.png`
- Archivo | tamaño: 381364 bytes

### `routes/chat.py`
- Python — Tech: Flask (API web), Redis (cache/colas) | tamaño: 3669 bytes | LOC aprox: 102
- Funciones: chat_page, api_docs, api_chat

### `routes/chat_embedding.py`
- Python — Tech: Flask (API web), Redis (cache/colas) | tamaño: 2879 bytes | LOC aprox: 75
- Funciones: obtener_docs_detalle, page, api_doc_raw, api_chat_embedding

### `routes/extraction.py`
- Python — Tech: Flask (API web) | tamaño: 2262 bytes | LOC aprox: 58
- Funciones: mostrar_formulario_extraccion, extraer_documento

### `routes/__init__.py`
- Python | tamaño: 0 bytes

### `Scripts/activate`
- Archivo | tamaño: 2258 bytes

### `Scripts/activate.bat`
- Batch | tamaño: 1057 bytes | LOC aprox: 34
**Encabezado/comentario (snippet):**
```
@echo off
```

### `Scripts/Activate.ps1`
- PowerShell | tamaño: 27975 bytes | LOC aprox: 528
**Encabezado/comentario (snippet):**
```
<#
```

### `Scripts/deactivate.bat`
- Batch | tamaño: 393 bytes | LOC aprox: 22
**Encabezado/comentario (snippet):**
```
@echo off
```

### `Scripts/distro.exe`
- Archivo | tamaño: 108415 bytes

### `Scripts/dotenv.exe`
- Archivo | tamaño: 108415 bytes

### `Scripts/dumppdf.py`
- Python | tamaño: 14382 bytes | LOC aprox: 480

### `Scripts/f2py.exe`
- Archivo | tamaño: 108419 bytes

### `Scripts/flask.exe`
- Archivo | tamaño: 108411 bytes

### `Scripts/fonttools.exe`
- Archivo | tamaño: 108420 bytes

### `Scripts/httpx.exe`
- Archivo | tamaño: 108407 bytes

### `Scripts/normalizer.exe`
- Archivo | tamaño: 108429 bytes

### `Scripts/numpy-config.exe`
- Archivo | tamaño: 108419 bytes

### `Scripts/openai.exe`
- Archivo | tamaño: 108412 bytes

### `Scripts/pdf2txt.py`
- Python | tamaño: 9893 bytes | LOC aprox: 323

### `Scripts/pdfplumber.exe`
- Archivo | tamaño: 108416 bytes

### `Scripts/pip.exe`
- Archivo | tamaño: 108424 bytes

### `Scripts/pip3.12.exe`
- Archivo | tamaño: 108424 bytes

### `Scripts/pip3.exe`
- Archivo | tamaño: 108424 bytes

### `Scripts/pyftmerge.exe`
- Archivo | tamaño: 108417 bytes

### `Scripts/pyftsubset.exe`
- Archivo | tamaño: 108418 bytes

### `Scripts/pymupdf.exe`
- Archivo | tamaño: 108418 bytes

### `Scripts/pypdfium2.exe`
- Archivo | tamaño: 108428 bytes

### `Scripts/pytesseract.exe`
- Archivo | tamaño: 108425 bytes

### `Scripts/python.exe`
- Archivo | tamaño: 274424 bytes

### `Scripts/pythonw.exe`
- Archivo | tamaño: 263400 bytes

### `Scripts/tqdm.exe`
- Archivo | tamaño: 108410 bytes

### `Scripts/ttx.exe`
- Archivo | tamaño: 108415 bytes

### `services/chat_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 7274 bytes | LOC aprox: 155

### `services/embedding_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 7165 bytes | LOC aprox: 185

### `services/pdf_service.py`
- Python — Servicios/Lógica de negocio — Tech: Redis (cache/colas) | tamaño: 5782 bytes | LOC aprox: 132
- Funciones: process_pdf, registrar_error_reproceso

### `services/__init__.py`
- Python | tamaño: 0 bytes

### `share/man/man1/ttx.1`
- Archivo | tamaño: 5601 bytes

### `static/css/style.css`
- CSS — Archivos estáticos (CSS/JS/Imágenes) | tamaño: 5389 bytes | LOC aprox: 264
**Encabezado/comentario (snippet):**
```
:root {
/* Navegación principal y secundaria */
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

### `templates/extraccion.html`
- HTML — Templates HTML | tamaño: 2399 bytes | LOC aprox: 74
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
```

### `templates/home.html`
- HTML — Templates HTML | tamaño: 705 bytes | LOC aprox: 22
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
    <!-- Podrías poner aquí un banner o instrucciones generales -->
```

### `templates/listado.html`
- HTML — Templates HTML | tamaño: 350 bytes | LOC aprox: 13
**Encabezado/comentario (snippet):**
```
<!DOCTYPE html>
  <!-- Lista de documentos disponibles -->
```

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
- Python — Utilidades — Tech: Redis (cache/colas) | tamaño: 3268 bytes | LOC aprox: 102
- Funciones: guardar_en_redis, leer_hash
