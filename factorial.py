def calcular_factorial(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial

numero = int(input("Ingresa un numero: "))
print("El factorial es:", calcular_factorial(numero))
