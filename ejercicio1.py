class Rutina:
    def __init__(self):
        self.actividades = {}
    def agregar_actividad(self, actividad, tiempo):
        self.actividades[actividad] = tiempo
    def mostrar_rutina(self):
        for actividad, tiempo in self.actividades.items():
            print(f"{actividad}: {tiempo} horas")

rutina = Rutina()
rutina.agregar_actividad('Despertarse', 0.5)
rutina.agregar_actividad('Ducharse', 0.5)
rutina.agregar_actividad('Desayunar', 0.5)
rutina.agregar_actividad('Leer', 1)
rutina.agregar_actividad('Salir', 0.5)
rutina.mostrar_rutina()