import json

ARCHIVO = "estudiantes.csv"

# =========================
# LEER CSV
# =========================
def leer_csv():
    estudiantes = []
    try:
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines()
            headers = lineas[0].strip().split(",")

            for linea in lineas[1:]:
                valores = linea.strip().split(",")
                estudiante = dict(zip(headers, valores))
                estudiantes.append(estudiante)

    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")

    return estudiantes


# =========================
# GUARDAR CSV
# =========================
def guardar_csv(estudiantes):
    with open(ARCHIVO, "w") as f:
        f.write("nombre,nota1,nota2,nota3\n")
        for e in estudiantes:
            f.write(f"{e['nombre']},{e['nota1']},{e['nota2']},{e['nota3']}\n")


# =========================
# MOSTRAR
# =========================
def mostrar(estudiantes):
    if not estudiantes:
        print("No hay estudiantes.")
        return

    for e in estudiantes:
        print(e)


# =========================
# AGREGAR
# =========================
def agregar(estudiantes):
    nombre = input("Nombre: ")

    if nombre == "":
        print("Nombre inválido")
        return

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        estudiantes.append({
            "nombre": nombre,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3
        })

        print("Estudiante agregado.")

    except ValueError:
        print("Error: debes ingresar números.")


# =========================
# BUSCAR
# =========================
def buscar(estudiantes):
    nombre = input("Nombre a buscar: ")

    for e in estudiantes:
        if e["nombre"] == nombre:
            print("Encontrado:", e)
            return

    print("No encontrado.")


# =========================
# ELIMINAR
# =========================
def eliminar(estudiantes):
    nombre = input("Nombre a eliminar: ")

    for e in estudiantes:
        if e["nombre"] == nombre:
            estudiantes.remove(e)
            print("Eliminado.")
            return

    print("No encontrado.")


# =========================
# ESTADÍSTICAS
# =========================
def estadisticas(estudiantes):
    if not estudiantes:
        print("No hay datos.")
        return

    mejor = None
    mejor_prom = 0

    for e in estudiantes:
        promedio = (float(e["nota1"]) + float(e["nota2"]) + float(e["nota3"])) / 3

        if promedio > mejor_prom:
            mejor_prom = promedio
            mejor = e["nombre"]

    print(f"Mejor estudiante: {mejor} con promedio {mejor_prom:.2f}")


# =========================
# EXPORTAR JSON
# =========================
def exportar_json(estudiantes):
    with open("reporte.json", "w") as f:
        json.dump(estudiantes, f, indent=4)

    print("Exportado a reporte.json")


# =========================
# MENÚ
# =========================
def menu():
    estudiantes = leer_csv()

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar estudiantes")
        print("2. Agregar")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Estadísticas")
        print("6. Exportar JSON")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar(estudiantes)

        elif opcion == "2":
            agregar(estudiantes)

        elif opcion == "3":
            buscar(estudiantes)

        elif opcion == "4":
            eliminar(estudiantes)

        elif opcion == "5":
            estadisticas(estudiantes)

        elif opcion == "6":
            exportar_json(estudiantes)

        elif opcion == "7":
            guardar_csv(estudiantes)
            print("Guardado. Adiós.")
            break

        else:
            print("Opción inválida")


# =========================
# EJECUTAR
# =========================
menu()
