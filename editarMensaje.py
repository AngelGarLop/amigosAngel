from conexion import conectar
from bson import ObjectId

def editar_mensaje_motivacional(usuario_id):
    db = conectar()
    coleccion_usuarios = db["usuarios"]
    usuario = coleccion_usuarios.find_one({"_id": ObjectId(usuario_id)})

    # Verificar si el usuario es técnico
    if usuario["rol"] == "tecnico":
        coleccion_mensajes = db["mensajesMotivacionales"]

        # Obtener los mensajes creados por el usuario técnico
        mensajes = coleccion_mensajes.find({"id_usuario": usuario_id})

        # Si no hay mensajes, informamos al usuario
        if not mensajes:
            print("No tienes mensajes motivacionales para editar.")
            return

        # Mostrar los mensajes con un índice
        print("Lista de mensajes motivacionales creados:")
        mensaje_lista = list(mensajes)
        for idx, mensaje in enumerate(mensaje_lista):
            print(f"{idx + 1}. {mensaje['mensaje']}")

        # Pedir al usuario que seleccione el mensaje a editar
        try:
            seleccion = int(input("\nSelecciona el número del mensaje que deseas editar: "))
            if seleccion < 1 or seleccion > len(mensaje_lista):
                print("Selección inválida. Intenta nuevamente.")
                return

            # Obtener el mensaje seleccionado
            mensaje_a_editar = mensaje_lista[seleccion - 1]

            # Solicitar nuevo mensaje
            nuevo_mensaje = input(f"Edita el mensaje (actualmente: '{mensaje_a_editar['mensaje']}'): ")

            # Actualizar el mensaje en la base de datos
            coleccion_mensajes.update_one(
                {"_id": mensaje_a_editar["_id"]},
                {"$set": {
                    "mensaje": nuevo_mensaje,
                }}
            )

            print(f"El mensaje ha sido actualizado a: '{nuevo_mensaje}.")

        except ValueError:
            print("Entrada inválida. Debes seleccionar un número de la lista o proporcionar un rango válido.")

editar_mensaje_motivacional("63ea809051c7dd6fe6e45282")
