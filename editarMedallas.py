from conexion import conectar
from pymongo import MongoClient
from bson import ObjectId

# Conectar a la base de datos
db = conectar()

# Acceder a la colección de medallas y usuarios
coleccion_medallas = db["medallas"]
coleccion_usuarios = db["usuarios"]

# Función para verificar si el usuario es un técnico
def es_tecnico(usuario_id):
    usuario = coleccion_usuarios.find_one({"_id": ObjectId(usuario_id)})
    if usuario and usuario.get("rol") == "tecnico":
        return True
    return False

# Función para cambiar el rango de una medalla existente
def cambiar_rango_medalla(usuario_id, medalla_nombre, nuevo_rango):
    if not es_tecnico(usuario_id):
        print("No tienes permisos para realizar esta acción.")
        return
    
    # Buscar la medalla en la colección
    medalla = coleccion_medallas.find_one({"medallas.medalla": medalla_nombre})
    
    if medalla:
        # Actualizar el rango de la medalla en la base de datos
        coleccion_medallas.update_one(
            {"medallas.medalla": medalla_nombre},
            {"$set": {"medallas.$.rango": nuevo_rango}}
        )
        print(f"El rango de la medalla {medalla_nombre} ha sido actualizado a {nuevo_rango}.")
        
        # Actualizar las medallas de los usuarios si es necesario
        actualizar_medallas_usuarios()
    else:
        print("La medalla no existe.")

# Función para añadir una nueva medalla
def añadir_medalla(usuario_id, medalla_nombre, rango):
    if not es_tecnico(usuario_id):
        print("No tienes permisos para realizar esta acción.")
        return
    
    # Añadir la nueva medalla a la colección
    coleccion_medallas.update_one(
        {},
        {"$push": {"medallas": {"medalla": medalla_nombre, "rango": rango}}}
    )
    print(f"La medalla {medalla_nombre} ha sido añadida con rango {rango}.")
    
    # Actualizar las medallas de los usuarios si es necesario
    actualizar_medallas_usuarios()

# Función para actualizar las medallas de todos los usuarios después de modificar las medallas
def actualizar_medallas_usuarios():
    # Obtener todas las medallas
    medallas = coleccion_medallas.find_one({"_id": ObjectId("6750a616a8a21306c000d933")})["medallas"]
    
    # Recorrer todos los usuarios
    usuarios = coleccion_usuarios.find({"cant_audios": {"$exists": True}})
    
    for usuario in usuarios:
        cant_audios = usuario["cant_audios"]
        medallas_asignadas = []

        # Asignar las medallas correspondientes
        for medalla in medallas:
            if cant_audios >= medalla["rango"]:
                medallas_asignadas.append(medalla["medalla"])

        # Actualizar las medallas del usuario
        coleccion_usuarios.update_one(
            {"_id": usuario["_id"]},
            {"$set": {"medallas": medallas_asignadas}}
        )
        print(f"Medallas actualizadas para el usuario {usuario['_id']}: {medallas_asignadas}")


        # Ejemplo de uso
usuario_id_tecnico = "6412f91c20a36f7802a5fe63"  # ID del usuario con rol 'tecnico'

# Cambiar el rango de la medalla "Bronce" a 5
cambiar_rango_medalla(usuario_id_tecnico, "Diamante", 50)

# Añadir una nueva medalla "Emerald" con rango 15
#añadir_medalla(usuario_id_tecnico, "Esmeralda", 20)