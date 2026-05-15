class PrioridadException(Exception):
    """Excepción lanzada cuando la prioridad de un evento no está en el rango permitido."""
    pass

class Evento:
    # Representa una reserva concreta de una pista.
    def __init__(self, id_evento: str, pista: 'Pista', usuario: 'Usuario', hora: str, num_jugadores: int, prioridad: int) -> None:
        # Validamos que el número de jugadores tenga sentido lógico
        if num_jugadores <= 0:
            raise ValueError(f"El número de jugadores debe ser mayor a 0. Se recibió: {num_jugadores}")

        # Validamos que la prioridad sea estrictamente 1 o 2 con nuestra excepción personalizada
        if prioridad not in (1, 2):
            raise PrioridadException(f"La prioridad debe ser 1 (Liga/Alta) o 2 (Normal/Baja). Se r# Validamos que el número de jugadores tenga sentido lógico
        if num_jugadores <= 0:
            raise ValueError(f"El número de jugadores debe ser mayor a 0. Se recibió: {num_jugadores}")

        # Validamos que la prioridad sea estrictamente 1 o 2 con nuestra excepción personalizada
        if prioridad not in (1, 2):
            raise PrioridadException(f"La prioridad debe ser 1 (Liga/Alta) o 2 (Normal/Baja). Se recibió: {prioridad}")ecibió: {prioridad}")

        self.id_evento: str = id_evento
        self.pista: 'Pista' = pista
        self.usuario: 'Usuario' = usuario
        self.hora: str = hora
        self.num_jugadores: int = num_jugadores
        self.prioridad: int = prioridad  # 1 (Liga/Alta), 2 (Normal/Baja))

    # Sobrecarga de operadores matemáticos: menor que (<)
    # esto nos permite saber cómo comparar y ordenar dos objetos Evento
    def __lt__(self, otro_evento:'Evento')->bool:
        # Afirmamos que se cumple una determinada condición antes de proceder
        assert hasattr(otro_evento, 'prioridad'), "El objeto a comparar no tiene un atributo 'prioridad' definido."
        return self.prioridad < otro_evento.prioridad

    def __str__(self)->str:
        tipo:str = "LIGA" if self.prioridad == 1 else "NORMAL"
        return f"{tipo} | Hora: {self.hora} | Pista {self.pista.id_pista} | A nombre de: {self.usuario.nombre}"


