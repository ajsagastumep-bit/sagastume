def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

grados = float(input("Ingresa los grados Celsius: "))
print("Grados Fahrenheit:", celsius_a_fahrenheit(grados))
