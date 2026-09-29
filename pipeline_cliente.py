import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'nuevos_clientes.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'datacaos_estrella.db')

def actualizar_dim_cliente():
    print("=== PIPELINE: ACTUALIZANDO DIMENSIÓN CLIENTE ===")
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: No se encontró {CSV_PATH}")
        return

    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    insertados, actualizados = 0, 0

    for _, row in df.iterrows():
        cli_id = str(row['ClienteID']).strip()
        cursor.execute("SELECT ClienteID FROM DimCliente WHERE ClienteID = ?", (cli_id,))
        
        if cursor.fetchone():
            cursor.execute("""
                UPDATE DimCliente
                SET NombreCliente=?, Genero=?, RangoEdad=?, Ciudad=?, SegmentoCliente=?
                WHERE ClienteID=?
            """, (str(row['NombreCliente']), str(row['Genero']), str(row['RangoEdad']),
                  str(row['Ciudad']), str(row['SegmentoCliente']), cli_id))
            actualizados += 1
        else:
            cursor.execute("""
                INSERT INTO DimCliente (ClienteID, NombreCliente, Genero, RangoEdad, Ciudad, SegmentoCliente)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (cli_id, str(row['NombreCliente']), str(row['Genero']),
                  str(row['RangoEdad']), str(row['Ciudad']), str(row['SegmentoCliente'])))
            insertados += 1

    conn.commit()
    conn.close()
    print(f"✅ DimCliente -> Registros procesados: {len(df)} | Insertados: {insertados} | Actualizados: {actualizados}\n")

if __name__ == '__main__':
    actualizar_dim_cliente()