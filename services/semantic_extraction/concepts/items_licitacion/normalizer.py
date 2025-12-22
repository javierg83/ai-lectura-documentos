from typing import Any, Dict, List
from datetime import datetime
import unicodedata
import re


def _normalize_text(text: str) -> str:
    """
    Normaliza texto para llaves internas:
    - minúsculas
    - sin tildes
    - sin caracteres especiales
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9_ ]+", "", text)
    text = re.sub(r"\s+", "_", text).strip("_")
    return text


def normalize_items_licitacion(
    parsed_output: Dict[str, Any],
    *,
    licitacion_id: str,
    semantic_run_id: str
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Convierte el JSON del extractor ITEMS_LICITACION en
    estructuras listas para persistir en BD.

    Retorna un dict con:
    - items
    - item_especificaciones
    - item_evidences (opcional, si existen fuentes)
    """

    items_rows: List[Dict[str, Any]] = []
    specs_rows: List[Dict[str, Any]] = []
    item_evidences: List[Dict[str, Any]] = []

    now = datetime.utcnow()

    for item in parsed_output.get("items", []):
        item_id_placeholder = f"ITEM::{item.get('item_key')}"

        item_row = {
            "id": None,  # se asigna al insertar en BD
            "licitacion_id": licitacion_id,
            "semantic_run_id": semantic_run_id,
            "nombre_item": item.get("nombre_item"),
            "cantidad": item.get("cantidad"),
            "unidad": item.get("unidad"),
            "descripcion": item.get("descripcion"),
            "observaciones": item.get("notas"),
            "fuente_resumen": _build_fuente_resumen(item.get("fuentes", [])),
            "created_at": now,
        }

        items_rows.append(item_row)

        # -------------------------
        # Especificaciones técnicas
        # -------------------------
        for spec in item.get("especificaciones", []):
            specs_rows.append({
                "item_ref": item_id_placeholder,
                "especificacion": spec,
                "created_at": now,
            })

        # -------------------------
        # Evidencias por ítem (opcional)
        # -------------------------
        for fuente in item.get("fuentes", []):
            if fuente.get("redis_key"):
                item_evidences.append({
                    "item_ref": item_id_placeholder,
                    "redis_key": fuente.get("redis_key"),
                    "documento_id": fuente.get("documento_id"),
                    "pagina": fuente.get("pagina"),
                    "created_at": now,
                })

    return {
        "items": items_rows,
        "item_especificaciones": specs_rows,
        "item_evidences": item_evidences,
    }


def _build_fuente_resumen(fuentes: List[Dict[str, Any]]) -> str | None:
    """
    Genera un resumen corto de fuentes tipo:
    'p.12; p.15; p.18'
    """
    paginas = []
    for f in fuentes:
        p = f.get("pagina")
        if isinstance(p, int):
            paginas.append(p)

    if not paginas:
        return None

    paginas = sorted(set(paginas))
    return "; ".join(f"p.{p}" for p in paginas)
