"""
generar_datos.py
Genera 3 archivos CSV con datos ficticios para un proyecto de BI en SQLite:
  data/nuevos_productos.csv  (50 filas)
  data/nuevos_clientes.csv   (200 filas)
  data/nuevas_tiendas.csv    (15 filas)

Uso:  python generar_datos.py
Solo usa la librería estándar (no requiere instalar nada).
"""

import csv
import os
import random
from datetime import date, timedelta

random.seed(42)  # Resultados reproducibles. Cambia o quita la semilla para datos distintos.

CARPETA = "data"
os.makedirs(CARPETA, exist_ok=True)


def guardar_csv(nombre_archivo, columnas, filas):
    ruta = os.path.join(CARPETA, nombre_archivo)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(columnas)
        escritor.writerows(filas)
    print(f"✔ {ruta} -> {len(filas)} filas")


# ---------------------------------------------------------------------------
# 1. PRODUCTOS (50 filas)
# ---------------------------------------------------------------------------
# (NombreProducto, Marca, Categoria, precio_min, precio_max)
CATALOGO = [
    # Computadores y Monitores (10)
    ("Portátil IdeaPad 15", "Lenovo", "Computadores", 1800000, 2800000),
    ("Portátil VivoBook 14", "ASUS", "Computadores", 2000000, 3200000),
    ("Portátil Pavilion 15", "HP", "Computadores", 2200000, 3400000),
    ("Portátil Inspiron 15", "Dell", "Computadores", 2100000, 3300000),
    ("MacBook Air 13", "Apple", "Computadores", 3800000, 4500000),
    ("Monitor 24\" Full HD", "Samsung", "Computadores", 500000, 800000),
    ("Monitor 27\" 4K", "LG", "Computadores", 1300000, 2200000),
    ("Impresora Multifuncional EcoTank", "Epson", "Computadores", 900000, 1500000),
    ("All-in-One IdeaCentre 24", "Lenovo", "Computadores", 2500000, 3600000),
    ("Monitor Curvo 32\"", "Samsung", "Computadores", 1400000, 2400000),
    # Celulares y Tablets (8)
    ("Galaxy S24", "Samsung", "Celulares y Tablets", 3200000, 4500000),
    ("Galaxy A55", "Samsung", "Celulares y Tablets", 1400000, 2000000),
    ("iPhone 15", "Apple", "Celulares y Tablets", 3800000, 4500000),
    ("Redmi Note 13", "Xiaomi", "Celulares y Tablets", 700000, 1200000),
    ("Moto G84", "Motorola", "Celulares y Tablets", 800000, 1200000),
    ("iPad 10ª Generación", "Apple", "Celulares y Tablets", 2000000, 2800000),
    ("Galaxy Tab S9 FE", "Samsung", "Celulares y Tablets", 1600000, 2400000),
    ("Xiaomi Pad 6", "Xiaomi", "Celulares y Tablets", 1200000, 1800000),
    # Audio (12)
    ("Audífonos WH-1000XM5", "Sony", "Audio", 1300000, 1800000),
    ("AirPods Pro 2", "Apple", "Audio", 900000, 1300000),
    ("Galaxy Buds2 Pro", "Samsung", "Audio", 500000, 800000),
    ("Audífonos Tune 770NC", "JBL", "Audio", 350000, 550000),
    ("Parlante Flip 6", "JBL", "Audio", 500000, 700000),
    ("Parlante Charge 5", "JBL", "Audio", 700000, 1000000),
    ("Audífonos QuietComfort 45", "Bose", "Audio", 1200000, 1700000),
    ("Soundbar HT-S400", "Sony", "Audio", 900000, 1400000),
    ("Echo Dot 5ª Gen", "Amazon", "Audio", 200000, 350000),
    ("Audífonos Gamer Cloud II", "HyperX", "Audio", 350000, 550000),
    ("Micrófono USB Yeti", "Blue", "Audio", 450000, 700000),
    ("Parlante SoundLink Flex", "Bose", "Audio", 600000, 900000),
    # Muebles de Oficina (10)
    ("Silla Ergonómica ErgoPro", "Ergotec", "Muebles de Oficina", 600000, 1500000),
    ("Escritorio Ajustable Eléctrico", "Flexispace", "Muebles de Oficina", 1200000, 2500000),
    ("Escritorio en L 160 cm", "Rimax", "Muebles de Oficina", 500000, 1100000),
    ("Silla Gerencial en Cuero", "Jamar", "Muebles de Oficina", 900000, 2200000),
    ("Archivador 4 Gavetas", "Rimax", "Muebles de Oficina", 400000, 800000),
    ("Biblioteca Modular", "Jamar", "Muebles de Oficina", 450000, 1000000),
    ("Mesa de Reuniones 6 Puestos", "Flexispace", "Muebles de Oficina", 1500000, 3200000),
    ("Silla Gamer Pro", "Ergotec", "Muebles de Oficina", 700000, 1400000),
    ("Reposapiés Ergonómico", "Ergotec", "Muebles de Oficina", 150000, 300000),
    ("Panel Divisor Acústico", "Flexispace", "Muebles de Oficina", 350000, 900000),
    # Accesorios (10)
    ("Mouse MX Master 3S", "Logitech", "Accesorios", 400000, 600000),
    ("Teclado Inalámbrico K380", "Logitech", "Accesorios", 150000, 260000),
    ("Webcam C920 HD", "Logitech", "Accesorios", 250000, 420000),
    ("Hub USB-C 7 en 1", "Anker", "Accesorios", 180000, 320000),
    ("Cargador GaN 65W", "Anker", "Accesorios", 150000, 280000),
    ("Power Bank 20000 mAh", "Xiaomi", "Accesorios", 150000, 260000),
    ("Disco Duro Externo 2 TB", "Seagate", "Accesorios", 350000, 520000),
    ("SSD Portátil 1 TB T7", "Samsung", "Accesorios", 450000, 700000),
    ("Memoria USB 128 GB", "SanDisk", "Accesorios", 150000, 220000),
    ("Soporte Portátil de Aluminio", "Baseus", "Accesorios", 150000, 260000),
]

# (NombreProveedor, PaisProveedor)
PROVEEDORES = [
    ("TechDistribuciones S.A.S.", "Colombia"),
    ("Importadora Andina Ltda.", "Colombia"),
    ("Global Electronics Corp.", "Estados Unidos"),
    ("Shenzhen Digital Trading Co.", "China"),
    ("Samsung Electronics Latinoamérica", "Panamá"),
    ("Nippon Audio Supply", "Japón"),
    ("Office Solutions México", "México"),
    ("Mueblería Industrial del Norte", "Colombia"),
    ("EuroTech GmbH", "Alemania"),
    ("Pacific Import Export", "Chile"),
]

assert len(CATALOGO) == 50, "El catálogo debe tener exactamente 50 productos"

filas_productos = []
for i, (nombre, marca, categoria, pmin, pmax) in enumerate(CATALOGO, start=1):
    proveedor, pais = random.choice(PROVEEDORES)
    precio = float(round(random.uniform(pmin, pmax), -4))  # múltiplos de 10.000 COP
    filas_productos.append([f"PRD{i:03d}", nombre, marca, categoria, proveedor, pais, precio])

guardar_csv(
    "nuevos_productos.csv",
    ["ProductoID", "NombreProducto", "MarcaProducto", "NombreCategoria",
     "NombreProveedor", "PaisProveedor", "PrecioListado"],
    filas_productos,
)

# ---------------------------------------------------------------------------
# 2. CLIENTES (200 filas)
# ---------------------------------------------------------------------------
NOMBRES_M = [
    "Juan", "Carlos", "Andrés", "Santiago", "Camilo", "Sebastián", "Daniel", "David",
    "Felipe", "Jorge", "Luis", "Miguel", "Alejandro", "Mateo", "Nicolás", "Julián",
    "Diego", "Esteban", "Iván", "Ricardo", "Hernán", "Fabián", "Óscar", "Sergio",
]
NOMBRES_F = [
    "María", "Valentina", "Camila", "Daniela", "Laura", "Sofía", "Isabella", "Paula",
    "Carolina", "Natalia", "Andrea", "Juliana", "Mariana", "Manuela", "Luisa",
    "Catalina", "Diana", "Angélica", "Viviana", "Lorena", "Sara", "Tatiana", "Karen", "Lina",
]
APELLIDOS = [
    "García", "Rodríguez", "Martínez", "López", "González", "Hernández", "Pérez", "Gómez",
    "Sánchez", "Ramírez", "Torres", "Díaz", "Vargas", "Castro", "Rojas", "Moreno",
    "Jiménez", "Ortiz", "Acosta", "Cardona", "Restrepo", "Ospina", "Álvarez", "Mejía",
    "Gutiérrez", "Herrera", "Muñoz", "Salazar", "Cárdenas", "Quintero", "Arango", "Zapata",
    "Suárez", "Patiño", "Valencia", "Correa", "Builes", "Uribe", "Montoya", "Ríos",
]
RANGOS_EDAD = ["18-25", "26-35", "36-45", "46-55", "56+"]
CIUDADES = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Bucaramanga", "Pereira", "Cartagena"]
PESOS_CIUDAD = [30, 22, 15, 10, 8, 8, 7]
SEGMENTOS = ["Nuevo", "Regular", "VIP", "Inactivo"]
PESOS_SEGMENTO = [25, 45, 10, 20]

filas_clientes = []
nombres_usados = set()
for i in range(1, 201):
    while True:
        genero = random.choice(["M", "F"])
        nombre = random.choice(NOMBRES_M if genero == "M" else NOMBRES_F)
        nombre_completo = f"{nombre} {random.choice(APELLIDOS)} {random.choice(APELLIDOS)}"
        if nombre_completo not in nombres_usados:  # evita nombres duplicados
            nombres_usados.add(nombre_completo)
            break
    filas_clientes.append([
        f"CLI{i:04d}",
        nombre_completo,
        genero,
        random.choices(RANGOS_EDAD, weights=[18, 32, 25, 15, 10])[0],
        random.choices(CIUDADES, weights=PESOS_CIUDAD)[0],
        random.choices(SEGMENTOS, weights=PESOS_SEGMENTO)[0],
    ])

guardar_csv(
    "nuevos_clientes.csv",
    ["ClienteID", "NombreCliente", "Genero", "RangoEdad", "Ciudad", "SegmentoCliente"],
    filas_clientes,
)

# ---------------------------------------------------------------------------
# 3. TIENDAS (15 filas)
# ---------------------------------------------------------------------------
# (NombreTienda, Ciudad, Region)
TIENDAS = [
    ("Tienda Unicentro Bogotá", "Bogotá", "Andina"),
    ("Tienda Centro Andino", "Bogotá", "Andina"),
    ("Tienda Titán Plaza", "Bogotá", "Andina"),
    ("Tienda Oviedo Medellín", "Medellín", "Andina"),
    ("Tienda El Tesoro", "Medellín", "Andina"),
    ("Tienda Jardín Plaza Cali", "Cali", "Pacífica"),
    ("Tienda Chipichape", "Cali", "Pacífica"),
    ("Tienda Buenavista Barranquilla", "Barranquilla", "Caribe"),
    ("Tienda Caribe Plaza Cartagena", "Cartagena", "Caribe"),
    ("Tienda Cacique Bucaramanga", "Bucaramanga", "Andina"),
    ("Tienda Parque Arboleda", "Pereira", "Andina"),
    ("Tienda Viva Villavicencio", "Villavicencio", "Orinoquía"),
    ("Tienda Centro Yopal", "Yopal", "Orinoquía"),
    ("Tienda Leticia Centro", "Leticia", "Amazonía"),
    ("Tienda Florencia Centro", "Florencia", "Amazonía"),
]

assert len(TIENDAS) == 15, "Deben ser exactamente 15 tiendas"

inicio, fin = date(2010, 1, 1), date(2024, 12, 31)
dias_rango = (fin - inicio).days

filas_tiendas = []
for i, (nombre, ciudad, region) in enumerate(TIENDAS, start=1):
    fecha = inicio + timedelta(days=random.randint(0, dias_rango))
    filas_tiendas.append([f"T{i:02d}", nombre, ciudad, region, fecha.strftime("%Y-%m-%d")])

guardar_csv(
    "nuevas_tiendas.csv",
    ["TiendaID", "NombreTienda", "Ciudad", "Region", "FechaApertura"],
    filas_tiendas,
)

print("\nListo. Archivos generados en la carpeta 'data/'.")
