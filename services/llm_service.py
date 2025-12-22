# services/llm_service.py
"""
Servicio LLM directo (sin chat, sin usuario, sin embeddings).
Usado por extractores semánticos y procesos batch.
"""

from openai import OpenAI
import config


# ==========================================================
# OPENAI CLIENT (MISMO PATRÓN QUE chat_service.py)
# ==========================================================
oai = OpenAI(api_key=config.API_KEY)


def run_llm_raw(prompt: str) -> str:
    """
    Ejecuta una llamada directa al LLM usando un prompt ya construido.
    Devuelve SOLO texto.
    """
    print("[llm_service] 🧠 Iniciando llamada LLM (modo batch)")
    print(f"[llm_service] 📏 Largo del prompt: {len(prompt)} caracteres")

    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "Eres un asistente experto en análisis de documentos públicos, "
                    "legales y técnicos. Tu tarea es extraer información estructurada "
                    "de forma precisa, sin inventar datos."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        print("[llm_service] 🚀 Enviando solicitud al modelo GPT...")
        resp = oai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0
        )

        reply = resp.choices[0].message.content
        token_in = resp.usage.prompt_tokens
        token_out = resp.usage.completion_tokens

        print("[llm_service] ✅ Respuesta LLM recibida correctamente")
        print(f"[llm_service] 📊 Tokens usados → input: {token_in}, output: {token_out}")
        print("[llm_service] 📝 Respuesta del modelo (primeros 500 chars):")
        print(reply[:500] + ("..." if len(reply) > 500 else ""))

        return reply.strip()

    except Exception as e:
        print(f"[llm_service] ❌ Error al llamar al LLM: {e}")
        raise
