class Tarifa:
    def __init__(self, precio_hora, nombre):
        self._precio_hora = precio_hora
        self._nombre = nombre

    @property
    def precio_hora(self):
        return self._precio_hora

    def calcular_precio(self, horas):
        return self._precio_hora * horas

    def __str__(self):
        return f"Tarifa {self._nombre}: {self._precio_hora}€/h"