
# Especialización para deportes colectivos (Fútbol, Baloncesto, etc.)
class DeporteEquipo(Deporte):
    def __init__(self, nombre, min_jugadores, duracion_oficial):
        super().__init__(nombre, min_jugadores)
        self.duracion_oficial = duracion_oficial

    def obtener_restricciones(self):
        #Genera un mensaje diciendo los minutos que duran los partidos de ese deporte
        return f"Equipos uniformados. Partidos oficiales de {self.duracion_oficial} minutos."


