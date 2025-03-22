class Paciente:
    def __init__(self, id_paciente, nombre, edad):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.enfermedades = []

    def Enfermedades(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def mostrar_informacion(self):
        print(f"Paciente ID: {self.id_paciente}, Nombre: {self.nombre}, Edad: {self.edad}")
        if self.enfermedades:
            print("Enfermedades asignadas:")
            for enfermedad in self.enfermedades:
                print(f"- {enfermedad.nombre} ({enfermedad.descripcion})")
        else:
            print("No tiene enfermedades asignadas.")


class Enfermedad:
    def __init__(self, id_enfermedad, nombre, descripcion):
        self.id_enfermedad = id_enfermedad
        self.nombre = nombre
        self.descripcion = descripcion


# Menú principal para interactuar
def menu():
    pacientes = {}
    enfermedades = {}

    while True:
        print("\n-------- Sistema de Gestión de Pacientes y Enfermedades --------")
        print("1. Registrar paciente")
        print("2. Registrar enfermedad")
        print("3. Asignar enfermedad a paciente")
        print("4. Mostrar información de un paciente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            id_paciente = input("Ingrese el ID del paciente: ")
            nombre = input("Ingrese el nombre del paciente: ")
            edad = input("Ingrese la edad del paciente: ")
            pacientes[id_paciente] = Paciente(id_paciente, nombre, edad)
            print("Paciente registrado con éxito.")

        elif opcion == "2":
            id_enfermedad = input("Ingrese el ID de la enfermedad: ")
            nombre = input("Ingrese el nombre de la enfermedad: ")
            descripcion = input("Ingrese la descripción de la enfermedad: ")
            enfermedades[id_enfermedad] = Enfermedad(id_enfermedad, nombre, descripcion)
            print("Enfermedad registrada con éxito.")

        elif opcion == "3":
            id_paciente = input("Ingrese el ID del paciente: ")
            id_enfermedad = input("Ingrese el ID de la enfermedad: ")

            if id_paciente in pacientes and id_enfermedad in enfermedades:
                paciente = pacientes[id_paciente]
                enfermedad = enfermedades[id_enfermedad]
                paciente.Enfermedad(enfermedad)
                print("Enfermedad asignada al paciente con éxito.")
            else:
                print("Error: ID de paciente o enfermedad no encontrado.")

        elif opcion == "4":
            id_paciente = input("Ingrese el ID del paciente: ")
            if id_paciente in pacientes:
                pacientes[id_paciente].mostrar_informacion()
            else:
                print("Error: Paciente no encontrado.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    menu()