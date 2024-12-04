import random
from conexion import conectar
from bson import ObjectId

def crear_mensaje_motivacional(usuario_id):
    db = conectar()
    coleccion = db["usuarios"]
    usuario = coleccion.find_one({"_id": ObjectId(usuario_id)})

    mensaje = {}
    if usuario["rol"]=="tecnico":
        coleccion = db["mensajesMotivacionales"]

        mensaje["mensaje"] = input("Introduce la frase: ").lower()
        mensaje["rango_audios"]=[10, 1000]
        mensaje["id_usuario"]=usuario_id

        coleccion.insert_one(mensaje)

crear_mensaje_motivacional("63ea809051c7dd6fe6e45282")