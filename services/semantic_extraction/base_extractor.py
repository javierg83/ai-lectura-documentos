from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseSemanticExtractor(ABC):
    """
    Contrato base para todos los extractores semánticos.

    Cada extractor representa un CONCEPTO (ej: ITEMS_LICITACION)
    y define cómo:
    - construir queries semánticas
    - construir el prompt
    - parsear la salida de la IA
    - normalizar resultados para persistencia
    """

    def __init__(
        self,
        licitacion_id: str,
        documento_ids: List[str] | None = None,
        top_k: int = 30,
        min_score: float = 0.25,
        prompt_version: str | None = None,
        extractor_version: str | None = None,
    ):
        self.licitacion_id = licitacion_id
        self.documento_ids = documento_ids or []
        self.top_k = top_k
        self.min_score = min_score
        self.prompt_version = prompt_version
        self.extractor_version = extractor_version

    # -------------------------
    # METADATA DEL CONCEPTO
    # -------------------------

    @property
    @abstractmethod
    def concepto(self) -> str:
        """Nombre del concepto (ej: ITEMS_LICITACION)"""
        raise NotImplementedError

    # -------------------------
    # RECUPERACIÓN SEMÁNTICA
    # -------------------------

    @abstractmethod
    def build_queries(self) -> List[str]:
        """
        Retorna una lista de queries semánticas
        que se usarán contra Redis (vector search).
        """
        raise NotImplementedError

    # -------------------------
    # PROMPT
    # -------------------------

    @abstractmethod
    def build_prompt(self, context: str) -> str:
        """
        Construye el prompt final que se enviará al modelo,
        inyectando el contexto recuperado desde Redis.
        """
        raise NotImplementedError

    # -------------------------
    # PARSEO IA
    # -------------------------

    @abstractmethod
    def parse_output(self, raw_output: str) -> Dict[str, Any]:
        """
        Recibe la salida cruda del modelo (string)
        y retorna un JSON validado (dict).
        Debe lanzar excepción si el JSON es inválido.
        """
        raise NotImplementedError

    # -------------------------
    # NORMALIZACIÓN
    # -------------------------

    @abstractmethod
    def normalize(self, parsed_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convierte el JSON del modelo en estructuras
        listas para persistir en BD.
        """
        raise NotImplementedError
