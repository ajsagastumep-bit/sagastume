def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()

    if origen == destino:
        return valor

    if origen == "C":
        c = valor
    elif origen == "F":
        c = fahrenheit_a_celsius(valor)
    elif origen == "K":
        c = kelvin_a_celsius(valor)
    else:
        return None

    if destino == "C":
        return c
    elif destino == "F":
        return celsius_a_fahrenheit(c)
    elif destino == "K":
        return celsius_a_kelvin(c)
    else:
        return None


# Pruebas
print(convertir(25, "C", "F"))
print(convertir(98, "F", "C"))
print(convertir(30, "C", "K"))
