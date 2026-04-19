# 1. Crear una tupla con las coordenadas de tu ciudad
coordenadas = (14.0833, -90.3833)

# 2. Desempaquetar en variables lat, lon
lat, lon = coordenadas
print("Latitud:", lat)
print("Longitud:", lon)


# 3. Función que retorna (min, max, promedio)
def calcular_estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio


# Probar la función
numeros = [10, 20, 30, 40, 50]
minimo, maximo, promedio = calcular_estadisticas(numeros)

print("\nEstadísticas:")
print("Min:", minimo)
print("Max:", maximo)
print("Promedio:", promedio)


# 4. Tuplas como claves de diccionario
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

print("\nDistancias:")
for ruta, km in distancias.items():
    print(ruta, "=", km, "km")


# 5. Intentar modificar una tupla (capturando el error)
try:
    coordenadas[0] = 15.0
except TypeError:
    print("\nError: No se puede modificar una tupla")
    print("# Las tuplas son inmutables")
