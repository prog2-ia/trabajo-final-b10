# Clase para deportes que no encajan en las categorías anteriores
class Deporte_otro(Deporte):
    def __init__(self, nombre, min_jugadores):
        super().__init__(nombre, 1)