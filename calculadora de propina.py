def calcular_propina(subtotal, porcentaje):
    return subtotal * porcentaje / 100

def calcular_total(subtotal, propina):
    return subtotal + propina

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: la cantidad de personas debe ser mayor que 0"
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    descuento = subtotal * descuento_pct / 100
    return subtotal - descuento

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Calcular propina")
    print("2. Dividir la cuenta")
    print("3. Aplicar descuento + propina")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            subtotal = float(input("Ingresa el subtotal: "))
            porcentaje = float(input("Ingresa el porcentaje de propina: "))
            propina = calcular_propina(subtotal, porcentaje)
            total = calcular_total(subtotal, propina)
            print("Propina:", propina)
            print("Total a pagar:", total)

        elif opcion == "2":
            total = float(input("Ingresa el total: "))
            personas = int(input("¿Entre cuántas personas?: "))
            print("Cada persona paga:", dividir_cuenta(total, personas))

        elif opcion == "3":
            subtotal = float(input("Ingresa el subtotal: "))
            descuento = float(input("Ingresa el descuento (%): "))
            porcentaje = float(input("Ingresa el porcentaje de propina: "))

            nuevo_subtotal = aplicar_descuento(subtotal, descuento)
            propina = calcular_propina(nuevo_subtotal, porcentaje)
            total = calcular_total(nuevo_subtotal, propina)

            print("Subtotal con descuento:", nuevo_subtotal)
            print("Propina:", propina)
            print("Total a pagar:", total)

        elif opcion == "4":
            print("Programa finalizado")
            break

        else:
            print("Opción no válida")

main()
