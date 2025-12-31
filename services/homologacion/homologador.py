import json
from pathlib import Path
from datetime import datetime
from uuid import uuid4

from services.homologacion.homologacion_db import get_pg_conn
from services.llm_service import call_llm
from services.homologacion.product_loader import load_productos_base
from licitacion_service import obtener_items_licitacion
from services.homologacion.homologacion_db import (
    insertar_homologacion_producto,
    insertar_candidato_homologacion,
)

PROMPT_PATH = Path("services/homologacion/prompts/prompt_homologacion_v3.txt")



def build_prompt_homologacion(item: dict, productos_base: list[str]) -> str:
    prompt_base = PROMPT_PATH.read_text(encoding="utf-8")

    prompt = prompt_base.replace("{DESCRIPCION}", item["descripcion"])
    prompt = prompt.replace("{PRODUCTOS_BASE}", json.dumps(productos_base, ensure_ascii=False, indent=2))

    return prompt


def homologar_productos_para_licitacion(licitacion_id: str):
    conn = get_pg_conn()

    print(f"[🏁] Iniciando proceso de homologación para licitación: {licitacion_id}")

    productos_base = load_productos_base()
    if not productos_base:
        print("[❌] No se encontraron productos base para homologar.")
        return

    items = obtener_items_licitacion(conn, licitacion_id)
    if not items:
        print("[❌] No se encontraron ítems para esta licitación.")
        return

    for item in items:
        print(f"\n[🔎] Procesando ítem: {item['item_key']}")

        prompt = build_prompt_homologacion(item, productos_base)
        resultado_llm = call_llm(prompt)

        try:
            datos = json.loads(resultado_llm)
        except json.JSONDecodeError:
            print("[❌] Error al parsear respuesta del modelo.")
            continue

        homologacion_id = str(uuid4())
        now = datetime.utcnow()

        # Insertar homologación general
        insertar_homologacion_producto(
            conn,
            homologacion_id=homologacion_id,
            licitacion_id=licitacion_id,
            item_key=item["item_key"],
            descripcion_detectada=item["descripcion"],
            razonamiento_general=datos.get("razonamiento_general"),
            tokens_input=datos.get("tokens_input", 0),
            tokens_output=datos.get("tokens_output", 0),
            tokens_total=datos.get("tokens_total", 0),
            modelo_usado=datos.get("modelo_usado"),
            fecha_homologacion=now,
        )
        print("[✅] Homologación insertada")

        # Insertar candidatos
        for candidato in datos.get("candidatos", []):
            insertar_candidato_homologacion(
                conn,
                homologacion_id=homologacion_id,
                ranking=candidato.get("ranking"),
                producto_codigo=candidato.get("producto_codigo"),
                producto_nombre=candidato.get("producto_nombre"),
                producto_descripcion=candidato.get("producto_descripcion"),
                stock_disponible=candidato.get("stock_disponible"),
                ubicacion_stock=candidato.get("ubicacion_stock"),
                score_similitud=candidato.get("score_similitud"),
                razonamiento=candidato.get("razonamiento"),
            )
            print(f"[📥] Candidato insertado: {candidato.get('producto_codigo')}")

    print("\n[✅] Proceso de homologación finalizado.")
