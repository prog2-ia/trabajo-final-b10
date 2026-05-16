# pistas.py
from abc import ABC, abstractmethod
from deporte import Deporte

class Pista(ABC):
    def __init__(self, id_pista: str, aforo_max: int, deporte: 'Deporte') -> None:
        # Validación para que el aforo tenga sentido físico
        if aforo_max <= 0:
            raise ValueError(f"El aforo máximo debe ser mayor que 0. Se recibió: {aforo_max}")

        #Uso de _ para atributos privados/protegidos
        self._id_pista:str = id_pista
        self._aforo_max:int = aforo_max
        self._deporte:'Deporte' = deporte
        self._estado:str = "Disponible" # Puede ser "Ocupada", "Mantenimiento"

    @property
    def id_pista(self)->str:
        return self._id_pista

    @property
    def deporte(self) -> 'Deporte':
        return self._deporte

    @property
    def estado(self)->str:
        return self._estado

    @estado.setter
    def estado(self, valor:str)->None:
        self._estado = valor

# esto obligará a las clases hijas a implementar el polimorfismo (sobrescribir)
    @abstractmethod
    def descripcion(self)->str:
        pass

    def __str__(self)->str:
        return f"Pista {self._id_pista} | {self._deporte.nombre} | Estado: {self._estado}"

#PistaInterior hereda de Pista
class PistaInterior(Pista):
    # aquí sobrescribimos el metodo de la clase padre
    def descripcion(self)->str:
        return "Pista cubierta con iluminación artificial y parqué."

# PistaExterior hereda de Pista
class PistaExterior(Pista):
    # Sobrescribimos el metodo de la clase padre
    def descripcion(self)->str:
        return "Pista al aire libre de cemento."