# pistas.py
from abc import ABC, abstractmethod

class Pista(ABC):
    def __init__(self, id_pista, aforo_max, deporte):
        #Uso de _ para atributos privados/protegidos
        self._id_pista = id_pista
        self._aforo_max = aforo_max
        self._deporte = deporte
        self._estado = "Disponible" # Puede ser "Ocupada", "Mantenimiento"

    @property
    def id_pista(self):
        return self._id_pista

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

# esto obligará a las clases hijas a implementar el polimorfismo (sobrescribir)
    @abstractmethod
    def descripcion(self):
        pass

    def __str__(self):
        return f"Pista {self._id_pista} | {self._deporte.nombre} | Estado: {self._estado}"

#PistaInterior hereda de Pista
class PistaInterior(Pista):
    # aquí sobrescribimos el metodo de la clase padre
    def descripcion(self):
        return "Pista cubierta con iluminación artificial y parqué."

# PistaExterior hereda de Pista
class PistaExterior(Pista):
    # Sobrescribimos el metodo de la clase padre
    def descripcion(self):
        return "Pista al aire libre de cemento."