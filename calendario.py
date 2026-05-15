class Calendario:
#almacena diferentes eventos
    def __init__(self)->None:
        self.eventos: List['Evento'] = []

    def añadir_evento(self, evento:'Evento')->None:
        #Verificamos que el objeto es de la clase correcta
        #para seguir.
        assert type(evento).__name__ == 'Evento', f"Se esperaba un objeto 'Evento', se recibió '{type(evento).__name__}'"

        self.eventos.append(evento)

        try:
            # Al ordenar, se usa __lt__ de Evento
            self.eventos.sort()
        except TypeError as error:
            #TypeError sale si tratamos de comparar/ ordenar tipos incompatibles
            self.eventos.pop()
            print("Error: No se puede ordenar el calendario porque el evento no es comparable.")
            raise
            # Relanzamos la excepción para que el programa principal decida qué hacer

    # Sobrecarga de operadores matemáticos: suma (+)
    # Permite fusionar dos calendarios en uno nuevo combinando sus listas
    def __add__(self, otro_calendario:'Calendario')->'Calendario':
        try:
            # Intentamos acceder al atributo eventos. Si no existe, fallará
            eventos_combinados = self.eventos + otro_calendario.eventos

        except AttributeError:
            # Levantamos un TypeError explicando que los tipos no son compatibles para la suma.
            raise TypeError(f"No se puede sumar un objeto 'Calendario' con un objeto '{type(otro_calendario).__name__}'")

        nuevo_calendario:'Calendario' = Calendario()
        nuevo_calendario.eventos = self.eventos + otro_calendario.eventos

        try:
            nuevo_calendario.eventos.sort()
        except TypeError:
            print("Error interno: Inconsistencia de tipos al intentar ordenar el calendario fusionado.")
            raise

        return nuevo_calendario


    def mostrar(self)->None:
        print("-----CALENDARIO-----") # muestra el calendario completo
        if not self.eventos:
            print("No hay eventos programados.")
        for ev in self.eventos:
            print(ev)