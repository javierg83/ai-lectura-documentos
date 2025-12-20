from openai import OpenAI
import os
import math

# ⚠️ IMPORTANTE: Debes tener esta variable en tu entorno
# OPENAI_API_KEY = "sk-..."

client = OpenAI()

def generar_embedding(texto: str, model: str = "text-embedding-3-small") -> list[float]:
    """
    Genera un embedding usando OpenAI
    """
    try:
        respuesta = client.embeddings.create(
            input=texto,
            model=model,
            encoding_format="float"
        )
        embedding = respuesta.data[0].embedding
        return embedding
    except Exception as e:
        print(f"[embedding_utils] ❌ Error generando embedding: {e}")
        return []

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Calcula la similitud del coseno entre dos vectores
    """
    if not vec1 or not vec2 or len(vec1) != len(vec2):
        print("[embedding_utils] ⚠️ Vectores vacíos o de distinta dimensión")
        return 0.0

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        print("[embedding_utils] ⚠️ Magnitud cero encontrada")
        return 0.0

    return dot_product / (magnitude1 * magnitude2)
