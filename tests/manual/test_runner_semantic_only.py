# Archivo: tests/manual/test_runner_semantic_only.py (multipágina y debug)
import json
import re
from datetime import datetime

from utils.redis_utils import leer_hash, get_redis_connection
from tests.manual.items_extractor_manual import ItemsLicitacionExtractor
from services.semantic_extraction.extractors.items_licitacion.normalizer import normalize_items_licitacion
from services.semantic_extraction.extractors.items_licitacion.schema import validate_items_licitacion_schema

# ----------------------------
# Parámetros del documento
# ----------------------------
documento_id = "BASES_ADMINISTRATIVAS_ESPECIALES__15"
redis_prefix = f"doc_raw_page:{documento_id}:p"
semantic_run_id = "TEST-SEMANTIC-MULTIPAGE"

# ----------------------------
# Función para buscar claves Redis de páginas
# ----------------------------
def obtener_claves_paginas(redis_conn, documento_id):
    patron = f"doc_raw_page:{documento_id}:p*_full"
    return list(redis_conn.scan_iter(match=patron))

# ----------------------------
# Función para convertir datetime en JSON
# ----------------------------
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()

# ----------------------------
# Iniciar
# ----------------------------
redis_conn = get_redis_connection()
claves_paginas = obtener_claves_paginas(redis_conn, documento_id)

if not claves_paginas:
    raise ValueError(f"❌ No se encontraron páginas para el documento '{documento_id}'")

print(f"📄 Total de páginas encontradas: {len(claves_paginas)}")

# ----------------------------
# Ejecutar extractor por cada página
# ----------------------------
extractor = ItemsLicitacionExtractor()
acumulado_raw = {
    "concepto": "ITEMS_LICITACION",
    "licitacion_id": documento_id,
    "codigo_licitacion": None,
    "resumen": {"total_items_detectados": 0, "observaciones": None},
    "items": [],
    "warnings": []
}

for redis_key in sorted(claves_paginas):
    print(f"🔍 Procesando: {redis_key}")
    pagina_data = leer_hash(redis_key)
    texto = pagina_data.get("texto", "")
    pagina_match = re.search(r":p(\d+)_full$", redis_key)
    pagina_num = int(pagina_match.group(1)) if pagina_match else None

    if not texto:
        print(f"⚠️ Página vacía: {redis_key}")
        continue

    doc_input = {
        "documento_id": documento_id,
        "texto": texto,
        "metadata": {
            "documento": documento_id,
            "pagina": pagina_num
        }
    }

    resultado_raw = extractor.run(doc_input)
    acumulado_raw["items"].extend(resultado_raw.get("items", []))
    acumulado_raw["warnings"].extend(resultado_raw.get("warnings", []))

# ----------------------------
# Validar
# ----------------------------
try:
    validate_items_licitacion_schema(acumulado_raw)
    print("✅ Esquema válido para todas las páginas")
except Exception as e:
    print("❌ Error en validación de esquema:")
    print(e)

# ----------------------------
# Normalizar resultado final
# ----------------------------
normalized = normalize_items_licitacion(
    acumulado_raw,
    licitacion_id=documento_id,
    semantic_run_id=semantic_run_id
)

# ----------------------------
# Mostrar resultado
# ----------------------------
print("\n==================== RESULTADO NORMALIZADO ====================")
print(json.dumps(normalized, indent=2, ensure_ascii=False, default=datetime_converter))

# ----------------------------
# Guardar en archivo
# ----------------------------
output_path = f"salida_items_{documento_id}.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(normalized, f, indent=2, ensure_ascii=False, default=datetime_converter)
    print(f"📁 Resultado guardado en: {output_path}")
