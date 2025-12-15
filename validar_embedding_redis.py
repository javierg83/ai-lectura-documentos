# validar_embedding_redis.py
import redis
import json
import csv
from config import REDIS_URL

def validar_claves():
    r = redis.from_url(REDIS_URL)
    keys = list(r.scan_iter("doc_raw_page:*"))
    total = len(keys)

    if total == 0:
        print("⚠️ No se encontraron claves con el patrón doc_raw_page:*")
        return

    print(f"[🔍] Total claves encontradas: {total}\n")

    filas_csv = []

    for k in keys:
        clave = k.decode("utf-8")
        tipo = r.type(clave).decode("utf-8")

        resumen = {
            "clave": clave,
            "tipo": tipo,
            "tiene_texto": False,
            "tiene_embedding": False,
            "dimensiones_embedding": 0,
            "observacion": ""
        }

        if tipo != "hash":
            resumen["observacion"] = "❌ Tipo no compatible (esperado: hash)"
            filas_csv.append(resumen)
            print(f"🔹 Clave: {clave} → Tipo: {tipo}")
            print(f"    • {resumen['observacion']}\n")
            continue

        data = r.hgetall(clave)
        texto = data.get(b"texto")
        embedding_raw = data.get(b"embedding")

        print(f"🔹 Clave: {clave} → Tipo: hash")

        if texto:
            resumen["tiene_texto"] = True
            texto_mostrado = texto.decode("utf-8")[:80].replace("\n", " ") + "..."
            print(f"    • 📄 Texto: {texto_mostrado}")
        else:
            print(f"    • ⛔️ Sin campo \"texto\"")

        if embedding_raw:
            try:
                emb = json.loads(embedding_raw)
                resumen["tiene_embedding"] = True
                resumen["dimensiones_embedding"] = len(emb)
                print(f"    • 🧠 Embedding: {len(emb)} dimensiones")
            except:
                resumen["observacion"] = "❌ Error al decodificar embedding"
                print(f"    • ❌ Error al decodificar embedding")
        else:
            print(f"    • ⛔️ Embedding no encontrado")

        print("")
        filas_csv.append(resumen)

    # Guardar CSV
    with open("reporte_validacion_embeddings.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "clave", "tipo", "tiene_texto", "tiene_embedding", "dimensiones_embedding", "observacion"
        ])
        writer.writeheader()
        writer.writerows(filas_csv)

    print("✅ Reporte CSV generado: reporte_validacion_embeddings.csv")

if __name__ == "__main__":
    validar_claves()
