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




