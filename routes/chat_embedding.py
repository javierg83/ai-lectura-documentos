# routes/chat_embedding.py
import re
from flask import Blueprint, render_template, request, jsonify
from services.embedding_service import list_raw_docs, run_chat_embedding
from services.chat_service import run_chat  # ✅ Ahora importado al inicio con soporte para contenido_manual
import redis
from config import REDIS_URL

chat_embedding_bp = Blueprint('chat_embedding', __name__)
r = redis.Redis.from_url(REDIS_URL)

def obtener_docs_detalle():
    claves = r.keys("doc_raw:*")
    documentos = []

    for k in claves:
        try:
            doc_data = r.hgetall(k)
            doc_id = k.decode().replace("doc_raw:", "")
            nombre_original = doc_data.get(b'nombre_original', b'').decode('utf-8', errors='ignore')
            filename = doc_data.get(b'filename', b'').decode('utf-8', errors='ignore')
            paginas = int(doc_data.get(b'pages_count', b'0').decode('utf-8'))
            fecha = doc_data.get(b'timestamp', b'').decode('utf-8', errors='ignore')

            documentos.append({
                "doc_id": doc_id,
                "nombre_original": nombre_original,
                "filename": filename,
                "pages_count": paginas,
                "timestamp": fecha
            })
        except Exception as e:
            print(f"[❌ ERROR] Al procesar documento {k}: {e}")
            continue

    return documentos

@chat_embedding_bp.route('/chat_embedding', methods=['GET'])
def page():
    return render_template('chat_embedding.html')

@chat_embedding_bp.route('/api/doc_raw', methods=['GET'])
def api_doc_raw():
    docs = obtener_docs_detalle()
    return jsonify(docs)

@chat_embedding_bp.route('/api/chat_embedding', methods=['POST'])
def api_chat_embedding():
    data    = request.json or {}
    user_id = data.get('user_id')
    message = data.get('message')
    docs    = data.get('docs', [])

    if not user_id or not message:
        return jsonify({'error': 'user_id y message son requeridos'}), 400

    docs_normalizados = docs
    result = run_chat_embedding(user_id, message, docs_normalizados)

    # 🔄 Extraer mejor contexto y pasar a run_chat()
    contenido_util = "\n\n".join([r.get("contenido", "") for r in result.get("resultados", []) if r.get("contenido")])

    if not contenido_util.strip():
        respuesta, token_in, token_out = "No se encontró información relevante en Redis.", 0, 0
    else:
        respuesta, token_in, token_out = run_chat(user_id=user_id, message=message, doc_ids=[], embedding_mode=False, contenido_manual=contenido_util)

    return jsonify({
        "user_id": user_id,
        "message": message,
        "reply": respuesta,  # ✅ Cambiado de 'respuesta' a 'reply'
        "token_in": token_in,
        "token_out": token_out,
        "resultados": result.get("resultados", [])
    })
