# routes/chat_embedding.py
import re
from flask import Blueprint, render_template, request, jsonify
from services.embedding_service import list_raw_docs, run_chat_embedding, get_doc_pdf_filename
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
    top_k   = data.get('top_k', 5)

    if not user_id or not message:
        return jsonify({'error': 'user_id y message son requeridos'}), 400

    docs_normalizados = docs
    result = run_chat_embedding(user_id, message, docs_normalizados, top_k=top_k)
    resultados = result.get("resultados", [])

    # Extraer contexto de los top-K resultados para el agente IA
    contenido_partes = []
    for res in resultados:
        if res.get("contenido"):
            # Incluir referencia de página en el contexto
            pagina = res.get("pagina", 0)
            doc = res.get("documento", "")
            contenido_partes.append(f"[Documento: {doc}, Página {pagina}]\n{res['contenido']}")
    
    contenido_util = "\n\n---\n\n".join(contenido_partes)

    if not contenido_util.strip():
        respuesta, token_in, token_out = "No se encontró información relevante en Redis.", 0, 0
    else:
        respuesta, token_in, token_out = run_chat(user_id=user_id, message=message, doc_ids=[], embedding_mode=False, contenido_manual=contenido_util)

    # Obtener metadatos del mejor resultado para la UI
    best_result = resultados[0] if resultados else {}
    best_doc_id = best_result.get("documento", docs[0] if docs else "")
    best_page = best_result.get("pagina", 0)
    pdf_filename = get_doc_pdf_filename(best_doc_id) if best_doc_id else None

    return jsonify({
        "user_id": user_id,
        "message": message,
        "reply": respuesta,
        "token_in": token_in,
        "token_out": token_out,
        "resultados": resultados,
        "page_number": best_page,
        "pdf_filename": pdf_filename,
        "doc_id": best_doc_id,
        "best_match_content": best_result.get("contenido", "")
    })
