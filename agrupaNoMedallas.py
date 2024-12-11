from conexion import conectar
from bson import ObjectId

def agrupaNoMedalla():
    db = conectar()
    coleccion_usuarios = db["usuarios"]
    pipeline = [
        {
            "$match": {
                "medallas": {"$exists": False},  # Buscar usuarios que no tienen el campo "medallas"
                "rol": "cliente"  # Filtrar solo los usuarios con el rol "cliente"
            }
        },
        {
            "$group": {
                "_id": "$rol",  # Agrupar por el campo 'rol'
                "usuarios_sin_medallas": {"$sum": 1}  # Contar los usuarios que no tienen medallas
            }
        }
    ]

    resultados = coleccion_usuarios.aggregate(pipeline)

    # Mostrar los resultados
    for resultado in resultados:
        print(f"Total de usuarios sin medallas con rol '{resultado['_id']}': {resultado['usuarios_sin_medallas']}")

agrupaNoMedalla()