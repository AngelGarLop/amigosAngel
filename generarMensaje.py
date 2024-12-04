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
    mensaje_aleatorio = ""

    # Consulta para obtener los mensajes según el rango de audios
    

    rango_mensajes = coleccion_mensajes.find()

# Verificar si se encontraron documentos
    if rango_mensajes.alive:
        # Convertir el cursor a una lista para acceder a los documentos
        documentos = list(rango_mensajes)
        
        # Filtrar los mensajes que estén dentro del rango de audios solicitado
        mensajes_validos = []
        for doc in documentos:
            for mensaje in doc.get('mensajes', []):
                if mensaje['rango_audios'][0]==cant_audios:
                    min_rango = mensaje['rango_audios'][0]
                    max_rango = mensaje['rango_audios'][1]
                    if min_rango <= cant_audios <= max_rango:
                        mensajes_validos.append(mensaje['mensaje'])
                
                # Comprobar si el rango de audios del mensaje cubre el valor de cant_audios
                
        
        # Si hay mensajes válidos, seleccionar uno aleatorio
        if mensajes_validos:
            mensaje_aleatorio = random.choice(mensajes_validos)

        else:
            print("No se encontraron mensajes en el rango solicitado.")
    else:
        print("No se encontraron documentos en la colección.")
    
    return mensaje_aleatorio

print(str(generar_mensaje_motivacional("641ca60334ace7a9ca2cffdb")))