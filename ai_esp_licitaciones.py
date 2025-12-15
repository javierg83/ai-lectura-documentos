import re
import json
import openai
from config import API_KEY

client = openai.OpenAI(api_key=API_KEY)

def handle_licitaciones(json_path: str) -> dict:
    """
    Lee el JSON extraído, envía a GPT para extraer datos clave y resumen.
    Limpia fences Markdown y maneja errores de JSON.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = f.read()

    prompt = [
        {
            "role": "system",
            "content": (
                "Eres un experto en licitaciones: extrae datos clave del documento tales como:"
                "el nombre de la empresa, rut, monto licitacion, lugar de entrega y otros que existan dentro del documento."
                "Con estos datos presenta un resumen tabulado en JSON con las claves 'resumen' y 'datos'."
            )
        },
        {"role": "user", "content": data}
    ]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
        temperature=0
    )
    raw = resp.choices[0].message.content.strip()
    print(f"[Licitaciones] RAW response:\n{raw}\n")

    # Limpiar posibles fences ```json ... ```
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```$", "", raw, flags=re.MULTILINE)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        print(f"[Licitaciones] Error parsing JSON, retorno raw para diagnóstico.")
        return {"resumen": None, "datos": None, "raw": raw}

    print(f"[Licitaciones] Resumen: {result.get('resumen')}")
    return result
