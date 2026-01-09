import json
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")


def cargar_detalle_mock(licitacion_id: str):
    """
    Retorna el detalle mock de una licitación por ID (mock-XXX)
    """
    path = os.path.join(DATA_DIR, "detalle_licitacion_mock.json")

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get(licitacion_id)

DETALLE_PATH = os.path.join(os.path.dirname(__file__), "data", "detalle_licitacion_mock.json")


def cargar_todos_detalles_mock():
    ruta = os.path.join(os.path.dirname(__file__), "data", "detalle_licitacion_mock.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
