from typing import TypedDict, Literal, Optional, List


class ProductoCatalogo(TypedDict):
    codigo: str
    nombre: str
    descripcion: str
    stock_disponible: int
    ubicacion_stock: str
    codigo_tienda: Optional[str]


class ItemLicitacion(TypedDict):
    item_key: str
    descripcion_detectada: str


class ProductoHomologado(TypedDict):
    codigo: str
    nombre: str
    descripcion: str
    stock_disponible: int
    ubicacion_stock: str
    codigo_tienda: Optional[str]


class CandidatoHomologacion(TypedDict):
    ranking: int
    producto: ProductoCatalogo
    score_similitud: float
    razonamiento: Optional[str]


class ResultadoHomologacion(TypedDict):
    item_key: str
    descripcion_detectada: str
    razonamiento_general: Optional[str]
    candidatos: List[CandidatoHomologacion]


class ResultadoHomologacionLicitacion(TypedDict):
    concepto: Literal["HOMOLOGACION_PRODUCTOS"]
    licitacion_id: str
    resumen: dict
    homologaciones: List[ResultadoHomologacion]
