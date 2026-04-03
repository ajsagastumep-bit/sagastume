def promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def mayor(notas):
    mayor_nota = notas[0]
    for nota in notas:
        if nota > mayor_nota:
            mayor_nota = nota
    return mayor_nota

def menor(notas):
    menor_nota = notas[0]
    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota
    return menor_nota

def contar_aprobados(notas, minimo=61):
    contador = 0
    for nota in notas:
        if nota >= minimo:
            contador += 1
    return contador

def reporte(notas):
    print("Promedio:", promedio(notas))
    print("Mayor:", mayor(notas))
    print("Menor:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))


# Prueba
notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas)
