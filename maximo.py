def maximo_lista(lista):
    if len(lista) == 0:
        return None

    maximo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero

    return maximo

numeros = [3, 8, 2, 15, 6]
print("El maximo es:", maximo_lista(numeros))
