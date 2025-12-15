import csv
import redis
from config import REDIS_URL

def cargar_claves_a_borrar(csv_path):
    claves = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            clave = fila.get("clave", "").strip()
            texto = fila.get("texto", "").strip()
            embedding = fila.get("embedding", "").strip()

            # Si falta el texto o el embedding, se considera para eliminación
            if not texto or not embedding:
                claves.append(clave)
    return claves

def borrar_claves_en_redis(claves):
    r = redis.Redis.from_url(REDIS_URL)
    for clave in claves:
        eliminado = r.delete(clave)
        if eliminado:
            print(f"🗑️ Borrada clave: {clave}")
        else:
            print(f"⚠️ No se encontró la clave: {clave}")

if __name__ == "__main__":
    ruta_csv = "reporte_validacion_embeddings.csv"
    claves = cargar_claves_a_borrar(ruta_csv)
    print(f"🔍 Total claves a borrar: {len(claves)}")
    borrar_claves_en_redis(claves)
