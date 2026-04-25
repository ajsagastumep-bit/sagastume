

def leer_csv():
    estudiantes = []

    try:
        with open("alumnos.csv", "r") as f:
            lineas = f.readlines()

            headers = lineas[0].strip().split(",")

            for linea in lineas[1:]:
                valores = linea.strip().split(",")
                estudiante = dict(zip(headers, valores))
                estudiantes.append(estudiante)

        return estudiantes

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []


def calcular_promedios(estudiantes):
    mejor = None
    mejor_prom = 0

    for e in estudiantes:
        promedio = (float(e["nota1"]) + float(e["nota2"]) + float(e["nota3"])) / 3
        print(f"{e['nombre']} -> Promedio: {promedio:.2f}")

        if promedio > mejor_prom:
            mejor_prom = promedio
            mejor = e["nombre"]

    print(f"\nMejor estudiante: {mejor} con {mejor_prom:.2f}")


estudiantes = leer_csv()
calcular_promedios(estudiantes)
