def calcular_area_circulo(radio):
    """
    Calcula el area de un circulo.

    Args:
        radio (float): Radio del circulo.

    Returns:
        float: Area calculada con la formula pi * r^2.
    """
    pi = 3.1416
    return pi * radio ** 2

radio = float(input("Ingresa el radio del circulo: "))
area = calcular_area_circulo(radio)
print("El area del circulo es:", area)
