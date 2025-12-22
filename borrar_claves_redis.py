import redis
import sys
from config import REDIS_URL


def borrar_doc_raw_y_paginas(nombre_archivo: str):
    """
    Elimina:
    - doc_raw:{nombre_archivo}
    - doc_raw_page:{nombre_archivo}:*
    """
    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

    total_borradas = 0

    # 1. Borrar doc_raw
    clave_doc_raw = f"doc_raw:{nombre_archivo}"
    if r.delete(clave_doc_raw):
        print(f"🗑️ Borrada clave: {clave_doc_raw}")
        total_borradas += 1
    else:
        print(f"⚠️ No encontrada: {clave_doc_raw}")

    # 2. Borrar doc_raw_page:*
    patron_paginas = f"doc_raw_page:{nombre_archivo}:*"
    claves_paginas = list(r.scan_iter(match=patron_paginas))

    if not claves_paginas:
        print(f"⚠️ No se encontraron páginas con patrón: {patron_paginas}")
    else:
        for clave in claves_paginas:
            r.delete(clave)
            print(f"🗑️ Borrada clave: {clave}")
            total_borradas += 1

    print(f"\n✅ Total de claves eliminadas: {total_borradas}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Uso incorrecto")
        print("👉 python borrar_claves_redis.py <nombre_archivo>")
        print("Ejemplo:")
        print("👉 python borrar_claves_redis.py 08-2025-ec-visa-internacional.pdf")
        sys.exit(1)

    nombre_archivo = sys.argv[1].strip()
    borrar_doc_raw_y_paginas(nombre_archivo)
