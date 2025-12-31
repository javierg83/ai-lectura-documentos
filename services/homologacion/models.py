from typing import TypedDict, Literal, Optional


class ProductoBase(TypedDict):
    codigo: str                     # cod_prod
    nombre: str                     # producto
    descripcion: str                # descripcion
    stock_disponible: int           # cantidad
    ubicacion_stock: str            # ubicación
    codigo_tienda: Optional[str]    # cod_tienda (opcional)


class ItemDetectado(TypedDict):
    item_key: str
    descripcion_detectada: str


class ProductoHomologado(TypedDict):
    codigo: str
    nombre: str
    descripcion: str
    stock_disponible: int
    ubicacion_stock: str
    codigo_tienda: Optional[str]


class ResultadoHomologacion(TypedDict):
    item_key: str
    descripcion_detectada: str
    producto_homologado: Optional[ProductoHomologado]
    score_similitud: float
    metodo: Literal["GPT-4o", "heuristica", "embedding"]
    razonamiento: Optional[str]


class ResultadoHomologacionLicitacion(TypedDict):
    concepto: Literal["HOMOLOGACION_PRODUCTOS"]
    licitacion_id: str
    resumen: dict  # e.g., {"total_items_detectados": 5, "total_items_homologados": 4}
    homologaciones: list[ResultadoHomologacion]
