# Función 1: Crear diccionario
def crear_diccionario():
    nombre = input("Ingresa tu nombre: ")
    
    # Validación de edad
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa")
            else:
                break
        except:
            print("Ingresa un número válido")
    
    ciudad = input("Ingresa tu ciudad: ")
    lenguaje = input("Lenguaje favorito: ")

    persona = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "lenguaje_favorito": lenguaje
    }
    return persona


# Función 2: Agregar universidad
def agregar_universidad(diccionario):
    universidad = input("Ingresa tu universidad: ")
    diccionario["universidad"] = universidad
    return diccionario


# Función 3: Modificar edad
def modificar_edad(diccionario):
    nueva_edad = int(input("Nueva edad: "))
    diccionario["edad"] = nueva_edad


# Función 4: Mostrar diccionario
def mostrar_datos(diccionario):
    print("\n--- Datos ---")
    for clave, valor in diccionario.items():
        print(clave, ":", valor)


# Función 5: Verificar email
def verificar_email(diccionario):
    if "email" in diccionario:
        print("El email existe")
    else:
        print("El email NO existe")


# Función 6: Obtener teléfono sin error
def obtener_telefono(diccionario):
    telefono = diccionario.get("telefono", "No hay teléfono registrado")
    print("Teléfono:", telefono)


# Programa principal
def main():
    persona = crear_diccionario()
    persona = agregar_universidad(persona)
    modificar_edad(persona)
    mostrar_datos(persona)
    verificar_email(persona)
    obtener_telefono(persona)


# Ejecutar programa
main()
