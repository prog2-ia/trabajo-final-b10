# Especialización para deportes que usan raqueta (Tenis, Padel, etc.)
class DeporteRaqueta(Deporte):  # Así se hereda
    def __init__(self, nombre, min_jugadores, necesita_red):
        super().__init__(nombre, min_jugadores)
        self.necesita_red = necesita_red

    def obtener_restricciones(self):
        # Genera un mensaje dinámico basado en si el deporte requiere red o no
        estado_red = "con red" if self.necesita_red else "sin red"
        return f"Obligatorio traer raquetas propias. Se juega {estado_red}."


