class GrafoMusical:
    def __init__(self):
        self.grafo = {}

    def agregar_cancion(self, cancion):
        if cancion not in self.grafo:
            self.grafo[cancion] = []

    def agregar_transicion(self, cancion_origen, cancion_destino):
        if cancion_origen in self.grafo and cancion_destino in self.grafo:
            self.grafo[cancion_origen].append(cancion_destino)

    def mostrar_grafo(self):
        for cancion, transiciones in self.grafo.items():
            print(f"{cancion} pertenece a: {', '.join(transiciones) if transiciones else 'Ninguna'}")
            
    def buscar_cancion(self, cancion):
        if cancion in self.grafo:
            transiciones = self.grafo[cancion]
            return f"{cancion} pertenece a: {', '.join(transiciones) if transiciones else 'Ninguna'}"
        return f"{cancion} no se encuentra en el grafo."
    
    """
reproductor = GrafoMusical()
reproductor.agregar_cancion('Comestibles')
reproductor.agregar_cancion('Tomate')
reproductor.agregar_cancion('Melon')
reproductor.agregar_cancion('Manzana')
reproductor.agregar_transicion('Tomate', 'Comestibles')
reproductor.agregar_transicion('Melon', 'Comestibles')
reproductor.agregar_transicion('Manzana', 'Comestibles')
"""


reproductor = GrafoMusical()
reproductor.agregar_cancion('Utensilios')
reproductor.agregar_cancion('Colador')
reproductor.agregar_cancion('Tenedor')
reproductor.agregar_cancion('Espatula')
reproductor.agregar_transicion('Colador', 'Utensilios')
reproductor.agregar_transicion('Tenedor', 'Utensilios')
reproductor.agregar_transicion('Espatula', 'Utensilios')

"""
reproductor = GrafoMusical()
reproductor.agregar_cancion('Limpieza')
reproductor.agregar_cancion('Rinso')
reproductor.agregar_cancion('Jabon')
reproductor.agregar_cancion('Paste')
reproductor.agregar_transicion('Rinso', 'Limpieza')
reproductor.agregar_transicion('Jabon', 'Limpieza')
reproductor.agregar_transicion('Paste', 'Limpieza')
"""
reproductor.mostrar_grafo()
cancion_buscar = input("Ingrese el nombre del articulo que desea buscar:")
resultado = reproductor.buscar_cancion(cancion_buscar)
print(resultado)