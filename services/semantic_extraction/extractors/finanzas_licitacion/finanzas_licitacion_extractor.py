# ==============================================
# Archivo: services/semantic_extraction/extractors/finanzas_licitacion/finanzas_licitacion_extractor.py
# ==============================================

import logging
import datetime
from typing import Any, Dict, List

from services.semantic_extraction.extractors.base_extractor import BaseSemanticExtractor
from services.semantic_extraction.extractors.finanzas_licitacion.schema import validate_finanzas_licitacion_schema
from services.licitacion_service import guardar_finanzas_licitacion, get_pg_conn

logger = logging.getLogger(__name__)

# ==========================================================
# CONFIGURACIÓN DE PROMPT
# ==========================================================
PROMPT_VERSION = "v1"

class FinanzasLicitacionExtractor(BaseSemanticExtractor):
    """
    Extractor semántico del concepto FINANZAS_LICITACION
    """

    concepto = "FINANZAS_LICITACION"

    def build_queries(self, licitacion_id: str) -> List[str]:
        """
        Queries semánticas para obtener información financiera de la licitación.
        """
        queries = [
            "presupuesto referencial",
            "monto total estimado",
            "forma de pago",
            "plazos de pago",
            "fuente de financiamiento",
            "condiciones económicas",
            "garantía de seriedad de la oferta",
            "garantía de fiel cumplimiento",
            "multas por incumplimiento"
        ]

        logger.info(
            "[FINANZAS] Queries semánticas generadas | licitacion_id=%s | queries=%s",
            licitacion_id,
            queries
        )

        return queries

    def build_prompt(self, context: str, licitacion_id: str) -> str:
        """
        Construye el prompt para el LLM.
        """
        logger.info(
            "[FINANZAS] Construyendo prompt | licitacion_id=%s | context_len=%s",
            licitacion_id,
            len(context or "")
        )

        prompt_path = (
            f"{self.concepto.lower()}/"
            f"prompt_{self.concepto.lower()}_{PROMPT_VERSION}.txt"
        )

        prompt_template = self.load_prompt(prompt_path)

        prompt = prompt_template.replace("{contexto}", context)

        logger.debug("[FINANZAS] Prompt generado:\n%s", prompt)

        return prompt

    def parse_output(self, raw_output: str) -> Dict[str, Any]:
        """
        Valida el esquema y lo formatea para guardar.
        """
        logger.info(
            "[FINANZAS] Parseando salida LLM | raw_len=%s",
            len(raw_output or "")
        )

        logger.debug("[FINANZAS] Raw output LLM:\n%s", raw_output)

        # Validar contra esquema esperado
        data = validate_finanzas_licitacion_schema(raw_output)

        logger.info("[FINANZAS] Validación de esquema exitosa")

        # Empaquetar con nombre de concepto
        return {
            "concepto": self.concepto,
            "finanzas": data
        }

    def persist_resultado(self, licitacion_id: str, json_data: Dict[str, Any]) -> None:
        """
        Guarda la información financiera en la base de datos.
        """
        logger.info("[FINANZAS] Guardando resultado en base de datos")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_pg_conn()
        try:
            logger.debug("[FINANZAS] ▶️ Ejecutando guardar_finanzas_licitacion | licitacion_id=%s | campos=%s", licitacion_id, list(json_data.get("finanzas", {}).keys()))
            guardar_finanzas_licitacion(conn, licitacion_id, json_data["finanzas"])
            logger.info("[FINANZAS] ✅ Datos financieros guardados correctamente | licitacion_id=%s", licitacion_id)
        except Exception as e:
            logger.error("[FINANZAS] ❌ Error al guardar datos financieros | licitacion_id=%s | error=%s", licitacion_id, str(e))
            raise
        finally:
            conn.close()
