from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path


def seleccion_paginas_extraccion(archivoEntrada):
    # === CONFIGURACIÓN (reusando tu código base) ===

    ARCHIVO_PDF = r"C:\Desarrollo\IA\Proyectos\ai-lectura-documentos\archivos\licitacion-imagenes.pdf"
    LEER_TODO_EL_DOCUMENTO = False
    PAGINAS_A_ANALIZAR = [48, 49]  # Índice basado en 0 (página 1 = 0)

    # === CONFIGURACIÓN DE SALIDA ===

    ARCHIVO_SALIDA = Path(ARCHIVO_PDF).with_name("paginas_extraidas.pdf")

    # === PROCESAMIENTO ===

    reader = PdfReader(ARCHIVO_PDF)
    writer = PdfWriter()

    total_paginas = len(reader.pages)
    print(f"[INFO] El documento tiene {total_paginas} páginas.")

    # Determinar qué páginas extraer
    paginas = list(range(total_paginas)) if LEER_TODO_EL_DOCUMENTO else PAGINAS_A_ANALIZAR

    for pagina in paginas:
        if 0 <= pagina < total_paginas:
            writer.add_page(reader.pages[pagina])
            print(f"[OK] Página {pagina + 1} agregada.")
        else:
            print(f"[WARNING] Página {pagina + 1} fuera de rango.")

    # Guardar nuevo archivo
    with open(ARCHIVO_SALIDA, "wb") as f:
        writer.write(f)

    print(f"\n📦 Archivo generado en: {ARCHIVO_SALIDA}")

    return ARCHIVO_SALIDA
