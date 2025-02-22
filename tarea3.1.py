class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {horario}.")

    def __str__(self):
        return f"Conductor: {self.nombre}, Horarios: {self.horarios}"


class Buses:
    def __init__(self, numero):
        self.numero = numero
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
        else:
            print(f"El bus {self.numero} ya tiene asignado el horario {horario}.")

    def asignar_conductor(self, conductor):
        if self.conductor_asignado is None:
            for horario in self.horarios:
                if horario in conductor.horarios:
                    print(f"El conductor {conductor.nombre} ya tiene asignado el horario {horario}.")
                    return
            self.conductor_asignado = conductor
            for horario in self.horarios:
                conductor.agregar_horario(horario)
            print(f"Conductor {conductor.nombre} asignado al bus {self.numero}.")
        else:
            print(f"El bus {self.numero} ya tiene un conductor asignado.")

    def __str__(self):
        return f"Bus: {self.numero}, Ruta: {self.ruta}, Horarios: {self.horarios}, Conductor: {self.conductor_asignado.nombre if self.conductor_asignado else 'No asignado'}"


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, numero):
        bus = Buses(numero)
        self.buses.append(bus)
        print(f"Bus {numero} agregado.")

    def agregar_ruta_a_bus(self, numero_bus, ruta):
        bus = self._buscar_bus(numero_bus)
        if bus:
            bus.agregar_ruta(ruta)
            print(f"Ruta {ruta} agregada al bus {numero_bus}.")
        else:
            print(f"Bus {numero_bus} no encontrado.")

    def registrar_horario_a_bus(self, numero_bus, horario):
        bus = self._buscar_bus(numero_bus)
        if bus:
            bus.agregar_horario(horario)
            print(f"Horario {horario} agregado al bus {numero_bus}.")
        else:
            print(f"Bus {numero_bus} no encontrado.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado.")

    def agregar_horario_a_conductor(self, nombre_conductor, horario):
        conductor = self._buscar_conductor(nombre_conductor)
        if conductor:
            conductor.agregar_horario(horario)
            print(f"Horario {horario} agregado al conductor {nombre_conductor}.")
        else:
            print(f"Conductor {nombre_conductor} no encontrado.")

    def asignar_bus_a_conductor(self, numero_bus, nombre_conductor):
        bus = self._buscar_bus(numero_bus)
        conductor = self._buscar_conductor(nombre_conductor)
        if bus and conductor:
            bus.asignar_conductor(conductor)
        else:
            print(f"Bus {numero_bus} o conductor {nombre_conductor} no encontrado.")

    def _buscar_bus(self, numero_bus):
        for bus in self.buses:
            if bus.numero == numero_bus:
                return bus
        return None

    def _buscar_conductor(self, nombre_conductor):
        for conductor in self.conductores:
            if conductor.nombre == nombre_conductor:
                return conductor
        return None

    def mostrar_buses(self):
        for bus in self.buses:
            print(bus)

    def mostrar_conductores(self):
        for conductor in self.conductores:
            print(conductor)


def menu():
    admin = Admin()
    while True:
        print("\n--- Menú de Gestión de Buses ---")
        print("1. Agregar Bus")
        print("2. Agregar Ruta a Bus")
        print("3. Registrar Horario a Bus")
        print("4. Agregar Conductor")
        print("5. Agregar Horario a Conductor")
        print("6. Asignar Bus a Conductor")
        print("7. Mostrar Buses")
        print("8. Mostrar Conductores")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_bus = input("Ingrese el número del bus: ")
            admin.agregar_bus(numero_bus)
        elif opcion == "2":
            numero_bus = input("Ingrese el número del bus: ")
            ruta = input("Ingrese la ruta: ")
            admin.agregar_ruta_a_bus(numero_bus, ruta)
        elif opcion == "3":
            numero_bus = input("Ingrese el número del bus: ")
            horario = input("Ingrese el horario (formato HH:MM): ")
            admin.registrar_horario_a_bus(numero_bus, horario)
        elif opcion == "4":
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            admin.agregar_conductor(nombre_conductor)
        elif opcion == "5":
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            horario = input("Ingrese el horario (formato HH:MM): ")
            admin.agregar_horario_a_conductor(nombre_conductor, horario)
        elif opcion == "6":
            numero_bus = input("Ingrese el número del bus: ")
            nombre_conductor = input("Ingrese el nombre del conductor: ")
            admin.asignar_bus_a_conductor(numero_bus, nombre_conductor)
        elif opcion == "7":
            admin.mostrar_buses()
        elif opcion == "8":
            admin.mostrar_conductores()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()