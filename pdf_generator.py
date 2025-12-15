from fpdf import FPDF
import json
import unicodedata


def build_pdf_from_json(json_path: str, output_path: str):
    with open(json_path, 'r', encoding='utf-8') as f:
        pages = json.load(f)

    pdf = FPDF()
    pdf.set_margins(10, 10, 10)
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font("Helvetica", size=12)
    width = pdf.w - pdf.l_margin - pdf.r_margin

    for page in pages:
        pdf.add_page()
        title = f"Página {page['pagina']}"
        safe_title = unicodedata.normalize('NFKD', title).encode('latin-1', 'ignore').decode('latin-1')
        pdf.cell(0, 10, safe_title, ln=True)
        for elem in page.get('elementos', []):
            txt = elem.get('contenido', '')
            safe_txt = unicodedata.normalize('NFKD', txt).encode('latin-1', 'ignore').decode('latin-1')
            pdf.multi_cell(width, 8, safe_txt)
        pdf.ln(5)

    pdf.output(output_path)