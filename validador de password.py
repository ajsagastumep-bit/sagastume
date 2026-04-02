def validar_password(password):
    especiales = "!@#$%"
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    if len(password) < 8:
        return False

    for c in password:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True
        if c in especiales:
            tiene_especial = True

    return tiene_mayuscula and tiene_numero and tiene_especial


def diagnosticar_password(password):
    especiales = "!@#$%"
    tiene_mayuscula = False
    tiene_numero = False
    tiene_especial = False

    if len(password) < 8:
        print("Falla: debe tener mínimo 8 caracteres")

    for c in password:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True
        if c in especiales:
            tiene_especial = True

    if not tiene_mayuscula:
        print("Falla: le falta una mayúscula")
    if not tiene_numero:
        print("Falla: le falta un número")
    if not tiene_especial:
        print("Falla: le falta un carácter especial")

    if validar_password(password):
        print("La contraseña sí cumple")


# Pruebas
print(validar_password("Hola123!"))
diagnosticar_password("hola12")
