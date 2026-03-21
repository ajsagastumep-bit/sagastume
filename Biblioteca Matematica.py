def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): radio del círculo

    Returns:
        float: área del círculo
    """
    return 3.1416 * radio * radio


def es_primo(a):
    """
    Dice si un número es primo.

    Args:
        a (int): número a evaluar

    Returns:
        bool: True si es primo, False si no
    """
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def factorial(n):
    """
    Calcula el factorial de un número.

    Args:
        n (int): número entero

    Returns:
        int: factorial de n
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def fibonacci(n):
    """
    Retorna los primeros números de Fibonacci.

    Args:
        n (int): cantidad de números

    Returns:
        list: lista de Fibonacci
    """
    lista = []
    a = 0
    b = 1
    for i in range(n):
        lista.append(a)
        temp = a + b
        a = b
        b = temp
    return lista


def celsius_a_fahrenheit(c):
    """
    Convierte Celsius a Fahrenheit.

    Args:
        c (float): temperatura en Celsius

    Returns:
        float: temperatura en Fahrenheit
    """
    return (c * 9 / 5) + 32


def maximo(lista):
    """
    Retorna el número mayor de una lista.

    Args:
        lista (list): lista de números

    Returns:
        int/float: número mayor
    """
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor


print(area_circulo(5))
print(es_primo(7))
print(factorial(5))
print(fibonacci(6))
print(celsius_a_fahrenheit(30))
print(maximo([2, 8, 3, 10, 5]))
