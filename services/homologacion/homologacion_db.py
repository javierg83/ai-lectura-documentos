import psycopg2
from psycopg2.extras import Json
from typing import Optional

def save_homologacion_result(resultado_json: dict, conn: Optional[psycopg2.extensions.connection] = None):
    """
    Guarda los resultados de homologación de productos en la base de datos.
    Debe recibir una conexión activa, no la crea internamente.
    """
    if conn is None:
        raise ValueError("Se requiere una conexión activa a la base de datos (conn)")

    licitacion_id = resultado_json.get("licitacion_id")
    if not licitacion_id:
        raise ValueError("El JSON no contiene 'licitacion_id'")

    resumen = resultado_json.get("resumen", {})
    homologaciones = resultado_json.get("homologaciones", [])

    try:
        with conn:
            with conn.cursor() as cur:
                # Insertar encabezado
                cur.execute("""
                    INSERT INTO homologaciones (
                        licitacion_id,
                        total_items_detectados,
                        total_items_con_match,
                        tokens_input,
                        tokens_output,
                        tokens_total,
                        modelo_usado
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (licitacion_id) DO UPDATE SET
                        total_items_detectados = EXCLUDED.total_items_detectados,
                        total_items_con_match = EXCLUDED.total_items_con_match,
                        tokens_input = EXCLUDED.tokens_input,
                        tokens_output = EXCLUDED.tokens_output,
                        tokens_total = EXCLUDED.tokens_total,
                        modelo_usado = EXCLUDED.modelo_usado
                """, (
                    licitacion_id,
                    resumen.get("total_items_detectados"),
                    resumen.get("total_items_con_match"),
                    resumen.get("tokens_input"),
                    resumen.get("tokens_output"),
                    resumen.get("tokens_total"),
                    resumen.get("modelo_usado")
                ))

                # Eliminar candidatos previos si los hubiera
                cur.execute("""
                    DELETE FROM homologacion_candidatos
                    WHERE item_id IN (
                        SELECT id FROM homologacion_items
                        WHERE homologacion_id IN (
                            SELECT id FROM homologaciones WHERE licitacion_id = %s
                        )
                    )
                """, (licitacion_id,))

                # Eliminar homologaciones previas
                cur.execute("""
                    DELETE FROM homologacion_items
                    WHERE homologacion_id IN (
                        SELECT id FROM homologaciones WHERE licitacion_id = %s
                    )
                """, (licitacion_id,))

                # Obtener ID de la homologación recién insertada
                cur.execute("""
                    SELECT id FROM homologaciones
                    WHERE licitacion_id = %s
                """, (licitacion_id,))
                row = cur.fetchone()
                if not row:
                    raise RuntimeError("No se pudo recuperar el ID de la homologación recién insertada")
                homologacion_id = row[0]

                # Insertar ítems homologados y sus candidatos
                for homologacion in homologaciones:
                    item_key = homologacion.get("item_key")
                    descripcion_detectada = homologacion.get("descripcion_detectada")
                    razonamiento_general = homologacion.get("razonamiento_general")

                    cur.execute("""
                        INSERT INTO homologacion_items (
                            homologacion_id,
                            item_key,
                            descripcion_detectada,
                            razonamiento_general
                        ) VALUES (%s, %s, %s, %s)
                        RETURNING id
                    """, (
                        homologacion_id,
                        item_key,
                        descripcion_detectada,
                        razonamiento_general
                    ))
                    item_id = cur.fetchone()[0]

                    for candidato in homologacion.get("candidatos", []):
                        producto = candidato.get("producto", {})
                        cur.execute("""
                            INSERT INTO homologacion_candidatos (
                                item_id,
                                ranking,
                                codigo_producto,
                                nombre_producto,
                                descripcion_producto,
                                stock_disponible,
                                ubicacion_stock,
                                score_similitud,
                                razonamiento
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            item_id,
                            candidato.get("ranking"),
                            producto.get("codigo"),
                            producto.get("nombre"),
                            producto.get("descripcion"),
                            producto.get("stock_disponible"),
                            producto.get("ubicacion_stock"),
                            candidato.get("score_similitud"),
                            candidato.get("razonamiento")
                        ))

        print("✅ Datos de homologación persistidos correctamente en la base de datos.")

    except Exception as e:
        print(f"❌ Error durante la persistencia de homologación: {e}")
        raise
