class Deporte:
    def __init__(self, nombre, min_jugadores):
        self.nombre = nombre
        self.min_jugadores = min_jugadores

class DeporteRaqueta(Deporte): # Así se hereda
    def __init__(self, nombre, min_jugadores, necesita_red):
        super().__init__(nombre, min_jugadores)
        self.necesita_red = necesita_red

class DeporteEquipo(Deporte):
    def __init__(self, nombre, min_jugadores,duracion_oficial):
        super().__init__(nombre, min_jugadores)
        self.duracion_oficial = duracion_oficial

class Deporte_otro(Deporte):
    def __init__(self, nombre, min_jugadores):
        super().__init__(nombre,1)

class Tarifa:
    def __init__(self, precio_hora):
        self.precio_hora = precio_hora

    def calcular_precio(self, horas):
        return self.precio_hora * horas

class Pista:
    def __init__(self, id_pista, aforo_max, deporte):
        self.id_pista = id_pista
        self.aforo_max = aforo_max
        self.deporte = deporte
        self.estado = "Disponible" # Puede ser "Ocupada", "Mantenimiento"

class Evento:
    def __init__(self, id_evento, pista, num_jugadores, prioridad):
        self.id_evento = id_evento
        self.pista = pista
        self.num_jugadores = num_jugadores
        self.prioridad = prioridad # Ej: 1 (Liga), 2 (Normal)

    # SOBRECARGA: Sirve para PRIORIZAR eventos (usando el símbolo < )
    def __lt__(self, otro_evento):
        # Si usas evento1 < evento2, Python ejecutará esto:
        return self.prioridad < otro_evento.prioridad

class Calendario:
    def __init__(self):
        self.eventos = [] # Lista que guarda los eventos

    def añadir_evento(self, evento):
        # Aquí deberías usar un 'try/except' para lanzar las excepciones
        pass

    # SOBRECARGA: Sirve para COMBINAR calendarios (usando el símbolo + )
    def __add__(self, otro_calendario):
        nuevo_calendario = Calendario()
        nuevo_calendario.eventos = self.eventos + otro_calendario.eventos
        return nuevo_calendario
