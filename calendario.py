class Calendario:
#almacena diferentes eventos
    def __init__(self):
        self.eventos = []

    def añadir_evento(self, evento):
        self.eventos.append(evento)
        # Al ordenar, se usa __lt__ de Evento
        self.eventos.sort()

    # Sobrecarga de operadores matemáticos: suma (+)
    # Permite fusionar dos calendarios en uno nuevo combinando sus listas
    def __add__(self, otro_calendario):
        nuevo_calendario = Calendario()
        nuevo_calendario.eventos = self.eventos + otro_calendario.eventos
        nuevo_calendario.eventos.sort()
        return nuevo_calendario


    def mostrar(self):
        print("-----CALENDARIO-----")
        if not self.eventos:
            print("No hay eventos programados.")
        for ev in self.eventos:
            print(ev)