import redis
import pandas as pd
from config import REDIS_URL

# Conexión a Redis
r = redis.from_url(REDIS_URL)

# Variables para reporte
reporte = []

print("[🔍] Buscando todas las claves en Redis...")
for key in r.scan_iter("*"):
    tipo = r.type(key).decode()

    # Solo analizamos hashes
    if tipo != 'hash':
        continue

    datos = r.hgetall(key)
    tiene_embedding = b'embedding_content' in datos
    tiene_texto = b'texto' in datos or b'text' in datos

    embedding_dim = 0
    if tiene_embedding:
        try:
            vector = eval(datos[b'embedding_content'].decode())
            embedding_dim = len(vector) if isinstance(vector, list) else 0
        except:
            embedding_dim = 0

    reporte.append({
        "clave": key.decode(),
        "tipo": tipo,
        "tiene_embedding": tiene_embedding,
        "embedding_dim": embedding_dim,
        "tiene_texto": tiene_texto,
        "comentario": "✅ OK" if tiene_embedding and tiene_texto else "⛔️ Faltan datos"
    })

# Guardar reporte
df = pd.DataFrame(reporte)
df = df.sort_values(by="clave")
df.to_excel("reporte_embeddings_general.xlsx", index=False)

print("✅ Reporte generado: reporte_embeddings_general.xlsx")
