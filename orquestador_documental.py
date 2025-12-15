import json
import openai
from config import API_KEY

# Cliente OpenAI para orquestación
client = openai.OpenAI(api_key=API_KEY)


def classify_document(json_path: str) -> str:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = f.read()

    system_msg = (
        "Eres un agente orquestador experto en clasificación documental.\n"
        "Considera procesos de licitación, contratos hipotecarios (incluye compra-venta), y créditos de consumo.\n"
        "Si detectas una compraventa de propiedad con financiamiento, clasifícala como 'hipotecario'.\n"
        "Responde solo con la clave de la categoría."
    )

    prompt = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": data}
    ]

    resp = client.chat.completions.create(model="gpt-4o-mini", messages=prompt, temperature=0)
    doc_type = resp.choices[0].message.content.strip().lower()
    print(f"[Orquestador] Tipo detectado: {doc_type}")
    return doc_type