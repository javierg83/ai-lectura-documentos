import json
import os
from typing import Any, Dict, List

from services.semantic_extraction.base_extractor import BaseSemanticExtractor
from services.semantic_extraction.registry import register_extractor


class ItemsLicitacionExtractor(BaseSemanticExtractor):
    """
    Extractor semántico para el concepto ITEMS_LICITACION.

    Se encarga de:
    - definir queries semánticas
    - construir el prompt (usando archivo versionado)
    - validar y parsear la salida JSON del modelo
    """

    CONCEPTO = "ITEMS_LICITACION"

    PROMPT_FILENAME = "prompt_items_licitacion_v1.txt"

    # -------------------------------------------------
    # METADATA
    # -------------------------------------------------

    @property
    def concepto(self) -> str:
        return self.CONCEPTO

    # -------------------------------------------------
    # QUERIES SEMÁNTICAS
    # -------------------------------------------------

    def build_queries(self) -> List[str]:
        """
        Queries orientadas a descubrir ítems solicitados,
        cantidades y especificaciones técnicas.
        """
        return [
            "ítems solicitados",
            "detalle de los ítems",
            "productos requeridos",
            "servicios requeridos",
            "cantidad solicitada",
            "especificaciones técnicas",
            "oferta técnica",
            "anexo oferta",
            "lista de ítems",
            "descripción de los ítems"
        ]

    # -------------------------------------------------
    # PROMPT
    # -------------------------------------------------

    def build_prompt(self, context: str) -> str:
        """
        Construye el prompt final inyectando el contexto
        recuperado desde Redis.
        """
        prompt_template = self._load_prompt_template()

        prompt = prompt_template.replace(
            "{LICITACION_ID}", self.licitacion_id
        ).replace(
            "{CONTEXT}", context
        )

        return prompt

    def _load_prompt_template(self) -> str:
        """
        Carga el prompt versionado desde archivo de texto.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, self.PROMPT_FILENAME)

        if not os.path.exists(prompt_path):
            raise FileNotFoundError(
                f"No se encontró el prompt: {prompt_path}"
            )

        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()

    # -------------------------------------------------
    # PARSEO SALIDA IA
    # -------------------------------------------------

    def parse_output(self, raw_output: str) -> Dict[str, Any]:
        """
        Parsea y valida el JSON devuelto por el modelo.

        Reglas:
        - Debe ser JSON válido
        - Debe contener 'concepto' == ITEMS_LICITACION
        - Debe contener la clave 'items'
        """
        try:
            parsed = json.loads(raw_output)
        except json.JSONDecodeError as e:
            raise ValueError(f"Salida IA no es JSON válido: {e}")

        if not isinstance(parsed, dict):
            raise ValueError("Salida IA no es un objeto JSON")

        concepto = parsed.get("concepto")
        if concepto != self.CONCEPTO:
            raise ValueError(
                f"Concepto incorrecto. Esperado={self.CONCEPTO}, recibido={concepto}"
            )

        if "items" not in parsed or not isinstance(parsed["items"], list):
            raise ValueError("JSON no contiene lista 'items' válida")

        return parsed

    # -------------------------------------------------
    # NORMALIZACIÓN (delegada)
    # -------------------------------------------------

    def normalize(self, parsed_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        La normalización a tablas se realiza en un módulo separado.
        Aquí solo retornamos el JSON validado.
        """
        return parsed_output


# -------------------------------------------------
# REGISTRO AUTOMÁTICO DEL EXTRACTOR
# -------------------------------------------------

register_extractor(
    ItemsLicitacionExtractor.CONCEPTO,
    ItemsLicitacionExtractor
)
