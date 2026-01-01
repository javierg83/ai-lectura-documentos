"""
Modulo de persistencia para homologacion de productos.

Este modulo contiene las funciones para insertar y consultar
datos de homologacion en la base de datos.

IMPORTANTE: Todas las funciones reciben la conexion (conn) como parametro.
NO se crean conexiones internamente.

Tablas utilizadas:
- homologaciones_productos: Registro principal de homologacion por item
- candidatos_homologacion: Candidatos de productos para cada homologacion
"""
import psycopg2
from typing import Optional
from datetime import datetime


def insertar_homologacion_producto(
    conn,
    homologacion_id: str,
    licitacion_id: str,
    item_key: str,
    descripcion_detectada: str,
    razonamiento_general: Optional[str],
    tokens_input: int,
    tokens_output: int,
    tokens_total: int,
    modelo_usado: str,
    fecha_homologacion: datetime
) -> None:
    """
    Inserta un registro de homologacion de producto en la tabla homologaciones_productos.

    Args:
        conn: Conexion activa a PostgreSQL
        homologacion_id: UUID de la homologacion
        licitacion_id: UUID de la licitacion
        item_key: Clave del item homologado
        descripcion_detectada: Descripcion del item detectado
        razonamiento_general: Razonamiento del LLM
        tokens_input: Tokens de entrada usados
        tokens_output: Tokens de salida usados
        tokens_total: Total de tokens usados
        modelo_usado: Modelo LLM utilizado
        fecha_homologacion: Fecha/hora de la homologacion
    """
    print(f"[HOMOLOGACION_DB] Insertando homologacion | lid={licitacion_id} | item={item_key}")

    sql = """
        INSERT INTO homologaciones_productos (
            id,
            licitacion_id,
            item_key,
            descripcion_detectada,
            razonamiento_general,
            tokens_input,
            tokens_output,
            tokens_total,
            modelo_usado,
            fecha_homologacion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    with conn.cursor() as cur:
        cur.execute(sql, (
            homologacion_id,
            licitacion_id,
            item_key,
            descripcion_detectada,
            razonamiento_general,
            tokens_input,
            tokens_output,
            tokens_total,
            modelo_usado,
            fecha_homologacion
        ))
    print(f"[HOMOLOGACION_DB] Homologacion insertada OK | item_key={item_key}")


def insertar_candidato_homologacion(
    conn,
    homologacion_id: str,
    ranking: int,
    producto_codigo: str,
    producto_nombre: str,
    producto_descripcion: Optional[str],
    stock_disponible: Optional[int],
    ubicacion_stock: Optional[str],
    score_similitud: float,
    razonamiento: Optional[str]
) -> None:
    """
    Inserta un candidato de homologacion en la tabla candidatos_homologacion.

    Args:
        conn: Conexion activa a PostgreSQL
        homologacion_id: UUID de la homologacion padre
        ranking: Posicion del candidato (1, 2, 3...)
        producto_codigo: Codigo del producto candidato
        producto_nombre: Nombre del producto candidato
        producto_descripcion: Descripcion del producto
        stock_disponible: Stock disponible del producto
        ubicacion_stock: Ubicacion del stock
        score_similitud: Score de similitud (0.0 - 1.0)
        razonamiento: Razonamiento del LLM para este candidato
    """
    print(f"[HOMOLOGACION_DB] Insertando candidato | hid={homologacion_id} | rank={ranking} | cod={producto_codigo}")

    sql = """
        INSERT INTO candidatos_homologacion (
            homologacion_id,
            ranking,
            producto_codigo,
            producto_nombre,
            producto_descripcion,
            stock_disponible,
            ubicacion_stock,
            score_similitud,
            razonamiento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    with conn.cursor() as cur:
        cur.execute(sql, (
            homologacion_id,
            ranking,
            producto_codigo,
            producto_nombre,
            producto_descripcion,
            stock_disponible,
            ubicacion_stock,
            score_similitud,
            razonamiento
        ))
    print(f"[HOMOLOGACION_DB] Candidato insertado OK | codigo={producto_codigo}")


def save_homologacion_result(resultado_json: dict, conn: Optional[psycopg2.extensions.connection] = None):
    """
    DEPRECATED: Esta funcion usa tablas antiguas (homologaciones, homologacion_items, homologacion_candidatos).

    Usar en su lugar:
    - insertar_homologacion_producto() para insertar en homologaciones_productos
    - insertar_candidato_homologacion() para insertar en candidatos_homologacion

    Esta funcion se mantiene por compatibilidad pero NO debe usarse en codigo nuevo.
    """
    print("[HOMOLOGACION_DB] WARNING: save_homologacion_result DEPRECATED. Usar insertar_homologacion_producto.")
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
