# ==============================================
# Archivo: services/semantic_extraction/runner.py (con logs detallados)
# ==============================================

import json
import os
import traceback
from typing import Any, Dict, List
from urllib.parse import urlparse

import psycopg2
import redis

from config import REDIS_URL, MODEL_EMBEDDING
from embeddings import generar_embedding
from services.semantic_extraction.registry import get_extractor

redis_url = urlparse(REDIS_URL)
redis_client = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    db=0,
    ssl=False,
)

DATABASE_URL = os.getenv("DATABASE_URL")

def _get_pg_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no está definido en el entorno")
    return psycopg2.connect(DATABASE_URL)


def _semantic_search(query: str, documento_ids: List[str], top_k: int, min_score: float) -> List[Dict[str, Any]]:
    import numpy as np

    print(f"[🔎] Generando embedding para query: {query}")
    vector = generar_embedding(query, model=MODEL_EMBEDDING)
    if not vector:
        return []

    resultados = []
    for doc_id in documento_ids:
        pattern = f"doc_raw_page:{doc_id}:*_full"
        for key in redis_client.scan_iter(match=pattern):
            data = redis_client.hgetall(key)
            if not data:
                continue
            try:
                emb = json.loads(data.get(b"embedding", b"[]").decode())
                texto = data.get(b"texto", b"").decode()
                if not emb or not texto:
                    continue
                dist = float(np.linalg.norm(np.array(vector) - np.array(emb)))
                if dist <= min_score:
                    continue
                resultados.append({
                    "redis_key": key.decode(),
                    "texto": texto,
                    "distancia": dist,
                })
            except Exception:
                continue

    resultados.sort(key=lambda x: x["distancia"])
    print(f"[🔍] Resultados encontrados para query '{query}': {len(resultados)}")
    return resultados[:top_k]


def _build_context(chunks: List[Dict[str, Any]]) -> str:
    bloques = []
    for c in chunks:
        bloques.append(f"[REDIS_KEY={c['redis_key']}]\n{c['texto']}")
    return "\n\n---\n\n".join(bloques)


def _call_llm(prompt: str) -> str:
    from services.llm_service import run_llm_raw
    return run_llm_raw(prompt)


def run_semantic_extraction(
    *,
    licitacion_id: str,
    concepto: str,
    documento_ids: List[str],
    top_k: int = 30,
    min_score: float = 0.25,
    prompt_version: str | None = None,
    extractor_version: str | None = None,
) -> Dict[str, Any]:

    print(f"[🧠] Ejecutando extractor semántico: {concepto}")
    extractor_cls = get_extractor(concepto)
    extractor = extractor_cls(
        licitacion_id=licitacion_id,
        documento_ids=documento_ids,
        top_k=top_k,
        min_score=min_score,
        prompt_version=prompt_version,
        extractor_version=extractor_version,
    )

    # Paso 1: búsqueda semántica
    semantic_chunks = []
    for query in extractor.build_queries():
        semantic_chunks.extend(_semantic_search(query, documento_ids, top_k, min_score))

    if not semantic_chunks:
        raise RuntimeError("No se encontraron fragmentos relevantes en Redis")

    context = _build_context(list({c["redis_key"]: c for c in semantic_chunks}.values()))
    print(f"[🧠] Contexto final tiene {len(context)} caracteres")

    # Paso 2: llamada IA
    prompt = extractor.build_prompt(context)
    print(f"[📨] Prompt listo. Ejecutando LLM...")
    raw_output = _call_llm(prompt)

    print(f"[📥] Parseando output IA...")
    parsed = extractor.parse_output(raw_output)
    normalized = extractor.normalize(parsed)

    print("[💾] Guardando en base de datos...")
    conn = _get_pg_conn()
    cur = conn.cursor()
    semantic_run_id = None

    try:
        cur.execute("""
            UPDATE semantic_runs
            SET is_current = false
            WHERE licitacion_id = %s AND concepto = %s AND is_current = true
        """, (licitacion_id, concepto))

        cur.execute("""
            INSERT INTO semantic_runs
            (licitacion_id, concepto, is_current, prompt_version, extractor_version)
            VALUES (%s, %s, true, %s, %s)
            RETURNING id
        """, (licitacion_id, concepto, prompt_version, extractor_version))

        semantic_run_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO semantic_results (semantic_run_id, concepto, resultado_json)
            VALUES (%s, %s, %s)
        """, (semantic_run_id, concepto, json.dumps(parsed)))

        for c in semantic_chunks:
            cur.execute("""
                INSERT INTO semantic_evidences (semantic_run_id, redis_key, texto_fragmento)
                VALUES (%s, %s, %s)
            """, (semantic_run_id, c["redis_key"], c["texto"]))

        conn.commit()
        print("[✅] Extracción semántica persistida correctamente")

    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise

    finally:
        cur.close()
        conn.close()

    return {
        "status": "OK",
        "concepto": concepto,
        "semantic_run_id": str(semantic_run_id),
    }


# ==========================================================
# CLI para pruebas sobre documento ya embebido en Redis
# ==========================================================
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python runner.py <CONCEPTO> <DOC_ID> [LICITACION_ID]")
        sys.exit(1)

    concepto = sys.argv[1].strip().upper()
    doc_id = sys.argv[2].strip()
    lic_id = sys.argv[3] if len(sys.argv) >= 4 else "testing-uuid"

    try:
        print(f"[🧪 CLI] Ejecutando extracción para '{concepto}' sobre documento: {doc_id}")
        run_semantic_extraction(
            licitacion_id=lic_id,
            concepto=concepto,
            documento_ids=[doc_id],
            top_k=30,
            min_score=0.15,
            prompt_version="prompt_items_licitacion_v1.txt",
            extractor_version="dev_test"
        )
    except Exception as e:
        print(f"[❌ ERROR CLI] {e}")
