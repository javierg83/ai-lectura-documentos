from collections import defaultdict
from dev_mock.licitaciones_mock_loader import cargar_licitaciones_mock

def construir_control_room_mock():
    licitaciones = cargar_licitaciones_mock()

    total = len(licitaciones)
    adjudicadas = [l for l in licitaciones if l["estado"] == "Adjudicada"]

    monto_adjudicado_total = sum(
        l["monto_adjudicado"] or 0 for l in adjudicadas
    )

    presupuesto_total = sum(
        l["presupuesto_maximo"] or 0 for l in licitaciones
    )

    por_usuario = defaultdict(lambda: {
        "cargadas": 0,
        "adjudicadas": 0,
        "monto_adjudicado": 0
    })

    for l in licitaciones:
        u = l["usuario"]
        por_usuario[u]["cargadas"] += 1
        if l["estado"] == "Adjudicada":
            por_usuario[u]["adjudicadas"] += 1
            por_usuario[u]["monto_adjudicado"] += l["monto_adjudicado"] or 0

    return {
        "kpis": {
            "total": total,
            "adjudicadas": len(adjudicadas),
            "monto_adjudicado_total": monto_adjudicado_total,
            "presupuesto_total": presupuesto_total
        },
        "por_usuario": por_usuario,
        "licitaciones": licitaciones
    }
