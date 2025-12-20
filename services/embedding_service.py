import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from utils.redis_utils import get_redis_client
from utils.embedding_utils import cosine_similarity

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIM = 1536
EMBEDDING_SEPARATOR = "\n"

def generar_embedding(texto: str) -> list[float] | None:
    try:
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=texto
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"[generar_embedding] ❌ Error al generar embedding: {e}")
        return None

def buscar_similares_por_embedding(pregunta: str, chunks: list[str], top_k: int = 5) -> str:
    embedding_pregunta = generar_embedding(pregunta)
    if not embedding_pregunta:
        return "No se pudo generar el embedding de la pregunta."

    similitudes = []
    for chunk in chunks:
        emb_chunk = generar_embedding(chunk)
        if emb_chunk:
            score = cosine_similarity(embedding_pregunta, emb_chunk)
            similitudes.append((score, chunk))

    if not similitudes:
        return "No se encontraron respuestas relevantes."

    similitudes.sort(reverse=True, key=lambda x: x[0])
    top_respuestas = [f"[{i+1}] {s[1]}" for i, s in enumerate(similitudes[:top_k])]
    return "\n\n".join(top_respuestas)

def run_embedding_batch(doc_id, texto_por_pagina):
    """
    Recibe un diccionario {nro_pagina: texto} y genera los embeddings para cada página,
    guardando los resultados en Redis bajo la clave doc_raw_page:{doc_id}:p{n}.
    """
    r = get_redis_client()

    for nro_pagina, texto in texto_por_pagina.items():
        key = f"doc_raw_page:{doc_id.replace('-', '_').replace('.', '')}:p{nro_pagina}"
        print(f"[run_embedding_batch] ⏳ Procesando página {nro_pagina}: {key}")

        # Generar embedding
        embedding = generar_embedding(texto)
        if embedding is None:
            print(f"[run_embedding_batch] ❌ No se pudo generar embedding para página {nro_pagina}")
            continue

        # Guardar en Redis
        r.hset(key, mapping={
            "doc_id": doc_id,
            "nro_pagina": nro_pagina,
            "texto": texto,
            "embedding": json.dumps(embedding)
        })
        print(f"[run_embedding_batch] ✅ Embedding guardado en Redis para página {nro_pagina}")
