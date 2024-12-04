from conexion import conectar
from pymongo import MongoClient
from bson import ObjectId

# Conectar a la base de datos
db = conectar()

# Acceder a la colección de medallas
coleccion_medallas = db["medallas"]

# Acceder a la colección de usuarios
coleccion_usuarios = db["usuarios"]

# Obtener las medallas desde la colección
medallas_documento = coleccion_medallas.find_one({"_id": ObjectId("6750a616a8a21306c000d933")})

def asignar_medallas(cant_audios):
    medallas_asignadas = []
    
    # Iterar sobre las medallas y rangos
    for medalla in medallas_documento["medallas"]:
        if cant_audios == medalla["rango"]:
            # Si la cantidad de audios coincide con el rango de la medalla, se asigna
            medallas_asignadas.append({
                "medalla": medalla["medalla"],
                "rango": medalla["rango"]
            })
    
    return medallas_asignadas

# Función para actualizar las medallas de todos los usuarios
def actualizar_medallas_a_todos_los_usuarios():
    # Obtener todos los usuarios con el campo cant_audios
    usuarios = coleccion_usuarios.find({"cant_audios": {"$exists": True}})
    
    for usuario in usuarios:
        cant_audios_usuario = usuario.get("cant_audios", 0)  # Obtener la cantidad de audios del usuario

        # Asignar las medallas al usuario
        medallas_asignadas = asignar_medallas(cant_audios_usuario)
        
        if medallas_asignadas:
            # Actualizar el campo de medallas del usuario si se asignaron medallas
            coleccion_usuarios.update_one(
                {"_id": usuario["_id"]},
                {"$set": {"medallas": medallas_asignadas}}
            )
            print(f"Medallas asignadas al usuario {usuario['_id']}: {medallas_asignadas}")
        else:
            print(f"No se asignaron medallas al usuario {usuario['_id']} debido a que no hay medallas que coincidan con {cant_audios_usuario}.")

# Ejecutar la actualización para todos los usuarios
actualizar_medallas_a_todos_los_usuarios()