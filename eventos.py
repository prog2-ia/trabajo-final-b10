class Evento:
    # Representa una reserva concreta de una pista.
    def __init__(self, id_evento, pista, num_jugadores, prioridad):
        self.id_evento = id_evento
        self.pista = pista
        self.num_jugadores = num_jugadores
        self.prioridad = prioridad # 1 (Liga/Alta), 2 (Normal/Baja)

    # Sobrecarga de operadores matemáticos: menor que (<)
    # esto nos permite saber cómo comparar y ordenar dos objetos Evento
    def __lt__(self, otro_evento):
        return self.prioridad < otro_evento.prioridad

    def __str__(self):
        tipo = "LIGA" if self.prioridad == 1 else "NORMAL"
        return f"{tipo} | Hora: {self.hora} | Pista {self.pista.id_pista} | A nombre de: {self.usuario.nombre}"


