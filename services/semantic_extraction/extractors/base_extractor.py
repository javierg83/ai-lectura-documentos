# ==============================================
# Archivo: services/semantic_extraction/extractors/base_extractor.py
# ==============================================

import logging
from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

from services.llm_service import run_llm_raw

logger = logging.getLogger(__name__)


class BaseSemanticExtractor(ABC):
    """
    Clase base para extractores semánticos.

    RESPONSABILIDAD:
    - Recibir CONTEXTO ya construido por el runner
    - Construir prompt
    - Ejecutar LLM
    - Parsear salida

    NO DEBE:
    - Importar registry
    - Ejecutar embeddings
    - Resolver extractores
    """

    concepto: Optional[str] = None

    def __init__(self, licitacion_id: str):
        self.licitacion_id = licitacion_id

        # Control de ejecución (evita loops)
        self._has_run = False
        self._started_at: Optional[datetime] = None
        self._finished_at: Optional[datetime] = None

        logger.debug(
            "[BASE_EXTRACTOR] Instanciado | concepto=%s | licitacion_id=%s",
            self.concepto,
            self.licitacion_id
        )

    # ======================================================
    # Métodos a implementar por extractores concretos
    # ======================================================

    @abstractmethod
    def build_queries(self, licitacion_id: str) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def build_prompt(self, context: str, licitacion_id: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def parse_output(self, raw_output: str):
        raise NotImplementedError

    # ======================================================
    # Ejecución principal (invocada por runner)
    # ======================================================

    def run(self, context: str):
        if self._has_run:
            logger.warning(
                "[SEMANTIC][%s] Ejecución duplicada bloqueada | licitacion_id=%s",
                self.concepto,
                self.licitacion_id
            )
            return None

        self._has_run = True
        self._started_at = datetime.utcnow()

        logger.info(
            "[SEMANTIC][%s] ▶️ Inicio extracción | licitacion_id=%s | context_len=%s",
            self.concepto,
            self.licitacion_id,
            len(context or "")
        )

        # Prompt
        prompt = self.build_prompt(context, self.licitacion_id)

        logger.debug(
            "[SEMANTIC][%s] Prompt construido | len=%s",
            self.concepto,
            len(prompt or "")
        )

        # LLM
        logger.info("[SEMANTIC][%s] Ejecutando LLM", self.concepto)
        raw_output = run_llm_raw(prompt)

        if not raw_output:
            logger.error("[SEMANTIC][%s] Salida vacía del LLM", self.concepto)
            raise RuntimeError("Salida vacía del LLM")

        logger.debug(
            "[SEMANTIC][%s] Raw output:\n%s",
            self.concepto,
            raw_output
        )

        # Parseo
        result = self.parse_output(raw_output)

        self._finished_at = datetime.utcnow()

        logger.info(
            "[SEMANTIC][%s] ✅ Extracción finalizada | duracion_ms=%s",
            self.concepto,
            int((self._finished_at - self._started_at).total_seconds() * 1000)
        )

        return result
