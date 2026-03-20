class Usuario:
    def _init_(self, dni, nombre):
        self._dni = dni
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def _str_(self):
        return f"Usuario[{self._dni}] - {self.nombre}"