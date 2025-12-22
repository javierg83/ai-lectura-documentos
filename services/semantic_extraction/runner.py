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

# 🔥 IMPORT CLAVE: fuerza el registro del extractor ITEMS_LICITACION
import services.semantic_extraction.concepts.items_licitacion.extractor  # noqa

from services.semantic_extraction.concepts.items_licitacion.schema import (
    validate_items_licitacion_schema,
    ItemsLicitacionSchemaError,
)
from services.semantic_extraction.concepts.items_licitacion.normalizer import (
    normalize_items_licitacion,
)

# ==========================================================
# REDIS CLIENT
# ==========================================================
redis_url = urlparse(REDIS_URL)
redis_client = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,
    password=redis_url.password,
    db=0,
    ssl=False,
)

# ==========================================================
# POSTGRES / SUPABASE CONNECTION
# ==========================================================
DATABASE_URL = os.getenv("DATABASE_URL")


def _get_pg_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL no está definido en el entorno")
    return psycopg2.connect(DATABASE_URL)


# ==========================================================
# REDIS SEMANTIC SEARCH
# ==========================================================
def _semantic_search(
    *,
    query: str,
    documento_ids: List[str],
    top_k: int,
    min_score: float,
) -> List[Dict[str, Any]]:
    """
    Búsqueda vectorial simple en Redis sobre páginas y elementos.
    Usa distancia euclidiana (menor = mejor).
    """
    import numpy as np

    vector_query = generar_embedding(query, model=MODEL_EMBEDDING)
    if not vector_query:
        return []

    results: List[Dict[str, Any]] = []

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

                dist = float(
                    np.linalg.norm(
                        np.array(vector_query) - np.array(emb)
                    )
                )

                # menor distancia = más similar
                if dist <= min_score:
                    continue

                results.append({
                    "redis_key": key.decode(),
                    "texto": texto,
                    "distancia": dist,
                })

            except Exception:
                continue

    results.sort(key=lambda x: x["distancia"])
    return results[:top_k]


# ==========================================================
# CONTEXT BUILDER
# ==========================================================
def _build_context(chunks: List[Dict[str, Any]]) -> str:
    """
    Construye el contexto textual para la IA,
    incluyendo metadata mínima por fragmento.
    """
    bloques = []
    for c in chunks:
        bloques.append(
            f"[REDIS_KEY={c['redis_key']}]\n{c['texto']}"
        )
    return "\n\n---\n\n".join(bloques)


# ==========================================================
# IA CALL
# ==========================================================
def _call_llm(prompt: str) -> str:
    """
    Llamada al LLM.
    Usa el chat_service existente del proyecto.
    """
    print("[🧠 DEBUG] Entrando a _call_llm()")
    from services.llm_service import run_llm_raw
    return run_llm_raw(prompt)


# ==========================================================
# MAIN RUNNER
# ==========================================================
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
    """
    Pipeline completo:
    Redis → IA → Validación → Normalización → Supabase
    """

    extractor_cls = get_extractor(concepto)
    extractor = extractor_cls(
        licitacion_id=licitacion_id,
        documento_ids=documento_ids,
        top_k=top_k,
        min_score=min_score,
        prompt_version=prompt_version,
        extractor_version=extractor_version,
    )

    print(f"[🧠] Ejecutando extractor semántico: {concepto}")

    # --------------------------------------------------
    # 1. BÚSQUEDA SEMÁNTICA
    # --------------------------------------------------
    semantic_chunks: List[Dict[str, Any]] = []

    for query in extractor.build_queries():
        resultados = _semantic_search(
            query=query,
            documento_ids=documento_ids,
            top_k=top_k,
            min_score=min_score,
        )
        semantic_chunks.extend(resultados)

    if not semantic_chunks:
        raise RuntimeError("No se encontraron fragmentos relevantes en Redis")

    # Deduplicar por redis_key
    unique_chunks = {
        c["redis_key"]: c for c in semantic_chunks
    }.values()

    context = _build_context(list(unique_chunks))

    # --------------------------------------------------
    # 2. PROMPT + IA
    # --------------------------------------------------
    prompt = extractor.build_prompt(context)
    raw_output = _call_llm(prompt)

    # --------------------------------------------------
    # 3. PARSEO + VALIDACIÓN
    # --------------------------------------------------
    parsed = extractor.parse_output(raw_output)

    try:
        validate_items_licitacion_schema(parsed)
    except ItemsLicitacionSchemaError as e:
        raise RuntimeError(f"Schema inválido: {e}")

    # --------------------------------------------------
    # 4. PERSISTENCIA (REPLACE)
    # --------------------------------------------------
    conn = _get_pg_conn()
    cur = conn.cursor()

    try:
        # Desactivar corrida anterior
        cur.execute(
            """
            UPDATE semantic_runs
            SET is_current = false
            WHERE licitacion_id = %s
              AND concepto = %s
              AND is_current = true
            """,
            (licitacion_id, concepto),
        )

        # Insert semantic_run
        cur.execute(
            """
            INSERT INTO semantic_runs
            (licitacion_id, concepto, is_current, prompt_version, extractor_version)
            VALUES (%s, %s, true, %s, %s)
            RETURNING id
            """,
            (licitacion_id, concepto, prompt_version, extractor_version),
        )
        semantic_run_id = cur.fetchone()[0]

        # Guardar JSON bruto
        cur.execute(
            """
            INSERT INTO semantic_results
            (semantic_run_id, concepto, resultado_json)
            VALUES (%s, %s, %s)
            """,
            (semantic_run_id, concepto, json.dumps(parsed)),
        )

        # Evidencias
        for c in unique_chunks:
            cur.execute(
                """
                INSERT INTO semantic_evidences
                (semantic_run_id, redis_key, texto_fragmento)
                VALUES (%s, %s, %s)
                """,
                (semantic_run_id, c["redis_key"], c["texto"]),
            )

        # Normalización
        normalized = normalize_items_licitacion(
            parsed,
            licitacion_id=licitacion_id,
            semantic_run_id=semantic_run_id,
        )

        item_id_map: Dict[str, Any] = {}

        for item in normalized["items"]:
            cur.execute(
                """
                INSERT INTO items_licitados
                (licitacion_id, semantic_run_id, nombre_item, cantidad,
                 unidad, descripcion, observaciones, fuente_resumen)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    item["licitacion_id"],
                    item["semantic_run_id"],
                    item["nombre_item"],
                    item["cantidad"],
                    item["unidad"],
                    item["descripcion"],
                    item["observaciones"],
                    item["fuente_resumen"],
                ),
            )
            item_id_map[item["nombre_item"]] = cur.fetchone()[0]

        for spec in normalized["item_especificaciones"]:
            key = spec["item_ref"].replace("ITEM::", "")
            if key not in item_id_map:
                continue

            cur.execute(
                """
                INSERT INTO item_especificaciones
                (item_id, especificacion)
                VALUES (%s, %s)
                """,
                (item_id_map[key], spec["especificacion"]),
            )

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
        "items_count": len(parsed.get("items", [])),
    }
