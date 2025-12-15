import redis
import pandas as pd
from config import REDIS_URL

# Conectar a Redis
r = redis.from_url(REDIS_URL)

# Cargar el Excel con el reporte
df = pd.read_excel("reporte_embeddings_general.xlsx")

# Filtrar las claves que tienen datos incompletos
claves_a_borrar = df[df["comentario"] == "⛔️ Faltan datos"]["clave"].tolist()

print(f"[🧹] Claves a eliminar: {len(claves_a_borrar)}")

# Eliminar claves
eliminadas = 0
for clave in claves_a_borrar:
    resultado = r.delete(clave)
    if resultado:
        print(f"✔️ Clave eliminada: {clave}")
        eliminadas += 1
    else:
        print(f"⚠️ No se pudo eliminar: {clave}")

print(f"\n✅ Total claves eliminadas: {eliminadas} de {len(claves_a_borrar)}")
