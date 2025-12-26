import json
from typing import Any, Dict, List

from services.semantic_extraction.extractors.base_extractor import BaseSemanticExtractor
from services.semantic_extraction.registry import register_extractor
from services.semantic_extraction.extractors.items_licitacion.schema import (
    validate_items_licitacion_schema,
    ItemsLicitacionSchemaError
)
from services.semantic_extraction.extractors.items_licitacion.normalizer import (
    normalize_items_licitacion,
)

class ItemsLicitacionExtractor(BaseSemanticExtractor):
    CONCEPTO = "ITEMS_LICITACION"

    @property
    def concepto(self) -> str:
        return self.CONCEPTO

    def build_queries(self) -> List[str]:
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

    def build_prompt(self, context: str) -> str:
        template = self._load_prompt_template()
        return template.replace("{LICITACION_ID}", str(self.licitacion_id)).replace("{CONTEXT}", context)

    def parse_output(self, raw_output: str) -> Dict[str, Any]:
        try:
            parsed = json.loads(raw_output)
        except json.JSONDecodeError as e:
            raise ValueError(f"Salida IA no es JSON válido: {e}")

        if not isinstance(parsed, dict):
            raise ValueError("Salida IA no es un objeto JSON")

        concepto = parsed.get("concepto")
        if concepto != self.CONCEPTO:
            raise ValueError(f"Concepto incorrecto. Esperado={self.CONCEPTO}, recibido={concepto}")

        if "items" not in parsed or not isinstance(parsed["items"], list):
            raise ValueError("JSON no contiene lista 'items' válida")

        # ✅ Reparar estructuras mal generadas por el modelo (fallback)
        licitacion_data = parsed.get("licitacion")
        if isinstance(licitacion_data, dict):
            parsed["licitacion_id"] = licitacion_data.get("id") or licitacion_data.get("licitacion_id")
            parsed["codigo_licitacion"] = licitacion_data.get("codigo_licitacion")
        elif isinstance(licitacion_data, str):
            try:
                temp = json.loads(licitacion_data.replace("'", '"'))
                parsed["licitacion_id"] = temp.get("id")
                parsed["codigo_licitacion"] = temp.get("codigo_licitacion")
            except Exception:
                parsed["licitacion_id"] = licitacion_data

        parsed.setdefault("licitacion_id", self.licitacion_id)

        try:
            validate_items_licitacion_schema(parsed)
        except ItemsLicitacionSchemaError as e:
            raise ValueError(f"Schema inválido: {e}")

        return parsed

    def normalize(self, parsed_output: Dict[str, Any]) -> Dict[str, Any]:
        return normalize_items_licitacion(
            parsed_output,
            licitacion_id=self.licitacion_id,
            semantic_run_id=self.extractor_version or "default",
        )

register_extractor(
    ItemsLicitacionExtractor.CONCEPTO,
    ItemsLicitacionExtractor
)
