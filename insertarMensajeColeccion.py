from conexion import conectar
import json
from pymongo import MongoClient

db = conectar()
# Acceder a la colección de mensajes motivacionales (si no existe, se crea automáticamente)
coleccion = db["mensajesMotivacionales"]

archivo_json = "mensajesMotivacionales.json"

with open(archivo_json, "r", encoding="utf-8") as archivo:
    mensajes_motivacionales = json.load(archivo)

# Insertar los mensajes en la base de datos
coleccion.insert_one(mensajes_motivacionales)