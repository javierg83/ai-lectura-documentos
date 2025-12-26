import os
from flask import Flask, render_template, jsonify
import config

print("[app] 🚀 Iniciando aplicación Flask")

# Asegúrate de tener el directorio 'templates' y 'static' en la raíz
app = Flask(__name__, static_folder='static', template_folder='templates')

# Importamos y registramos los blueprints
from routes.extraction import extraction_bp
from routes.chat import chat_bp
from routes.chat_embedding import chat_embedding_bp
from services.licitacion_service import (
    obtener_licitacion_por_id,
    obtener_items_por_licitacion,
    obtener_todas_las_licitaciones,
    obtener_finanzas_por_licitacion  # ✅ nuevo
)

app.register_blueprint(extraction_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(chat_embedding_bp)

# ✅ Ruta raíz que renderiza home.html
@app.route('/')
def home():
    print("[app] 🏠 Renderizando home.html")
    return render_template("home.html")

# ✅ Ruta adicional para servir PDFs desde archivos_texto/<doc_id>/<archivo>.pdf
@app.route('/archivos_texto/<path:subpath>')
def serve_archivos_texto(subpath):
    # Ojo: esto sirve archivos desde /static/archivos_texto.
    # Si tus PDFs están en otro lado, revisa esta ruta.
    return app.send_static_file('archivos_texto/' + subpath)

# ✅ Nueva ruta para listado de licitaciones
@app.route('/licitaciones')
def licitaciones():
    print("[app] 📋 Renderizando licitaciones.html")
    return render_template("licitaciones.html")

@app.route('/api/licitaciones')
def api_licitaciones():
    print("[app] 📋 API: Obteniendo licitaciones desde PostgreSQL")
    licitaciones_list = obtener_todas_las_licitaciones()
    result = []
    for lic in licitaciones_list:
        result.append({
            'id': str(lic['id']),
            'codigo_licitacion': lic['codigo_licitacion'],
            'nombre': lic['nombre'],
            'descripcion': lic['descripcion'],
            'fecha_carga': lic['fecha_carga'],
            'estado': lic['estado']
        })
    return jsonify(result)

# ✅ Ruta para detalle de licitación con finanzas y fallback si no hay datos
@app.route('/detalle_licitacion/<uuid:licitacion_id>')
def detalle_licitacion(licitacion_id):
    licitacion = obtener_licitacion_por_id(licitacion_id)
    if licitacion is None:
        licitacion = {}  # ✅ fallback defensivo
    items = obtener_items_por_licitacion(licitacion_id)
    finanzas = obtener_finanzas_por_licitacion(licitacion_id)  # ✅ nuevos datos
    return render_template('detalle_licitacion.html', licitacion=licitacion, items=items, finanzas=finanzas)

if __name__ == '__main__':
    print("[app] ✅ Flask corriendo en 0.0.0.0:5000 (debug=True)")
    app.run(host='0.0.0.0', port=5000, debug=True)
