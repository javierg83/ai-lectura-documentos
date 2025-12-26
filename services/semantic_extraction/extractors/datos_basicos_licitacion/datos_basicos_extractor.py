# ==============================================
# Archivo: services/semantic_extraction/extractors/datos_basicos_licitacion/datos_basicos_extractor.py
# ==============================================

import logging
from typing import Any, Dict, List

from services.semantic_extraction.extractors.base_extractor import BaseSemanticExtractor
from services.semantic_extraction.extractors.datos_basicos_licitacion.schema import (
    validate_datos_basicos_licitacion_schema
)
from services.semantic_extraction.extractors.datos_basicos_licitacion.normalizer import (
    normalize_datos_basicos_licitacion
)

logger = logging.getLogger(__name__)


class DatosBasicosLicitacionExtractor(BaseSemanticExtractor):
    """
    Extractor semántico del concepto DATOS_BASICOS_LICITACION
    """

    concepto = "DATOS_BASICOS_LICITACION"

    def build_queries(self, licitacion_id: str) -> List[str]:
        queries = [
            "código de licitación",
            "nombre de la licitación",
            "descripción de la licitación",
            "estado de la licitación",
            "objeto de la licitación",
            "identificación del proceso",
            "número de licitación",
            "título del proceso"
        ]

        logger.info(
            "[DATOS_BASICOS] Queries semánticas generadas | licitacion_id=%s | queries=%s",
            licitacion_id,
            queries
        )

        return queries

    def build_prompt(self, context: str, licitacion_id: str) -> str:
        logger.info(
            "[DATOS_BASICOS] Construyendo prompt | licitacion_id=%s | context_len=%s",
            licitacion_id,
            len(context or "")
        )

        prompt_template = self.load_prompt(
            "datos_basicos_licitacion/prompt_datos_basicos_licitacion_v1.txt"
        )

        prompt = prompt_template.replace("{contexto}", context)

        logger.debug("[DATOS_BASICOS] Prompt generado:\n%s", prompt)

        return prompt

    def parse_output(self, raw_output: str) -> Dict[str, Any]:
        logger.info(
            "[DATOS_BASICOS] Parseando salida LLM | raw_len=%s",
            len(raw_output or "")
        )

        logger.debug("[DATOS_BASICOS] Raw output LLM:\n%s", raw_output)

        data = validate_datos_basicos_licitacion_schema(raw_output)

        logger.info(
            "[DATOS_BASICOS] Schema validado correctamente | keys=%s",
            list(data.keys())
        )

        normalized = normalize_datos_basicos_licitacion(data)

        logger.debug(
            "[DATOS_BASICOS] Resultado normalizado:\n%s",
            normalized
        )

        return normalized
