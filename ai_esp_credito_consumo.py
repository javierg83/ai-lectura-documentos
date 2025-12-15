import json
import openai
from config import API_KEY

client = openai.OpenAI(api_key=API_KEY)


def handle_credito_consumo(json_path: str) -> dict:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = f.read()
    prompt = [
        {"role": "system", "content": "Eres especialista en crédito consumo: extrae tasa, cuotas y obligaciones."},
        {"role": "user", "content": data}
    ]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
        temperature=0
    )
    result = json.loads(resp.choices[0].message.content.strip())
    print(f"[Crédito Consumo] Resumen: {result.get('resumen')}")
    return result