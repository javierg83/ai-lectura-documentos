# ai_extractor_pdf.py

import re
import base64
import json
import time
from datetime import datetime
import openai
from config import API_KEY
from pdf_utils import extract_page_image
from tiktoken import encoding_for_model, get_encoding
from image_filters import enhance_image_contrast  # NUEVO: mejora binarización imagen

# Cliente OpenAI con visión habilitada
client = openai.OpenAI(api_key=API_KEY)

# Contador global de llamadas (para debug)
_request_count = 0

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    try:
        enc = encoding_for_model(model)
    except Exception:
        enc = get_encoding("cl100k_base")
    return len(enc.encode(text))

def analyze_page_with_gpt(pdf_path: str, page_number: int, timeout: float = 60.0, enhance_contrast: bool = True):
    """
    Envía la página como imagen a GPT-4o y limpia fences Markdown.
    Retorna: elementos (lista), raw (JSON limpio), tokens_in, tokens_out.
    """
    global _request_count
    _request_count += 1

    print(f"\n[Extractor] ({_request_count}) → {datetime.now():%H:%M:%S} "
          f"Iniciando análisis de página {page_number+1} de '{pdf_path}'")

    # 1) Extraer imagen original
    img_bytes = extract_page_image(pdf_path, page_number)
    print(f"[Extractor]   • Imagen original obtenida (bytes={len(img_bytes)})")

    # 2) Mejorar contraste visual (binarización)
    if enhance_contrast:
        img_bytes = enhance_image_contrast(img_bytes)
        print(f"[Extractor]   • Mejora de contraste aplicada (binarización adaptativa)")
    else:
        print(f"[Extractor]   • Mejora de contraste DESACTIVADA")

    # 3) Codificar a Base64
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    print(f"[Extractor]   • Imagen convertida a base64 (largo={len(img_b64)} caracteres)")

    # 4) Construir prompt
    system_msg = (
        '''
        Eres un asistente experto en analizar páginas de documentos PDF escaneados.

        Tu objetivo es:
        1. Detectar un posible título de página (texto destacado o encabezado en la parte superior) y retornarlo en el campo "titulo_pagina" (vacío si no existe).
        2. Identificar todos los elementos en orden: texto, tabla, tabla_checkbox, gráfico, esquema, imagen, logo o firma.
        3. Para cada 'tabla_checkbox', verificar que cada casilla haya sido correctamente leída y su estado marcado (true) o desmarcado (false), sin omitir ninguna casilla.
        4. Si encuentras imágenes, logos o firmas, además de categorizarlas, debes añadir un campo **"coordenadas"** con un objeto `{ "x": <valor>, "y": <valor>, "width": <valor>, "height": <valor> }` que indique su posición y tamaño en puntos (o la unidad que prefieras).
        5. Calcular un valor de **"confianza"** (float entre 0.0 y 1.0) que refleje cuán seguro estás de la exactitud de la extracción.
        6. Si detectas que una tabla continúa desde la página anterior (por ejemplo, aparece texto estructurado como filas, pero sin encabezado de tabla), intenta reconstruir la tabla usando el encabezado anterior, y considera todos los elementos como parte de la misma tabla.
            - Mantén la consistencia de columnas aunque no se repita el encabezado.
            - Si el contenido parece tabla pero no tiene bordes visibles, analízalo igualmente como una tabla visual.
            - Puedes agregar un campo "continuacion_tabla": true si es una tabla que se extiende desde otra página.
        
        La salida debe ser un JSON con estas claves de nivel raíz:
        - titulo_pagina: texto del título detectado o cadena vacía.
        - confianza: puntuación de confianza de la extracción.
        - elementos: lista de objetos con campos:
            * id: identificador único (ej. 'p1_e1').
            * tipo: uno de 'texto','tabla','tabla_checkbox','grafico','esquema','imagen','logo','firma'.
            * posicion: ordinal en la página (1,2,…).
            * titulo: título o reseña del elemento si existe, sino cadena vacía.
            * descripcion: caption breve o contexto si existe, sino cadena vacía.
            * contenido:
                - 'texto': texto plano.
                - 'tabla': lista de filas (cada fila es lista de celdas).
                - 'tabla_checkbox': lista de objetos `{ "valor": <texto>, "checked": true|false }`.
                - 'grafico','esquema': cadena vacía.
                - 'imagen','logo','firma': cadena vacía.
            * coordenadas: objeto `{ "x":…, "y":…, "width":…, "height":… }` solo para tipos 'imagen','logo','firma'; para otros deja `{}`.
            * metadatos: objeto opcional con información adicional (por ejemplo, dimensiones exactas, notas).
        '''
    )

    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": [
            {"type": "text", "text": f"Página {page_number+1}: analiza esta imagen."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}}
        ]}
    ]
    print(f"[Extractor]   • Prompt armado, mensajes={len(messages)} entradas")

    # 5) Llamada al modelo
    try:
        t0 = time.time()
        print(f"[Extractor]   • {datetime.now():%H:%M:%S} Antes de OpenAI request")
        resp = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
            timeout=timeout
        )
        dt = time.time() - t0
        print(f"[Extractor]   • {datetime.now():%H:%M:%S} Después de OpenAI ({dt:.1f}s)")
    except Exception as e:
        print(f"[Extractor]   ✖ Error o Timeout en llamada #{_request_count}: {e}")
        return [], "{}", 0, 0

    # 6) Procesar respuesta
    raw = resp.choices[0].message.content.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```$", "", raw, flags=re.MULTILINE)

    try:
        data = json.loads(raw)
        elementos = data.get('elementos', [])
        print(f"[Extractor]   ✅ JSON parseado OK: elementos detectados = {len(elementos)}")

        if not elementos:
            print(f"[Extractor]   ⚠️  Advertencia: respuesta vacía en página {page_number+1}")
        else:
            tipos = set(el.get("tipo", "¿?") for el in elementos)
            print(f"[Extractor]   🔍 Tipos encontrados: {sorted(tipos)}")
    except json.JSONDecodeError:
        print(f"[Extractor]   ✖ JSON inválido página {page_number+1}. Fragmento: {raw[:200].replace(chr(10), ' ')}…")
        elementos = []

    # 7) Tokens
    usage = getattr(resp, 'usage', None)
    tokens_in  = usage.prompt_tokens    if usage else count_tokens(json.dumps(messages))
    tokens_out = usage.completion_tokens if usage else count_tokens(raw)
    print(f"[Extractor]   • Tokens → in={tokens_in}, out={tokens_out}")

    return elementos, raw, tokens_in, tokens_out
