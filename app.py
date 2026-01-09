import os
from flask import Flask, render_template, jsonify
import config

print("[app] 🚀 Iniciando aplicación Flask")

app = Flask(__name__, static_folder='static', template_folder='templates')

# -------------------------------------------------
# IMPORTS EXISTENTES (NO SE TOCAN)
# -------------------------------------------------
from routes.extraction import extraction_bp
from routes.chat import chat_bp
from routes.chat_embedding import chat_embedding_bp

from services.licitacion_service import (
    obtener_licitacion_por_id,
    obtener_items_por_licitacion,
    obtener_todas_las_licitaciones,
    obtener_finanzas_por_licitacion,
    obtener_items_homologados_con_candidatos,
)

# -------------------------------------------------
# IMPORTS MOCK (PROVISORIOS)
# -------------------------------------------------
from dev_mock.licitaciones_mock_loader import cargar_licitaciones_mock
from dev_mock.detalle_licitacion_mock_loader import (
    cargar_detalle_mock,
    cargar_todos_detalles_mock
)

# -------------------------------------------------
# REGISTRO BLUEPRINTS
# -------------------------------------------------
app.register_blueprint(extraction_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(chat_embedding_bp)

# ===============================
# FLAG GLOBAL DEMO / REAL
# ===============================
USE_MOCK = True   # ← cambiar a False para volver a BD real

# ===============================
# RUTAS FRONTEND
# ===============================

@app.route('/')
def home():
    print("[app] 🏠 Renderizando home.html")
    return render_template("home.html")


@app.route('/licitaciones')
def licitaciones():
    print("[app] 📋 Renderizando licitaciones.html")
    return render_template("licitaciones.html")


@app.route('/control-room')
def control_room():
    print("[app] 📊 Renderizando control_room.html")
    return render_template("control_room.html")


@app.route('/archivos_texto/<path:subpath>')
def serve_archivos_texto(subpath):
    return app.send_static_file('archivos_texto/' + subpath)

# ===============================
# API: LICITACIONES (REAL + MOCK)
# ===============================

@app.route('/api/licitaciones')
def api_licitaciones():
    print("[app] 📋 API: Obteniendo licitaciones reales + mock")

    licitaciones = []

    # =========================
    # Caso especial: Real (ID)
    # =========================
    if True:  # No usar USE_MOCK aquí, porque es un mix
        real_id = "2b54095a-5a9c-4510-ade8-4f426487c887"
        
        real = obtener_licitacion_por_id(real_id)
        finanzas = obtener_finanzas_por_licitacion(real_id)
        items = obtener_items_por_licitacion(real_id)
        homologados = obtener_items_homologados_con_candidatos(real_id)

        if real:
            licitaciones.append({
                "id": real.get("id"),
                "codigo_licitacion": real.get("codigo_licitacion") or real.get("id"),
                "nombre": real.get("titulo") or "ADQUISICION DE ESTANQUE MAS BOMBA CENTRIFUGA Y KIT DE INSTALACION",
                "estado": real.get("estado") or "En proceso",
                "usuario": real.get("usuario") or "Javier Gallardo",
                "moneda": finanzas.get("moneda") if finanzas else "CLP",
                "presupuesto_maximo": finanzas.get("presupuesto_referencial") if finanzas else 0,
                "monto_adjudicado": 0,
                "cantidad_items_total": len(items),
                "cantidad_items_adjudicados": len(homologados),
                "fecha_publicacion": real.get("fecha_publicacion") or "2025-01-04",
                "fecha_limite": real.get("fecha_cierre") or "2026-01-31",
                "origen": "real"
            })

    # =========================
    # Mock normales
    # =========================
    if USE_MOCK:
        for lic in cargar_licitaciones_mock():
            licitaciones.append({
                "id": lic["id"],
                "codigo_licitacion": lic.get("codigo_licitacion") or lic.get("id"),
                "nombre": lic.get("nombre"),
                "descripcion": lic.get("descripcion", ""),
                "estado": lic.get("estado"),
                "usuario": lic.get("usuario"),
                "organismo": lic.get("organismo"),
                "moneda": lic.get("moneda"),
                "fecha_publicacion": lic.get("fecha_publicacion"),
                "fecha_limite": lic.get("fecha_limite"),
                "presupuesto_maximo": lic.get("presupuesto_maximo"),
                "monto_adjudicado": lic.get("monto_adjudicado"),
                "cantidad_items_total": lic.get("cantidad_items_total"),
                "cantidad_items_adjudicados": lic.get("cantidad_items_adjudicados"),
                "origen": "mock"
            })

    return jsonify(licitaciones)

# ===============================
# DETALLE LICITACION (REAL / MOCK)
# ===============================

@app.route('/detalle_licitacion/<licitacion_id>')
def detalle_licitacion(licitacion_id):
    print(f"[app] 🔎 Renderizando detalle_licitacion para {licitacion_id}")

    if USE_MOCK and str(licitacion_id).startswith("mock-"):
        print("[app] 🧪 Usando datos MOCK para detalle_licitacion")

        lic_mock = next(
            (l for l in cargar_licitaciones_mock() if l["id"] == licitacion_id),
            {}
        )

        detalle = cargar_detalle_mock(licitacion_id) or {}

        licitacion = {
            "id": lic_mock.get("id"),
            "codigo_licitacion": lic_mock.get("codigo_licitacion"),
            "nombre": lic_mock.get("nombre"),
            "descripcion": lic_mock.get("descripcion", ""),
            "estado": lic_mock.get("estado"),
            "usuario": lic_mock.get("usuario"),
            "organismo_solicitante": lic_mock.get("organismo"),
            "moneda": lic_mock.get("moneda"),
            "fecha_carga": lic_mock.get("fecha_carga"),
            "presupuesto_maximo": lic_mock.get("presupuesto_maximo"),
            "monto_adjudicado": lic_mock.get("monto_adjudicado"),
            "cantidad_items_total": lic_mock.get("cantidad_items_total"),
            "cantidad_items_adjudicados": lic_mock.get("cantidad_items_adjudicados"),
        }

        return render_template(
            "detalle_licitacion.html",
            licitacion=licitacion,
            items=detalle.get("items", []),
            finanzas=detalle.get("finanzas"),
            homologaciones=[]
        )

    licitacion = obtener_licitacion_por_id(licitacion_id) or {}
    items = obtener_items_por_licitacion(licitacion_id)
    finanzas = obtener_finanzas_por_licitacion(licitacion_id)
    homologaciones = obtener_items_homologados_con_candidatos(licitacion_id)

    return render_template(
        "detalle_licitacion.html",
        licitacion=licitacion,
        items=items,
        finanzas=finanzas,
        homologaciones=homologaciones,
    )

# ===============================
# API: CONTROL ROOM (SOLO MOCK)
# ===============================
from datetime import datetime, timedelta

@app.route('/api/control-room')
def api_control_room():
    print("[app] 📊 API Control Room")

    if not USE_MOCK:
        return jsonify({"error": "Control Room solo disponible en modo demo"})

    licitaciones = cargar_licitaciones_mock()
    detalles_dict = cargar_todos_detalles_mock()

    licitaciones_adjudicadas = [l for l in licitaciones if l.get("estado") == "Adjudicada"]
    licitaciones_en_proceso = [l for l in licitaciones if l.get("estado") not in ("Adjudicada", "Desierta", "No Adjudicada")]

    presupuesto_total = sum(l.get("presupuesto_maximo", 0) or 0 for l in licitaciones)
    monto_adjudicado_total = sum(l.get("monto_adjudicado", 0) or 0 for l in licitaciones_adjudicadas)

    por_usuario = {}
    for lic in licitaciones:
        usuario = lic.get("usuario", "Sin asignar")
        por_usuario.setdefault(usuario, {
            "cargadas": 0,
            "adjudicadas": 0,
            "monto_adjudicado": 0,
            "total_items": 0,
            "items_adjudicados": 0
        })
        por_usuario[usuario]["cargadas"] += 1
        por_usuario[usuario]["total_items"] += lic.get("cantidad_items_total", 0) or 0
        if lic.get("estado") == "Adjudicada":
            por_usuario[usuario]["adjudicadas"] += 1
            por_usuario[usuario]["monto_adjudicado"] += lic.get("monto_adjudicado", 0) or 0
            por_usuario[usuario]["items_adjudicados"] += lic.get("cantidad_items_adjudicados", 0) or 0

    for usuario, datos in por_usuario.items():
        total_items = datos["total_items"]
        items_adj = datos["items_adjudicados"]
        total_lic = datos["cargadas"]
        lic_adj = datos["adjudicadas"]
        datos["porcentaje_items"] = round((items_adj / total_items) * 100, 1) if total_items > 0 else 0
        datos["porcentaje_licitaciones"] = round((lic_adj / total_lic) * 100, 1) if total_lic > 0 else 0

    uso_mensual = {}
    for lic in licitaciones:
        fecha = lic.get("fecha_carga")
        if not fecha:
            continue
        mes = fecha[:7]
        uso_mensual[mes] = uso_mensual.get(mes, 0) + 1

    frecuencia_cotizados = {}
    frecuencia_adjudicados = {}
    for lic in licitaciones:
        lic_id = lic.get("id")
        detalle = detalles_dict.get(lic_id)
        if not detalle:
            continue
        items = detalle.get("items", [])
        for item in items:
            nombre = item.get("nombre") or item.get("descripcion") or "Ítem sin nombre"
            frecuencia_cotizados[nombre] = frecuencia_cotizados.get(nombre, 0) + 1
        if lic.get("estado") == "Adjudicada":
            for item in items:
                nombre = item.get("nombre") or item.get("descripcion") or "Ítem sin nombre"
                frecuencia_adjudicados[nombre] = frecuencia_adjudicados.get(nombre, 0) + 1

    top_cotizados = sorted(frecuencia_cotizados.items(), key=lambda x: x[1], reverse=True)[:20]
    top_adjudicados = sorted(frecuencia_adjudicados.items(), key=lambda x: x[1], reverse=True)[:20]

    alertas = []

    sin_responsable = [l for l in licitaciones if l.get("usuario") in (None, "", "Sin asignar")]
    if sin_responsable:
        alertas.append({
            "tipo": "danger",
            "mensaje": f"{len(sin_responsable)} licitaciones sin responsable asignado",
            "ids_afectados": [l["id"] for l in sin_responsable]
        })

    usuarios_carga_alta = [usuario for usuario, datos in por_usuario.items() if datos["cargadas"] - datos["adjudicadas"] > 20]
    if usuarios_carga_alta:
        alertas.append({
            "tipo": "warning",
            "mensaje": f"{len(usuarios_carga_alta)} usuarios con alta carga operativa (más de 20 licitaciones activas)",
            "ids_afectados": usuarios_carga_alta
        })

    sin_items = [l for l in licitaciones if not detalles_dict.get(l["id"], {}).get("items")]
    if sin_items:
        alertas.append({
            "tipo": "danger",
            "mensaje": f"{len(sin_items)} licitaciones sin ítems extraídos",
            "ids_afectados": [l["id"] for l in sin_items]
        })

    sin_candidatos = 0
    for detalle in detalles_dict.values():
        homologaciones = detalle.get("homologaciones", [])
        for h in homologaciones:
            if not h.get("candidatos"):
                sin_candidatos += 1

    if sin_candidatos > 0:
        alertas.append({
            "tipo": "warning",
            "mensaje": f"{sin_candidatos} ítems sin candidatos homologados"
        })

    desviadas = [l for l in licitaciones if (l.get("presupuesto_maximo") or 0) > 0 and abs((l.get("presupuesto_maximo") or 0) - (l.get("monto_adjudicado") or 0)) / (l.get("presupuesto_maximo") or 1) > 0.3]
    if desviadas:
        alertas.append({
            "tipo": "info",
            "mensaje": f"{len(desviadas)} licitaciones con desviación superior al 30% entre presupuesto y adjudicación",
            "ids_afectados": [l["id"] for l in desviadas]
        })

    # ✅ NUEVA ALERTA: fecha límite hoy o mañana
    limite_hoy = datetime.today().date()
    limite_manana = limite_hoy + timedelta(days=1)

    fecha_limite_criticas = []
    for lic in licitaciones:
        fecha_str = lic.get("fecha_limite")
        if not fecha_str:
            continue
        try:
            fecha_limite = datetime.strptime(fecha_str[:10], "%Y-%m-%d").date()
            if fecha_limite in (limite_hoy, limite_manana):
                fecha_limite_criticas.append(lic)
        except Exception:
            continue

    if fecha_limite_criticas:
        alertas.append({
            "tipo": "danger",
            "mensaje": f"{len(fecha_limite_criticas)} licitaciones con fecha límite hoy o mañana",
            "ids_afectados": [l["id"] for l in fecha_limite_criticas]
        })

    return jsonify({
        "kpis": {
            "licitaciones_cargadas": len(licitaciones),
            "licitaciones_en_proceso": len(licitaciones_en_proceso),
            "licitaciones_adjudicadas": len(licitaciones_adjudicadas),
            "presupuesto_total": presupuesto_total,
            "monto_adjudicado_total": monto_adjudicado_total
        },
        "por_usuario": por_usuario,
        "uso_mensual": uso_mensual,
        "items_mas_cotizados": top_cotizados,
        "items_mas_adjudicados": top_adjudicados,
        "licitaciones": licitaciones,
        "alertas": alertas
    })




# ===============================
# MAIN
# ===============================

if __name__ == "__main__":
    print("[app] ✅ Flask corriendo en 0.0.0.0:5000 (debug=True)")
    app.run(host="0.0.0.0", port=5000, debug=True)
