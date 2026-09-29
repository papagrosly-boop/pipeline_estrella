import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'nuevos_productos.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'datacaos_estrella.db')

def actualizar_dim_producto():
    print("=== PIPELINE: ACTUALIZANDO DIMENSIÓN PRODUCTO ===")
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: No se encontró {CSV_PATH}")
        return

    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    insertados, actualizados = 0, 0

    for _, row in df.iterrows():
        prod_id = str(row['ProductoID']).strip()
        cursor.execute("SELECT ProductoID FROM DimProducto WHERE ProductoID = ?", (prod_id,))
        
        if cursor.fetchone():
            cursor.execute("""
                UPDATE DimProducto
                SET NombreProducto=?, MarcaProducto=?, NombreCategoria=?, NombreProveedor=?, PaisProveedor=?, PrecioListado=?
                WHERE ProductoID=?
            """, (str(row['NombreProducto']), str(row['MarcaProducto']), str(row['NombreCategoria']),
                  str(row['NombreProveedor']), str(row['PaisProveedor']), float(row['PrecioListado']), prod_id))
            actualizados += 1
        else:
            cursor.execute("""
                INSERT INTO DimProducto (ProductoID, NombreProducto, MarcaProducto, NombreCategoria, NombreProveedor, PaisProveedor, PrecioListado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (prod_id, str(row['NombreProducto']), str(row['MarcaProducto']),
                  str(row['NombreCategoria']), str(row['NombreProveedor']), str(row['PaisProveedor']), float(row['PrecioListado'])))
            insertados += 1

    conn.commit()
    conn.close()
    print(f"✅ DimProducto -> Registros procesados: {len(df)} | Insertados: {insertados} | Actualizados: {actualizados}\n")

if __name__ == '__main__':
    actualizar_dim_producto()