def tabla(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def tablas_primos(limite):
    for n in range(2, limite + 1):
        if es_primo(n):
            print("Tabla del", n)
            tabla(n)
            print()


# Prueba
tablas_primos(10)
