class PrecioInvalidoException(Exception):
    """Excepción lanzada cuando se intenta asignar un precio negativo a una tarifa."""
    pass

class Tarifa:
    def __init__(self, nombre:str, precio_hora:float)->None:
        self._nombre:str = nombre
        # Intentamos forzar la conversión a float por seguridad
        try:
            precio_validado = float(precio_hora)
        except ValueError as error:
            # Capturamos el ValueError ( Raised when there is a wrong value in a specified data type )
            # y lanzamos uno más descriptivo.
            raise ValueError(f"El precio por hora debe ser un valor numérico. Detalle del error: {error}")

        # Validamos con nuestra excepción personalizada que el precio no sea negativo
        if precio_validado < 0:
            raise PrecioInvalidoException(f"El precio por hora no puede ser negativo. Se recibió: {precio_validado}")

        self._precio_hora: float = precio_validado

    @property
    def precio_hora(self)->float:
        return self._precio_hora

    def calcular_precio(self, horas:float)->float:
        # Afirmamos que se cumple una determinada condición: que 'horas' sea int o float
        assert isinstance(horas, (int,
                                  float)), f"La cantidad de horas debe ser numérica. Se recibió un tipo '{type(horas).__name__}'."

        # Generamos un ValueError tradicional si las horas son negativas
        if horas < 0:
            raise ValueError(f"Las horas calculadas no pueden ser negativas. Se recibió: {horas}")

        return self._precio_hora * horas

    def __str__(self)->str:
        return f"Tarifa {self._nombre}: {self._precio_hora}€/h"