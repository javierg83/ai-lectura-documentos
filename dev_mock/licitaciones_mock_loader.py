import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "dev_mock", "data")


def cargar_licitaciones_mock():
    path = os.path.join(DATA_DIR, "licitaciones_mock.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f).get("licitaciones", [])
