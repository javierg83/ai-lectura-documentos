# routes/extraction.py
from flask import Blueprint, request, jsonify, render_template
from services.pdf_service import process_pdf
import os

extraction_bp = Blueprint('extraction', __name__)

# ✅ Vista para mostrar la página HTML de extracción
@extraction_bp.route("/extraccion", methods=["GET"])
def mostrar_formulario_extraccion():
    return render_template("extraccion.html")

# ✅ Endpoint para subir y procesar el archivo
@extraction_bp.route("/api/extraccion", methods=["POST"])
def extraer_documento():
    archivo = request.files.get("archivo")
    if not archivo:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    tipo_extraccion = request.form.get("tipo_extraccion", "ia")
    read_all = request.form.get("read_all", "true").lower() == "true"
    paginas = request.form.get("paginas", "")
    lista_paginas = [int(p.strip()) for p in paginas.split(",") if p.strip().isdigit()] if paginas else []

    nombre_archivo = archivo.filename
    doc_id = os.path.splitext(nombre_archivo)[0]
    ruta_carpeta = os.path.join("archivos_texto", doc_id)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    ruta_pdf = os.path.join(ruta_carpeta, nombre_archivo)
    archivo.save(ruta_pdf)

    print(f"[pdf_service] → Archivo recibido: {nombre_archivo}")
    print(f"[pdf_service] → PDF guardado en: {ruta_pdf}")
    print(f"[pdf_service] → Parámetros: read_all={read_all}, páginas específicas={lista_paginas}")
    print(f"[pdf_service] → Tipo de extracción seleccionado: {tipo_extraccion}")

    try:
        total_paginas = process_pdf(
            ruta_pdf,
            carpeta_destino=ruta_carpeta,
            tipo_extraccion=tipo_extraccion,
            read_all=read_all,
            paginas=lista_paginas
        )
    except Exception as e:
        print(f"[❌ ERROR] Error durante el procesamiento del PDF: {e}")
        return jsonify({"error": "Error procesando el documento"}), 500

    print(f"[process_pdf] ✔ Extracción finalizada, total páginas: {total_paginas}")

    return jsonify({
        "mensaje": "Extracción completada",
        "archivo": nombre_archivo,
        "total_paginas": total_paginas
    })
