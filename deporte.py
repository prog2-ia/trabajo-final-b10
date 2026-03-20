from abc import ABC, abstractmethod
#Importamos abc para trabajar con clases abstractas

class Deporte(ABC): # Clase base que define la estructura común para todos los deportes
    def __init__(self, nombre, min_jugadores):
        self._nombre = nombre
        self._min_jugadores = min_jugadores

    # Aplicamos dos property para poder leer el nombre y mínimo de jugadores ya que son atributos privados
    @property
    def nombre(self):
        return self._nombre

    @property
    def min_jugadores(self):
        return self._min_jugadores

    # Aplicamos abstractmethod que tienen que cumplir todos los deportes
    @abstractmethod
    def obtener_restricciones(self):
        pass

    #Utilizamos esta función para imprimir los datos del deporte
    def __str__(self):
        return f"{self._nombre} (Min: {self._min_jugadores} jug.)"


# Especialización para deportes que usan raqueta (Tenis, Padel, etc.)
class DeporteRaqueta(Deporte):  # Así se hereda
    def __init__(self, nombre, min_jugadores, necesita_red):
        super().__init__(nombre, min_jugadores)
        self.necesita_red = necesita_red

    def obtener_restricciones(self):
        # Genera un mensaje dinámico basado en si el deporte requiere red o no
        estado_red = "con red" if self.necesita_red else "sin red"
        return f"Obligatorio traer raquetas propias. Se juega {estado_red}."



# Especialización para deportes colectivos (Fútbol, Baloncesto, etc.)
class DeporteEquipo(Deporte):
    def __init__(self, nombre, min_jugadores, duracion_oficial):
        super().__init__(nombre, min_jugadores)
        self.duracion_oficial = duracion_oficial

    def obtener_restricciones(self):
        #Genera un mensaje diciendo los minutos que duran los partidos de ese deporte
        return f"Equipos uniformados. Partidos oficiales de {self.duracion_oficial} minutos."



# Clase para deportes que no encajan en las categorías anteriores
class Deporte_otro(Deporte):
    def __init__(self, nombre, min_jugadores):
        super().__init__(nombre, 1)
