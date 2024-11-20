import random
from conexion import conectar
from bson import ObjectId

db = conectar()
coleccion = db["usuarios"]
# Función para generar el mensaje motivacional
def generar_mensaje_motivacional(usuario_id):
    # Buscar al usuario por su ObjectId
    usuario = coleccion.find_one({"_id": ObjectId(usuario_id)})

    # Obtener la cantidad de audios grabados por el usuario
    cant_audios = usuario.get('cant_audios', 0)

    # Consultar la colección de mensajes en la base de datos para obtener el rango adecuado
    coleccion_mensajes = db["mensajesMotivacionales"]
    
    # Buscar el rango que corresponde a la cantidad de audios
    mensaje = ""

    # Consulta para obtener los mensajes según el rango de audios
    rango_mensajes = coleccion_mensajes.find_one({
        "rango_audios.0": {"$gte": cant_audios},
        "rango_audios.1": {"$lte": cant_audios}
    })
    
    if rango_mensajes:
        # Si se encuentra un rango, seleccionar un mensaje aleatorio
        mensaje = random.choice(rango_mensajes['mensajes'])
    
    return mensaje

print(str(generar_mensaje_motivacional("641ca60334ace7a9ca2cffdb")))