from typing import Dict, Type

from services.semantic_extraction.base_extractor import BaseSemanticExtractor

# El import concreto se hará lazy para evitar dependencias circulares


EXTRACTOR_REGISTRY: Dict[str, Type[BaseSemanticExtractor]] = {}


def register_extractor(concepto: str, extractor_cls: Type[BaseSemanticExtractor]) -> None:
    """
    Registra un extractor para un concepto dado.
    """
    EXTRACTOR_REGISTRY[concepto] = extractor_cls


def get_extractor(concepto: str) -> Type[BaseSemanticExtractor]:
    """
    Retorna la clase del extractor asociada al concepto.
    Lanza KeyError si no existe.
    """
    if concepto not in EXTRACTOR_REGISTRY:
        raise KeyError(f"No hay extractor registrado para el concepto: {concepto}")
    return EXTRACTOR_REGISTRY[concepto]
