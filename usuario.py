class Usuario:
    def __init__(self, dni, nombre):
        self._dni = dni
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return f"Usuario[{self._dni}] - {self.nombre}"