class Evento:
    # Representa una reserva concreta de una pista.
    def __init__(self, id_evento: str, pista: 'Pista', usuario: 'Usuario', hora: str, num_jugadores: int, prioridad: int) -> None:
        self.id_evento: str = id_evento
        self.pista: 'Pista' = pista
        self.usuario: 'Usuario' = usuario
        self.hora: str = hora
        self.num_jugadores: int = num_jugadores
        self.prioridad: int = prioridad  # 1 (Liga/Alta), 2 (Normal/Baja))

    # Sobrecarga de operadores matemáticos: menor que (<)
    # esto nos permite saber cómo comparar y ordenar dos objetos Evento
    def __lt__(self, otro_evento:'Evento')->bool:
        return self.prioridad < otro_evento.prioridad

    def __str__(self)->str:
        tipo:str = "LIGA" if self.prioridad == 1 else "NORMAL"
        return f"{tipo} | Hora: {self.hora} | Pista {self.pista.id_pista} | A nombre de: {self.usuario.nombre}"


