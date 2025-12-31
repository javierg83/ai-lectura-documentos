import sys
import psycopg2
from services.licitacion_service import get_pg_conn, obtener_items_por_licitacion
from services.homologacion.product_loader import cargar_productos_catalogo
from services.homologacion.homologador import homologar_productos_para_licitacion

def main():
    if len(sys.argv) < 2:
        print("Uso: python runner_homologacion_manual.py <LICITACION_ID>")
        sys.exit(1)

    licitacion_id = sys.argv[1]

    # Obtener ítems de licitación
    print(f"[🧾] Obteniendo ítems de licitación {licitacion_id} desde BD...")
    items_licitacion = obtener_items_por_licitacion(licitacion_id)
    if not items_licitacion:
        print(f"[❌] No se encontraron ítems para la licitación {licitacion_id}")
        sys.exit(1)

    # Cargar productos desde catálogo
    productos_catalogo = cargar_productos_catalogo()

    # Obtener conexión
    conn = get_pg_conn()

    try:
        # Ejecutar homologación
        resultado = homologar_productos_para_licitacion(
            licitacion_id=licitacion_id,
            items_licitacion=items_licitacion,
            productos_catalogo=productos_catalogo,
            modelo="gpt-4o",
            conn=conn,
        )
        print("\n[✅] Homologación finalizada correctamente")
        print(f"[🧾] Total ítems homologados: {resultado['resumen']['total_items_con_match']}/{resultado['resumen']['total_items_detectados']}")
        print(f"[🔢] Tokens usados: input={resultado['resumen']['tokens_input']} / output={resultado['resumen']['tokens_output']}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
