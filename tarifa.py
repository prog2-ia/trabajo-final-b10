class Tarifa:
    def __init__(self, precio_hora):
        self.precio_hora = precio_hora

    @property
    def precio_hora(self):
        return self._precio_hora

    def calcular_precio(self, horas):
        return self._precio_hora * horas

    def _str_(self):
        return f"Tarifa {self._nombre}: {self._precio_hora}€/h"