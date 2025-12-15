# pdf_selectable.py
import pdfplumber

def analyze_page_selectable(pdf_path: str, page_number: int) -> tuple[list[dict], str, int, float]:
    print(f"[analyze_page_selectable] → Abriendo PDF: {pdf_path}, página: {page_number+1}")
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        texto = page.extract_text() or ""
        tablas = page.extract_tables() or []
        longitud_texto = len(texto)
        print(f"[analyze_page_selectable] → Texto extraído ({longitud_texto} caracteres)")

        elementos = []
        orden = 1
        titulo = texto.strip().split('\n')[0] if texto.strip() else ""

        if texto:
            elementos.append({
                "id": f"p{page_number+1}_e{orden}",
                "tipo": "texto",
                "posicion": orden,
                "titulo": "",
                "descripcion": "",
                "contenido": texto.strip(),
                "coordenadas": {},
                "metadatos": { "longitud": longitud_texto }
            })
            orden += 1

        for tabla in tablas:
            elementos.append({
                "id": f"p{page_number+1}_e{orden}",
                "tipo": "tabla",
                "posicion": orden,
                "titulo": "",
                "descripcion": "",
                "contenido": tabla,
                "coordenadas": {},
                "metadatos": { "filas": len(tabla) }
            })
            orden += 1

        print(f"[analyze_page_selectable] ✔ Página procesada con {len(elementos)} elementos")
        return elementos, texto, longitud_texto, 1.0
