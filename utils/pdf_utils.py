# utils/pdf_utils.py
import fitz  # PyMuPDF
import os

def extraer_paginas_pdf(pdf_path, paginas, carpeta_salida):
    """
    Extrae páginas específicas desde un PDF y las guarda como archivos individuales.
    :param pdf_path: Ruta del PDF original
    :param paginas: Lista de números de página (empezando en 1)
    :param carpeta_salida: Carpeta donde guardar las páginas extraídas
    :return: Lista de rutas de archivos PDF extraídos
    """
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    pdf = fitz.open(pdf_path)
    archivos_extraidos = []

    for i in paginas:
        indice = i - 1
        if 0 <= indice < len(pdf):
            nuevo_doc = fitz.open()
            nuevo_doc.insert_pdf(pdf, from_page=indice, to_page=indice)
            output_path = os.path.join(carpeta_salida, f"pagina_{i}.pdf")
            nuevo_doc.save(output_path)
            nuevo_doc.close()
            archivos_extraidos.append(output_path)
        else:
            print(f"[pdf_utils] ⚠️ Página {i} fuera de rango en el archivo")

    pdf.close()
    return archivos_extraidos
