from abc import ABC, abstractmethod
class Deporte(ABC):
    def __init__(self, nombre, min_jugadores):
        self.nombre = nombre
        self.min_jugadores = min_jugadores

    # Aplicamos dos property para poder leer el nombre y mínimo de jugadores ya que son atributos privados
    @property
    def nombre(self):
        return self.nombre

    @property
    def min_jugadores(self):
        return self.min_jugadores

    # Aplicamos abstractmethod que tienen que cumplir todos los deportes
    @abstractmethod
    def obtener_restricciones(self):
        pass

    # Le meto esta función para imprimir los datos del deporte
    def _str_(self):
        return f"{self.nombre} (Min: {self.min_jugadores} jug.)"

class DeporteRaqueta(Deporte):  # Así se hereda
    def __init__(self, nombre, min_jugadores, necesita_red):
        super().__init__(nombre, min_jugadores)
        self.necesita_red = necesita_red

    def obtener_restricciones(self):
        estado_red = "con red" if self._necesita_red else "sin red"
        return f"Obligatorio traer raquetas propias. Se juega {estado_red}."

class DeporteEquipo(Deporte):
    def __init__(self, nombre, min_jugadores, duracion_oficial):
        super().__init__(nombre, min_jugadores)
        self.duracion_oficial = duracion_oficial

    def obtener_restricciones(self):
        return f"Equipos uniformados. Partidos oficiales de {self._duracion_oficial} minutos."


class Deporte_otro(Deporte):
    def __init__(self, nombre, min_jugadores):
        super().__init__(nombre, 1)
