from pipeline_producto import actualizar_dim_producto
from pipeline_cliente import actualizar_dim_cliente
from pipeline_tienda import actualizar_dim_tienda

def ejecutar_pipeline_completo():
    print("==================================================")
    print("🚀 INICIANDO EJECUCIÓN DE PIPELINES DE DIMENSIONES")
    print("==================================================\n")

    actualizar_dim_producto()
    actualizar_dim_cliente()
    actualizar_dim_tienda()

    print("==================================================")
    print("🎉 PIPELINE COMPLETADO EXITOSAMENTE")
    print("==================================================")

if __name__ == '__main__':
    ejecutar_pipeline_completo()