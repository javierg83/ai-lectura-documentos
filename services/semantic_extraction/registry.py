# ==============================================
# Archivo: services/semantic_extraction/registry.py
# ==============================================

from typing import Dict, Type

# Interfaz base
from services.semantic_extraction.extractors.base_extractor import BaseSemanticExtractor

# Registro global de extractores
_extractors: Dict[str, Type[BaseSemanticExtractor]] = {}


def register_extractor(concepto: str, extractor_cls: Type[BaseSemanticExtractor]):
    concepto = concepto.upper()

    if concepto in _extractors:
        # 🔹 Mismo extractor → no es error
        if _extractors[concepto] is extractor_cls:
            return

        # 🔹 Otro extractor con mismo concepto → sí es error
        raise ValueError(
            f"Extractor distinto ya registrado para el concepto: {concepto}"
        )

    _extractors[concepto] = extractor_cls

def get_extractor(concepto: str) -> Type[BaseSemanticExtractor]:
    concepto = concepto.upper()
    if concepto not in _extractors:
        raise ValueError(f"No hay extractor registrado para: {concepto}")
    return _extractors[concepto]


# =========================
# REGISTRO DE EXTRACTORES
# =========================

from services.semantic_extraction.extractors.items_licitacion.items_licitacion_extractor import (
    ItemsLicitacionExtractor
)

from services.semantic_extraction.extractors.finanzas_licitacion.finanzas_licitacion_extractor import (
    FinanzasLicitacionExtractor
)

register_extractor("ITEMS_LICITACION", ItemsLicitacionExtractor)
register_extractor("FINANZAS_LICITACION", FinanzasLicitacionExtractor)
