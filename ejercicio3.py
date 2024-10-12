class Rutina:
    def __init__(self):
        self.actividades = []
        self.hora_inicio = 7 # 7:00 a.m.
    def agregar_actividad(self, actividad, tiempo):
        self.actividades.append((actividad, tiempo))
    def mostrar_rutina(self):
        hora_actual = self.hora_inicio
        for actividad, tiempo in self.actividades:
            print(f"{actividad}: {hora_actual}:00 - {hora_actual + tiempo}:00")
            hora_actual += tiempo
    def buscar_actividad(self, actividad):
        for act, tiempo in self.actividades:
            if act.lower() == actividad.lower():
                return f"{actividad} se realiza durante {tiempo} horas."
        return f"{actividad} no se encuentra en la rutina."
    def tiempo_total(self):
        total_horas = sum(tiempo for _, tiempo in self.actividades)
        return f"Tiempo total de actividades: {total_horas} horas."
    
        rutina = Rutina()
        rutina.agregar_actividad('Despertarse', 0.5)
        rutina.agregar_actividad('Ducharse', 0.5)
        rutina.agregar_actividad('Desayunar', 0.5)
        rutina.agregar_actividad('Leer', 1)
        rutina.agregar_actividad('Salir', 0.5)
        rutina.mostrar_rutina()
        actividad_buscar = input("Ingrese la actividad que desea buscar: ")
        resultado = rutina.buscar_actividad(actividad_buscar)
        print(resultado)
        print(rutina.tiempo_total()) 
