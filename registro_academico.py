class RegistroAcademico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
    def agregar_nota(self, nota):
        if 0 <= nota <= 5:
            self.notas.append(nota)
            print("nota agregada correctamente.\n")
        else:
            print("la nota debe estar entre 0 y 5.\n")
    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    def estado(self):
        promedio = self.calcular_promedio()
        return "aprobado" if promedio >= 3 else "reprobado"
    def mostrar_reporte(self):
        print(f"\n reporte academico")
        print(f"estudiante: {self.nombre}")
        if not self.notas:
            print("no hay notas registradas.")
        else:
            print("notas:", ", ".join(str(nota) for nota in self.notas))
            print(f"promedio: {self.calcular_promedio():.2f}")
            print(f"estado: {self.estado()}")
        print()
def menu():
    nombre = input("ingrese el nombre del estudiante: ")
    registro = RegistroAcademico(nombre)
    while True:
        print("registro academico")
        print("1. agregar nota")
        print("2. mostrar reporte")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            try:
                nota = float(input("ingrese la nota (0 - 5): "))
                registro.agregar_nota(nota)
            except ValueError:
                print("debe ingresar un numero valido.\n")
        elif opcion == "2":
            registro.mostrar_reporte()
        elif opcion == "3":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()