from typing import Any, Dict, List


class ItemsLicitacionSchemaError(Exception):
    """Error de validación del schema ITEMS_LICITACION"""
    pass


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float))


def validate_items_licitacion_schema(data: Dict[str, Any]) -> None:
    """
    Valida que el JSON cumpla con el contrato ITEMS_LICITACION.

    Lanza ItemsLicitacionSchemaError si hay errores.
    """

    if not isinstance(data, dict):
        raise ItemsLicitacionSchemaError("El payload no es un objeto JSON")

    # ----------------------------
    # Nivel raíz
    # ----------------------------
    if data.get("concepto") != "ITEMS_LICITACION":
        raise ItemsLicitacionSchemaError(
            "Campo 'concepto' inválido o ausente"
        )

    if "licitacion" not in data or not isinstance(data["licitacion"], dict):
        raise ItemsLicitacionSchemaError(
            "Campo 'licitacion' ausente o inválido"
        )

    if "items" not in data or not isinstance(data["items"], list):
        raise ItemsLicitacionSchemaError(
            "Campo 'items' ausente o no es lista"
        )

    # ----------------------------
    # Validación licitación
    # ----------------------------
    lic = data["licitacion"]

    if "licitacion_id" not in lic or not isinstance(lic["licitacion_id"], str):
        raise ItemsLicitacionSchemaError(
            "licitacion.licitacion_id ausente o inválido"
        )

    # codigo_licitacion puede ser null o string
    if "codigo_licitacion" in lic and lic["codigo_licitacion"] is not None:
        if not isinstance(lic["codigo_licitacion"], str):
            raise ItemsLicitacionSchemaError(
                "licitacion.codigo_licitacion debe ser string o null"
            )

    # ----------------------------
    # Validación items
    # ----------------------------
    for idx, item in enumerate(data["items"], start=1):
        if not isinstance(item, dict):
            raise ItemsLicitacionSchemaError(
                f"Item #{idx} no es objeto JSON"
            )

        # Campos obligatorios
        for field in ["item_key", "nombre_item"]:
            if field not in item or not isinstance(item[field], str) or not item[field].strip():
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}: campo '{field}' ausente o inválido"
                )

        # cantidad puede ser number o null
        if "cantidad" in item and item["cantidad"] is not None:
            if not _is_number(item["cantidad"]):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}: 'cantidad' debe ser numérico o null"
                )

        # unidad puede ser string o null
        if "unidad" in item and item["unidad"] is not None:
            if not isinstance(item["unidad"], str):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}: 'unidad' debe ser string o null"
                )

        # descripcion / notas
        for field in ["descripcion", "notas"]:
            if field in item and item[field] is not None:
                if not isinstance(item[field], str):
                    raise ItemsLicitacionSchemaError(
                        f"Item #{idx}: '{field}' debe ser string o null"
                    )

        # Listas
        for list_field in [
            "especificaciones",
            "criterios_cumplimiento",
            "exclusiones_o_prohibiciones"
        ]:
            if list_field in item:
                if not isinstance(item[list_field], list):
                    raise ItemsLicitacionSchemaError(
                        f"Item #{idx}: '{list_field}' debe ser lista"
                    )
                for v in item[list_field]:
                    if not isinstance(v, str):
                        raise ItemsLicitacionSchemaError(
                            f"Item #{idx}: '{list_field}' contiene valor no string"
                        )

        # Fuentes
        if "fuentes" not in item or not isinstance(item["fuentes"], list) or not item["fuentes"]:
            raise ItemsLicitacionSchemaError(
                f"Item #{idx}: debe contener al menos una fuente"
            )

        for f_idx, fuente in enumerate(item["fuentes"], start=1):
            if not isinstance(fuente, dict):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}, fuente #{f_idx}: no es objeto"
                )

            for key in ["documento", "documento_id", "pagina", "redis_key"]:
                if key not in fuente:
                    raise ItemsLicitacionSchemaError(
                        f"Item #{idx}, fuente #{f_idx}: falta campo '{key}'"
                    )

            if fuente["pagina"] is not None and not isinstance(fuente["pagina"], int):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}, fuente #{f_idx}: 'pagina' debe ser int o null"
                )

        # confianza_item
        if "confianza_item" in item:
            if not _is_number(item["confianza_item"]):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}: 'confianza_item' debe ser numérico"
                )
            if not (0.0 <= float(item["confianza_item"]) <= 1.0):
                raise ItemsLicitacionSchemaError(
                    f"Item #{idx}: 'confianza_item' fuera de rango 0–1"
                )
