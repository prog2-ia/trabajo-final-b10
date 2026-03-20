class Evento:
    # Representa una reserva concreta de una pista.
    def __init__(self, id_evento, pista, num_jugadores, prioridad):
        self.id_evento = id_evento
        self.pista = pista
        self.num_jugadores = num_jugadores
        self.prioridad = prioridad # 1 (Liga/Alta), 2 (Normal/Baja)

    # Sobrecarga de operadores matemáticos: menor que (<)
    # esto nos permite saber cómo comparar y ordenar dos objetos Evento
    def __lt__(self, otro_evento):
        return self.prioridad < otro_evento.prioridad

    def __str__(self):
        tipo = "LIGA" if self.prioridad == 1 else "NORMAL"
        return f"{tipo} | Hora: {self.hora} | Pista {self.pista.id_pista} | A nombre de: {self.usuario.nombre}"


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