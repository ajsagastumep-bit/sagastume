def cifrar_caracter(c, desplazamiento):
    if c.isalpha():
        if c.islower():
            base = ord('a')
        else:
            base = ord('A')

        posicion = ord(c) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)
    else:
        return c

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)


# Prueba
texto = cifrar_mensaje("hola", 3)
print("Cifrado:", texto)
print("Descifrado:", descifrar_mensaje(texto, 3))
