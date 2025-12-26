# 📁 services/semantic_extraction/extractors/datos_basicos_licitacion/datos_basicos_extractor.py

from services.semantic_extraction.extractors.base_extractor import BaseExtractor
from services.licitacion_service import actualizar_datos_basicos_licitacion

class DatosBasicosLicitacionExtractor(BaseExtractor):
    def concepto(self) -> str:
        return "datos_basicos_licitacion"

    def build_queries(self, texto: str) -> list[str]:
        return [texto]

    def build_prompt(self, contexto: str) -> str:
        return self.load_prompt("datos_basicos_licitacion/prompt_datos_basicos_licitacion_v1.txt").format(contexto=contexto)

    def parse_output(self, respuesta: str) -> dict:
        try:
            data = self.safe_json_loads(respuesta)
            if not isinstance(data, dict):
                raise ValueError("La respuesta no es un diccionario JSON válido.")
            return data
        except Exception as e:
            raise ValueError(f"Error al parsear salida de LLM: {e}")

    def normalize(self, datos: dict) -> dict:
        return {
            "codigo_licitacion": datos.get("codigo_licitacion", "").strip(),
            "nombre": datos.get("nombre", "").strip(),
            "descripcion": datos.get("descripcion", "").strip(),
            "estado": datos.get("estado", "").strip()
        }

    def persist(self, licitacion_id: str, semantic_run_id: str, datos: dict) -> None:
        actualizar_datos_basicos_licitacion(licitacion_id, datos)
