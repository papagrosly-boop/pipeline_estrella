import os
import sqlite3

def inicializar_bd():
    os.makedirs('data', exist_ok=True)
    db_path = os.path.join('data', 'datacaos_estrella.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Tabla DimProducto
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DimProducto (
        ProductoID VARCHAR(10) PRIMARY KEY,
        NombreProducto VARCHAR(60) NOT NULL,
        MarcaProducto VARCHAR(25) NOT NULL,
        NombreCategoria VARCHAR(30) NOT NULL,
        NombreProveedor VARCHAR(40) NOT NULL,
        PaisProveedor VARCHAR(20) NOT NULL,
        PrecioListado DECIMAL(12, 2) NOT NULL
    )
    ''')

    # 2. Tabla DimCliente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DimCliente (
        ClienteID VARCHAR(10) PRIMARY KEY,
        NombreCliente VARCHAR(60) NOT NULL,
        Genero VARCHAR(1) NOT NULL,
        RangoEdad VARCHAR(10) NOT NULL,
        Ciudad VARCHAR(20) NOT NULL,
        SegmentoCliente VARCHAR(10) NOT NULL
    )
    ''')

    # 3. Tabla DimTienda
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DimTienda (
        TiendaID VARCHAR(5) PRIMARY KEY,
        NombreTienda VARCHAR(40) NOT NULL,
        Ciudad VARCHAR(20) NOT NULL,
        Region VARCHAR(20) NOT NULL,
        FechaApertura DATE NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print("✅ Base de datos 'data/datacaos_estrella.db' inicializada correctamente.")

if __name__ == '__main__':
    inicializar_bd()