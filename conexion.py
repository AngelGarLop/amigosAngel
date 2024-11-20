from pymongo import MongoClient


def conectar():
    # Configuración de la conexión
    MONGO_URI = "mongodb://prelara:pr3l4r4m3c@localhost:27017/"
    client = MongoClient(MONGO_URI,maxPoolSize=80)
    db=client["prelara"]
    return db