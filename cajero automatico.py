def calcular_billetes(monto):
    if monto % 20 != 0:
        print("Error: el monto debe ser múltiplo de 20")
        return

    b200 = monto // 200
    monto = monto % 200

    b100 = monto // 100
    monto = monto % 100

    b50 = monto // 50
    monto = monto % 50

    b20 = monto // 20

    print("Billetes:")
    print("Q200:", b200)
    print("Q100:", b100)
    print("Q50:", b50)
    print("Q20:", b20)


# Prueba
calcular_billetes(360)
