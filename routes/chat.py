# routes/chat.py
from flask import Blueprint, render_template, request, jsonify
import redis
import json
import config
from services.chat_service import run_chat

# Configuración de Redis
redis_client = redis.Redis.from_url(config.REDIS_URL)

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=['GET'])
def chat_page():
    """Renderiza la página de chat con IA (sin embeddings)"""
    print("[chat] 🔹 GET /chat - renderizando chat.html (modo sin embeddings)")
    return render_template('chat.html')


@chat_bp.route('/api/docs', methods=['GET'])
def api_docs():
    """Lista los documentos disponibles para seleccionar en el chat"""
    print("[chat] 🔹 GET /api/docs - listando documentos desde Redis")

    # 🔄 Usamos el mismo patrón que en chat_embedding: doc_raw:*
    pattern = 'doc_raw:*'
    try:
        keys = redis_client.keys(pattern)
        print(f"[chat] 🔹 /api/docs - patrón '{pattern}', claves encontradas: {len(keys)}")
    except Exception as e:
        print(f"[chat] ❌ Error al consultar Redis en /api/docs: {e}")
        return jsonify({'error': 'Error al obtener documentos desde Redis'}), 500

    docs = []
    for key in keys:
        try:
            meta = redis_client.hgetall(key)
            # doc_raw:<doc_id>
            doc_id = key.decode().split(':', 1)[1]

            nombre_original = meta.get(b'nombre_original', b'').decode('utf-8', errors='ignore')
            filename = meta.get(b'filename', b'').decode('utf-8', errors='ignore')
            pages_raw = meta.get(b'pages_count', b'0').decode('utf-8', errors='ignore')
            timestamp = meta.get(b'timestamp', b'').decode('utf-8', errors='ignore')

            try:
                pages_count = int(pages_raw)
            except ValueError:
                pages_count = 0

            docs.append({
                'id': doc_id,
                'filename': filename or nombre_original,
                'original': nombre_original or filename,
                'pages_count': pages_count,
                'timestamp': timestamp,
            })
        except Exception as e:
            print(f"[chat] ❌ Error procesando clave {key}: {e}")
            continue

    print(f"[chat] 🔹 /api/docs - documentos enviados al frontend: {len(docs)}")
    return jsonify(docs)


@chat_bp.route('/api/chat', methods=['POST'])
def api_chat():
    """Maneja las peticiones de chat, normal o con embeddings"""
    print("[chat] 🔹 POST /api/chat - inicio")

    data = request.json or {}
    user_id = data.get('user_id')
    message = data.get('message')
    docs = data.get('docs', [])
    embedding_mode = data.get('embedding_mode', False)

    print(f"[chat]    payload → user_id={user_id}, embedding_mode={embedding_mode}, docs={docs}")

    if not user_id or not message:
        print("[chat] ❌ Falta user_id o message en la petición.")
        return jsonify({'error': 'user_id y message son requeridos'}), 400

    try:
        # run_chat devuelve: (respuesta, token_in, token_out)
        respuesta, token_in, token_out = run_chat(
            user_id=user_id,
            message=message,
            doc_ids=docs,
            embedding_mode=embedding_mode
        )
    except Exception as e:
        print(f"[chat] ❌ Error al ejecutar run_chat: {e}")
        return jsonify({'error': 'Error interno al procesar el chat'}), 500

    print("[chat] ✅ Respuesta generada correctamente en /api/chat")

    return jsonify({
        'reply': respuesta,
        'token_in': token_in,
        'token_out': token_out
    })
