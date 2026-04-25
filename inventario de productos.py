import json

inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        inventario.append(producto)
        print("Producto agregado correctamente.")

    except ValueError:
        print("Error: precio o cantidad inválida.")

def buscar_producto():
    dato = input("Buscar por nombre o categoría: ")

    encontrado = False

    for producto in inventario:
        if producto.get("nombre") == dato or producto.get("categoria") == dato:
            print(producto)
            encontrado = True

    if not encontrado:
        print("No se encontraron productos.")

def actualizar_cantidad():
    nombre = input("Producto a actualizar: ")

    for producto in inventario:
        if producto.get("nombre") == nombre:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                producto["cantidad"] = nueva_cantidad
                print("Cantidad actualizada.")
                return
            except ValueError:
                print("Cantidad inválida.")
                return

    print("Producto no encontrado.")

def valor_total():
    total = 0

    for producto in inventario:
        total += producto.get("precio") * producto.get("cantidad")

    print("Valor total del inventario:", total)

def stock_bajo():
    print("Productos con stock bajo:")

    for producto in inventario:
        if producto.get("cantidad") < 5:
            print(producto)

def exportar_json():
    json_string = json.dumps(inventario, indent=4)
    print(json_string)

while True:
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Buscar por nombre o categoría")
    print("3. Actualizar cantidad")
    print("4. Calcular valor total")
    print("5. Mostrar stock bajo")
    print("6. Exportar como JSON")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        actualizar_cantidad()
    elif opcion == "4":
        valor_total()
    elif opcion == "5":
        stock_bajo()
    elif opcion == "6":
        exportar_json()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
