from conexion import conectar
from bson import ObjectId

def eliminar_todos_mensajes_usuario(usuario_id):
    db = conectar()
    coleccion_usuarios = db["usuarios"]
    usuario = coleccion_usuarios.find_one({"_id": ObjectId(usuario_id)})

    # Verificar si el usuario es técnico
    if usuario["rol"] == "tecnico":
        coleccion_mensajes = db["mensajesMotivacionales"]

        # Eliminar todos los mensajes del usuario técnico
        resultado = coleccion_mensajes.delete_many({"id_usuario": usuario_id})

        if resultado.deleted_count > 0:
            print(f"Se han eliminado {resultado.deleted_count} mensajes motivacionales del usuario.")
        else:
            print("No hay mensajes motivacionales para eliminar.")
    else:
        print("El usuario no tiene permisos para eliminar los mensajes.")

eliminar_todos_mensajes_usuario("63ea809051c7dd6fe6e45282")