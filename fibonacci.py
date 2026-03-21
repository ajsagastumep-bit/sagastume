def primeros_fibonacci(n):
    serie = []
    a, b = 0, 1

    for i in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie

numero = int(input("Ingresa la cantidad de numeros Fibonacci: "))
print(primeros_fibonacci(numero))
