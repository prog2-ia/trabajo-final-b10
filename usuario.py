class Usuario:
    def __init__(self, dni:str, nombre:str)->None:
        self._dni:str = dni
        self._nombre:str = nombre

    @property
    def nombre(self)->str:
        return self._nombre

    def __str__(self)->str:
        return f"Usuario[{self._dni}] - {self.nombre}"