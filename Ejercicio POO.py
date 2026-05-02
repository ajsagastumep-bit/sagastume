class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []  # lista vacía al inicio

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61


# Ejemplo de uso (para que pruebes)
est = Estudiante("Juan Pérez", "2026001", "Ingeniería")

est.agregar_nota(70)
est.agregar_nota(60)
est.agregar_nota(80)

print("Promedio:", est.promedio())
print("¿Aprobado?:", est.aprobado())
