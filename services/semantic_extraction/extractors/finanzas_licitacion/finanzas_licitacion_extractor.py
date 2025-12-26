import logging

from services.semantic_extraction.extractors.base_extractor import BaseSemanticExtractor
from services.semantic_extraction.extractors.finanzas_licitacion.schema import (
    validate_finanzas_licitacion_schema
)
from services.semantic_extraction.extractors.finanzas_licitacion.normalizer import (
    normalize_finanzas_licitacion
)

logger = logging.getLogger(__name__)


class FinanzasLicitacionExtractor(BaseSemanticExtractor):
    """
    Extractor semántico del concepto FINANZAS_LICITACION
    """

    concepto = "FINANZAS_LICITACION"

    def build_queries(self, licitacion_id: str):
        queries = [
            "presupuesto referencial",
            "monto total",
            "forma de pago",
            "plazos de pago",
            "fuente de financiamiento",
            "condiciones económicas",
            "garantía de seriedad de la oferta",
            "garantía de fiel cumplimiento",
            "multas"
        ]

        logger.info(
            "[FINANZAS] Queries semánticas generadas | licitacion_id=%s | queries=%s",
            licitacion_id,
            queries
        )

        return queries

    def build_prompt(self, context: str, licitacion_id: str) -> str:
        logger.info(
            "[FINANZAS] Construyendo prompt | licitacion_id=%s | context_len=%s",
            licitacion_id,
            len(context or "")
        )

        prompt_template = self.load_prompt(
            "finanzas_licitacion/prompt_finanzas_licitacion_v1.txt"
        )

        prompt = prompt_template.format(
            LICITACION_ID=licitacion_id,
            CONTEXT=context
        )

        logger.debug("[FINANZAS] Prompt generado:\n%s", prompt)

        return prompt

    def parse_output(self, raw_output: str):
        logger.info(
            "[FINANZAS] Parseando salida LLM | raw_len=%s",
            len(raw_output or "")
        )

        logger.debug("[FINANZAS] Raw output LLM:\n%s", raw_output)

        data = validate_finanzas_licitacion_schema(raw_output)

        logger.info(
            "[FINANZAS] Schema validado correctamente | keys=%s",
            list(data.keys())
        )

        normalized = normalize_finanzas_licitacion(data)

        logger.debug(
            "[FINANZAS] Resultado normalizado:\n%s",
            normalized
        )

        return normalized
