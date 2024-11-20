def mensaje_final_sesion(usuario_id):
    # Obtener la información del usuario
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})
    
    # Generar el mensaje final
    if usuario['cant_audios'] < 5:
        mensaje_final = "¡Buen inicio! Aún tienes mucho por descubrir, ¡sigue practicando y mejorando!"
    elif 5 <= usuario['cant_audios'] < 15:
        mensaje_final = "¡Vas muy bien! Te está quedando todo cada vez más claro, sigue así."
    else:
        mensaje_final = "¡Excelente trabajo! Has demostrado una gran dedicación. ¡Sigue adelante!"
    
    # Agregar un mensaje empático si tiene alguna condición médica
    if "Ictus" in usuario.get('enfermedades', []) or "Disfonía" in usuario.get('dis', []):
        mensaje_final += " Sabemos que no es fácil, pero tu esfuerzo es admirable. ¡Sigue trabajando en tu mejoría!"
    
    # Mostrar el mensaje final
    print(mensaje_final)
