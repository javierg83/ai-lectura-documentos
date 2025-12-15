# processor.py
import fitz  # PyMuPDF
import base64
import json
import os
from ai_extractor_pdf import analyze_page_with_gpt as analizar_pagina
from embeddings import generar_embedding
from utils.redis_utils import guardar_en_redis

def convertir_pagina_a_base64(pdf_path, page_number):
    with fitz.open(pdf_path) as doc:
        page = doc.load_page(page_number)
        pix = page.get_pixmap(dpi=200)
        return base64.b64encode(pix.tobytes()).decode("utf-8")

def process_pages(pdf_path, carpeta_destino, paginas_especificas, read_all, doc_id):
    resultados = []
    with fitz.open(pdf_path) as doc:
        total_paginas = doc.page_count

        indices = list(range(total_paginas)) if read_all else [i - 1 for i in paginas_especificas]
        print(f"[process_pages] → PDF tiene {total_paginas} páginas. Leyendo indices: {indices}")

        for i in indices:
            print(f"=== process_pages → Procesando {i + 1}/{total_paginas} (página real {i + 1}) ===")

            try:
                print(f"[Extractor] ({i + 1}) → Iniciando análisis de página {i + 1} de '{pdf_path}'")
                elementos, raw, tokens_in, tokens_out = analizar_pagina(pdf_path, i)

                resultado = {
                    "pagina": i + 1,
                    "elementos": elementos,
                    "tokens_in": tokens_in,
                    "tokens_out": tokens_out,
                    "raw": raw
                }
                resultados.append(resultado)

                for idx, elem in enumerate(elementos):
                    texto = str(elem.get("contenido", "")).strip()
                    if texto:
                        emb = generar_embedding(texto)
                        if emb:
                            clave = f"doc_raw_page:{doc_id}:p{i+1}_e{idx+1}"
                            guardar_en_redis(clave, {
                                "embedding": json.dumps(emb),
                                "texto": texto,
                                "pagina": i + 1,
                                "tipo": elem.get("tipo", "")
                            })

                texto_pagina = "\n".join(
                    str(e.get("contenido", "")) for e in elementos if isinstance(e.get("contenido", ""), str)
                )
                if texto_pagina.strip():
                    emb_pagina = generar_embedding(texto_pagina.strip())
                    if emb_pagina:
                        clave = f"doc_raw_page:{doc_id}:p{i+1}_full"
                        guardar_en_redis(clave, {
                            "embedding": json.dumps(emb_pagina),
                            "texto": texto_pagina.strip(),
                            "pagina": i + 1,
                            "tipo": "pagina"
                        })
            except Exception as e:
                print(f"[❌ ERROR] No se pudo procesar página {i + 1}: {e}")

    print("[process_pages] ✅ Finalizado.")
    return resultados

def guardar_resultados(resultados, carpeta_destino, nombre_base="documento"):
    json_path = os.path.join(carpeta_destino, f"{nombre_base}_resultado_paginas.json")
    txt_path = os.path.join(carpeta_destino, f"{nombre_base}.txt")
    token_path = os.path.join(carpeta_destino, f"{nombre_base}_tokens.txt")

    with open(json_path, "w", encoding="utf-8") as f_json, \
         open(txt_path, "w", encoding="utf-8") as f_txt, \
         open(token_path, "w", encoding="utf-8") as f_tok:

        total_tokens = 0
        for pagina in resultados:
            num_pagina = pagina["pagina"]
            elementos = pagina.get("elementos", [])

            f_txt.write(f"=== PÁGINA {num_pagina} ===\n")
            for elem in elementos:
                t = elem.get("tipo")
                if t == "titulo":
                    f_txt.write(f"\n# {elem.get('contenido', '').strip()}\n")
                elif t == "texto":
                    f_txt.write(elem.get("contenido", "").strip() + "\n")
                elif t == "checkbox":
                    f_txt.write("☑️ " + elem.get("contenido", "").strip() + "\n")
                elif t == "tabla":
                    contenido = elem.get("contenido", [])
                    if isinstance(contenido, list):
                        for row in contenido:
                            if isinstance(row, list):
                                f_txt.write("|".join(str(c) for c in row) + "\n")
                            else:
                                f_txt.write(str(row) + "\n")
                    else:
                        f_txt.write(str(contenido) + "\n")

                tokens = elem.get("tokens", 0)
                total_tokens += tokens

            f_txt.write("\n\n")

        f_tok.write(f"Total tokens: {total_tokens}\n")

    print(f"[guardar_archivos] → Guardando JSON en {os.path.basename(json_path)}")
    print(f"[guardar_archivos] → Guardando texto plano en {os.path.basename(txt_path)}")
    print(f"[guardar_archivos] → Guardando tokens en {os.path.basename(token_path)}")
    print("[guardar_archivos] ✅ Archivos guardados correctamente")
