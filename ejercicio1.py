class Rutina:
    def __init__(self):
        self.actividades = {}
    def agregar_actividad(self, actividad, tiempo):
        self.actividades[actividad] = tiempo
    def mostrar_rutina(self):
        for actividad, tiempo in self.actividades.items():
            print(f"{actividad}: {tiempo} horas")

rutina = Rutina()
rutina.agregar_actividad('levantarme', 1)
rutina.agregar_actividad('rezar', 0.5)
rutina.agregar_actividad('ducharme', 1)
rutina.agregar_actividad('desayunar', 1)
rutina.agregar_actividad('Salir', 0.5)
rutina.mostrar_rutina()