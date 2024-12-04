from conexion import conectar
from pymongo import MongoClient
import json

# Conectar a la base de datos
db = conectar()

# Acceder a la colección de medallas (si no existe, se crea automáticamente)
coleccion_medallas = db["medallas"]

# Definir los datos de ejemplo para las medallas
medallas = {
    "medallas": [
        {"medalla": "Hierro", "rango": 2},
        {"medalla": "Bronce", "rango": 4},
        {"medalla": "Plata", "rango": 6},
        {"medalla": "Oro", "rango": 8},
        {"medalla": "Platino", "rango": 10},
        {"medalla": "Diamante", "rango": 20}
    ]
}

# Insertar los datos de medallas en la colección de medallas
coleccion_medallas.insert_one(medallas)

# Verificar que la inserción fue exitosa (puedes imprimir el contenido de la colección)
for medalla in coleccion_medallas.find():
    print(medalla)