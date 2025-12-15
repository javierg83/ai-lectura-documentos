import os
from flask import Flask, render_template
import config

print("[app] 🚀 Iniciando aplicación Flask")

# Asegúrate de tener el directorio 'templates' y 'static' en la raíz
app = Flask(__name__, static_folder='static', template_folder='templates')

# Importamos y registramos los blueprints
from routes.extraction import extraction_bp
from routes.chat import chat_bp
from routes.chat_embedding import chat_embedding_bp

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

if __name__ == '__main__':
    print("[app] ✅ Flask corriendo en 0.0.0.0:5000 (debug=True)")
    app.run(host='0.0.0.0', port=5000, debug=True)
