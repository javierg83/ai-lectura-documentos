from openai import OpenAI
import config
import json
from datetime import datetime
import os

# ==========================================================
# OPENAI CLIENT
# ==========================================================
oai = OpenAI(api_key=config.API_KEY)


def _guardar_llm_raw_json(raw_text: str, tag: str = "llm_response"):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"debug_llm_raw_{tag}_{ts}.json"

    try:
        parsed = json.loads(raw_text)
        contenido = parsed
    except Exception:
        contenido = {"raw_text": raw_text}

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contenido, f, indent=2, ensure_ascii=False)

    print(f"[🧪 DEBUG] Respuesta LLM cruda guardada en: {filename}")


def run_llm_raw(prompt: str) -> str:
    """
    Ejecuta una llamada directa al LLM y devuelve solo el texto plano.
    """
    print("[llm_service] 🧠 Iniciando llamada LLM (modo batch)")
    print(f"[llm_service] 📏 Largo del prompt: {len(prompt)} caracteres")

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

    _guardar_llm_raw_json(reply, tag="items_licitacion")

    return reply.strip()


def run_llm_raw_with_tokens(prompt: str, modelo: str = "gpt-4o") -> dict:
    """
    Llama al modelo indicado y retorna respuesta + tokens.
    """
    print(f"[llm_service] 🧠 Iniciando llamada LLM con modelo: {modelo}")
    print(f"[llm_service] 📏 Largo del prompt: {len(prompt)} caracteres")

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

    print(f"[llm_service] 🚀 Enviando solicitud al modelo {modelo}...")
    resp = oai.chat.completions.create(
        model=modelo,
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

    _guardar_llm_raw_json(reply, tag="items_licitacion")

    return {
        "respuesta": reply.strip(),
        "tokens_input": token_in,
        "tokens_output": token_out
    }
