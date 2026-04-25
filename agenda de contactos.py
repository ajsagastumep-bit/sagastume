contactos = []

def agregar_contacto():
    nombre = input("Nombre: ")

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    telefono = input("Teléfono: ")
    email = input("Email: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    contactos.append(contacto)
    print("Contacto agregado correctamente.")

def buscar_contacto():
    nombre = input("Nombre a buscar: ")

    for contacto in contactos:
        if contacto.get("nombre") == nombre:
            print("Contacto encontrado:")
            print("Nombre:", contacto.get("nombre"))
            print("Teléfono:", contacto.get("telefono"))
            print("Email:", contacto.get("email"))
            return

    print("Contacto no encontrado.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos registrados.")
        return

    for contacto in contactos:
        print("-------------------")
        print("Nombre:", contacto.get("nombre"))
        print("Teléfono:", contacto.get("telefono"))
        print("Email:", contacto.get("email"))

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")

    for contacto in contactos:
        if contacto.get("nombre") == nombre:
            contactos.remove(contacto)
            print("Contacto eliminado.")
            return

    print("Contacto no encontrado.")

while True:
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
