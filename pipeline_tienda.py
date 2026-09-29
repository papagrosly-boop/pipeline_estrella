import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'nuevas_tiendas.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'datacaos_estrella.db')

def actualizar_dim_tienda():
    print("=== PIPELINE: ACTUALIZANDO DIMENSIÓN TIENDA ===")
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: No se encontró {CSV_PATH}")
        return

    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    insertados, actualizados = 0, 0

    for _, row in df.iterrows():
        tienda_id = str(row['TiendaID']).strip()
        cursor.execute("SELECT TiendaID FROM DimTienda WHERE TiendaID = ?", (tienda_id,))
        
        if cursor.fetchone():
            cursor.execute("""
                UPDATE DimTienda
                SET NombreTienda=?, Ciudad=?, Region=?, FechaApertura=?
                WHERE TiendaID=?
            """, (str(row['NombreTienda']), str(row['Ciudad']),
                  str(row['Region']), str(row['FechaApertura']), tienda_id))
            actualizados += 1
        else:
            cursor.execute("""
                INSERT INTO DimTienda (TiendaID, NombreTienda, Ciudad, Region, FechaApertura)
                VALUES (?, ?, ?, ?, ?)
            """, (tienda_id, str(row['NombreTienda']), str(row['Ciudad']),
                  str(row['Region']), str(row['FechaApertura'])))
            insertados += 1

    conn.commit()
    conn.close()
    print(f"✅ DimTienda -> Registros procesados: {len(df)} | Insertados: {insertados} | Actualizados: {actualizados}\n")

if __name__ == '__main__':
    actualizar_dim_tienda()