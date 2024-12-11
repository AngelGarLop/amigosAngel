from conexion import conectar
from bson import ObjectId

# Pipeline de agregación para contar usuarios por rango de medallas
#Función 2: Agrupar y contar usuarios por el rango de medalla
def agrupaMedalla():
    db = conectar()
    coleccion_usuarios = db["usuarios"]
    pipeline = [
        {
            "$unwind": "$medallas"  # Desenrollar el array de medallas para trabajar con cada medalla individualmente
        },
        {
            "$group": {
                "_id": "$medallas.medalla",  # Agrupar por rango de medalla
                "total_usuarios": {"$count": {}}  # Contar el número de usuarios por rango
            }
        },
        {
            "$sort": {"total_usuarios": -1}  # Ordenar de mayor a menor por cantidad de usuarios
        }
    ]

    resultados = coleccion_usuarios.aggregate(pipeline)

    # Mostrar los resultados
    for resultado in resultados:
        print(f"Rango: {resultado['_id']} - Total de usuarios: {resultado['total_usuarios']}")

agrupaMedalla()        