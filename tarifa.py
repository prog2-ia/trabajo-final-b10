class Tarifa:
    def __init__(self, nombre:str, precio_hora:float)->None:
        self._precio_hora:str = precio_hora
        self._nombre:str = nombre

    @property
    def precio_hora(self)->float:
        return self._precio_hora

    def calcular_precio(self, horas:float)->float:
        return float(self._precio_hora) * horas

    def __str__(self)->str:
        return f"Tarifa {self._nombre}: {self._precio_hora}€/h"