import json
import logging

logger = logging.getLogger(__name__)


class FinanzasLicitacionSchemaError(Exception):
    pass


def validate_finanzas_licitacion_schema(raw_output: str) -> dict:
    logger.info("[FINANZAS][SCHEMA] Validando salida LLM")

    if not raw_output:
        logger.error("[FINANZAS][SCHEMA] Salida vacía del LLM")
        raise FinanzasLicitacionSchemaError("Salida vacía del LLM")

    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError as e:
        logger.error(
            "[FINANZAS][SCHEMA] JSON inválido | error=%s | raw=%s",
            str(e),
            raw_output
        )
        raise FinanzasLicitacionSchemaError(
            f"Salida no es JSON válido: {str(e)}"
        )

    if not isinstance(data, dict):
        logger.error(
            "[FINANZAS][SCHEMA] Estructura inválida | tipo=%s",
            type(data)
        )
        raise FinanzasLicitacionSchemaError(
            "La salida debe ser un objeto JSON"
        )

    expected_keys = [
        "presupuesto_referencial",
        "moneda",
        "forma_pago",
        "plazo_pago",
        "fuente_financiamiento",
        "garantias",
        "multas"
    ]

    for key in expected_keys:
        data.setdefault(key, None)

    logger.info(
        "[FINANZAS][SCHEMA] Validación OK | campos=%s",
        list(data.keys())
    )

    return data
