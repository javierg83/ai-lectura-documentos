import json
import os
import traceback
from datetime import datetime
from typing import Any, Dict, List
from urllib.parse import urlparse
import re

import psycopg2
import redis

from config import REDIS_URL, MODEL_EMBEDDING
from embeddings import generar_embedding
from services.semantic_extraction.registry import get_extractor

MODO_DEBUG = False

def _json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

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
            except Exception as e:
                print(f"[⚠️] Error procesando clave Redis {key}: {e}")
                continue

    resultados.sort(key=lambda x: x["distancia"])
    print(f"[🔍] Resultados encontrados para query '{query}': {len(resultados)}")

    for i, r in enumerate(resultados[:top_k]):
        print(f"\n[🧩 Chunk #{i+1}] redis_key={r['redis_key']} | distancia={r['distancia']:.4f}")
        print(f"[📝 Texto (primeros 500 chars)]:\n{r['texto'][:500]}")

    return resultados[:top_k]

def _build_context(chunks: List[Dict[str, Any]]) -> str:
    bloques = []
    for c in chunks:
        bloques.append(f"[REDIS_KEY={c['redis_key']}]\n{c['texto']}")
    return "\n\n---\n\n".join(bloques)

def _call_llm(prompt: str) -> str:
    from services.llm_service import run_llm_raw
    return run_llm_raw(prompt)

def _sanitize(text):
    text = re.sub(r"[^a-zA-Z0-9_-]+", "_", text.strip().lower())
    return text or "sin_nombre"

def _guardar_json_en_disco(nombre_licitacion: str, concepto: str, result: dict):
    base_dir = os.path.join("salida_json", _sanitize(nombre_licitacion))
    os.makedirs(base_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{concepto.lower()}_{timestamp}.json"
    path_completo = os.path.join(base_dir, nombre_archivo)
    with open(path_completo, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False, default=_json_serial)
    print(f"[📁] Resultado guardado en: {path_completo}")

def run_semantic_extraction(
    *,
    licitacion_id: str,
    concepto: str,
    documento_ids: List[str],
    nombre_licitacion: str = "sin_nombre",
    top_k: int = 30,
    min_score: float = 0.25,
    prompt_version: str | None = None,
    extractor_version: str | None = None,
) -> Dict[str, Any]:

    print(f"[SEMANTIC] Ejecutando extractor semantico: {concepto}")
    extractor_cls = get_extractor(concepto)
    extractor = extractor_cls(licitacion_id=licitacion_id)
    extractor.prompt_version = prompt_version
    extractor.extractor_version = extractor_version

    semantic_chunks = []
    queries = extractor._call_build_queries()
    for query in queries:
        semantic_chunks.extend(_semantic_search(query, documento_ids, top_k, min_score))

    if not semantic_chunks:
        raise RuntimeError("No se encontraron fragmentos relevantes en Redis")

    context = _build_context(list({c["redis_key"]: c for c in semantic_chunks}.values()))
    print(f"[SEMANTIC] Contexto final tiene {len(context)} caracteres")

    print(f"[SEMANTIC] Ejecutando extractor.run()...")
    print("\n[DEBUG CONTEXT PREVIEW]\n")
    print(context[:4000])
    print("\n[END CONTEXT PREVIEW]\n")

    result = extractor.run(context)

    try:
        _guardar_json_en_disco(nombre_licitacion, concepto, result)
    except Exception as e:
        print(f"[⚠️] Error guardando archivo JSON en disco: {e}")

    if MODO_DEBUG:
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"debug_semantic_{concepto}_{ts}.json"
        print(f"\n[DEBUG] Resultado normalizado:\n")
        print(json.dumps(result, indent=2, ensure_ascii=False, default=_json_serial))
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False, default=_json_serial)
        print(f"\n[DEBUG] Resultado guardado en archivo: {nombre_archivo}")
        return {
            "status": "DEBUG_ONLY",
            "concepto": concepto,
            "mensaje": "No se escribió en base de datos",
        }

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
        """, (semantic_run_id, concepto, json.dumps(result, default=_json_serial)))

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

    try:
        if concepto == "ITEMS_LICITACION":
            from services.licitacion_service import guardar_items_licitacion, guardar_especificaciones_tecnicas
            guardar_items_licitacion(conn, licitacion_id, semantic_run_id, result["items"])
            if "item_especificaciones" in result:
                guardar_especificaciones_tecnicas(conn, semantic_run_id, result["item_especificaciones"])

            # Ejecutar homologación automática
            if result.get("items"):
                try:
                    from services.homologacion.homologacion_service import ejecutar_homologacion_automatica
                    homologacion_resultado = ejecutar_homologacion_automatica(
                        licitacion_id=licitacion_id,
                        conn=conn,
                        modelo="gpt-4o"
                    )
                    print(f"[✅] Homologación ejecutada correctamente | items_con_match={homologacion_resultado.get('resumen', {}).get('total_items_con_match', 0)}")
                except Exception as e:
                    print(f"[⚠️] Error en proceso de homologación automática: {str(e)}")

        elif concepto == "FINANZAS_LICITACION":
            from services.licitacion_service import guardar_finanzas_licitacion
            import datetime
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] 🏦 Procesando resultado de FINANZAS_LICITACION para licitacion_id={licitacion_id}")
            try:
                guardar_finanzas_licitacion(conn, licitacion_id, result["finanzas"])
                print(f"[{now}] ✅ Datos financieros guardados correctamente en BD")
            except Exception as e:
                print(f"[{now}] ❌ Error al guardar datos financieros: {str(e)}")
                raise

        elif concepto == "DATOS_BASICOS_LICITACION":
            from services.licitacion_service import actualizar_datos_basicos_licitacion
            actualizar_datos_basicos_licitacion(
                licitacion_id,
                result.get("datos_basicos", {})
            )
    finally:
        conn.close()

    return {
        "status": "OK",
        "concepto": concepto,
        "semantic_run_id": str(semantic_run_id),
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Uso: python runner.py <CONCEPTO> <DOC_ID> [LICITACION_ID]")
        sys.exit(1)

    concepto = sys.argv[1].strip().upper()

    if concepto == "HOMOLOGACION":
        lic_id = sys.argv[2]
        from services.homologacion.homologacion_service import ejecutar_homologacion_automatica
        print(f"[🧪 CLI] Ejecutando homologación automática para licitación: {lic_id}")
        conn = _get_pg_conn()
        try:
            resultado = ejecutar_homologacion_automatica(
                licitacion_id=lic_id,
                conn=conn,
                modelo="gpt-4o"
            )
            print("[✅] Resultado homologación:")
            print(json.dumps(resultado, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"[❌] Error en ejecución de homologación: {str(e)}")
        finally:
            conn.close()
    else:
        doc_id = sys.argv[2].strip()
        lic_id = sys.argv[3] if len(sys.argv) >= 4 else "testing-uuid"
        try:
            print(f"[🧪 CLI] Ejecutando extracción para '{concepto}' sobre documento: {doc_id}")
            run_semantic_extraction(
                licitacion_id=lic_id,
                concepto=concepto,
                documento_ids=[doc_id],
                nombre_licitacion=doc_id,
                top_k=30,
                min_score=0.15,
                prompt_version="prompt_items_licitacion_v1.txt",
                extractor_version="dev_test"
            )
        except Exception as e:
            print(f"[❌ ERROR CLI] {e}")
