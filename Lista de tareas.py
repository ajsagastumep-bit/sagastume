tareas = []

while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append({"nombre": tarea, "completada": False})
        print("Tarea agregada")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            for i, t in enumerate(tareas, 1):
                estado = "✓ Completada" if t["completada"] else "Pendiente"
                print(f"{i}. {t['nombre']} - {estado}")

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar")
        else:
            idx = int(input("Número de tarea a eliminar: "))
            if 1 <= idx <= len(tareas):
                tareas.pop(idx - 1)
                print("Tarea eliminada")
            else:
                print("Número inválido")

    elif opcion == "4":
        if len(tareas) == 0:
            print("No hay tareas para marcar")
        else:
            idx = int(input("Número de tarea completada: "))
            if 1 <= idx <= len(tareas):
                tareas[idx - 1]["completada"] = True
                print("Tarea marcada como completada")
            else:
                print("Número inválido")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")
