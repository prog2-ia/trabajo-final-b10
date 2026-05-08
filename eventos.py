class Evento:
    # Representa una reserva concreta de una pista.
    def __init__(self, id_evento: str, pista: 'Pista', usuario: 'Usuario', hora: str, num_jugadores: int, prioridad: int) -> None:
        self.id_evento: str = id_evento
        self.pista: 'Pista' = pista
        self.usuario: 'Usuario' = usuario
        self.hora: str = hora
        self.num_jugadores: int = num_jugadores
        self.prioridad: int = prioridad  # 1 (Liga/Alta), 2 (Normal/Baja))

    # Sobrecarga de operadores matemáticos: menor que (<)
    # esto nos permite saber cómo comparar y ordenar dos objetos Evento
    def __lt__(self, otro_evento:'Evento')->bool:
        return self.prioridad < otro_evento.prioridad

    def __str__(self)->str:
        tipo:str = "LIGA" if self.prioridad == 1 else "NORMAL"
        return f"{tipo} | Hora: {self.hora} | Pista {self.pista.id_pista} | A nombre de: {self.usuario.nombre}"


class Calendario:
#almacena diferentes eventos
    def __init__(self)->None:
        self.eventos: List['Evento'] = []

    def añadir_evento(self, evento:'Evento')->None:
        self.eventos.append(evento)
        # Al ordenar, se usa __lt__ de Evento
        self.eventos.sort()

    # Sobrecarga de operadores matemáticos: suma (+)
    # Permite fusionar dos calendarios en uno nuevo combinando sus listas
    def __add__(self, otro_calendario:'Calendario')->'Calendario':
        nuevo_calendario:'Calendario' = Calendario()
        nuevo_calendario.eventos = self.eventos + otro_calendario.eventos
        nuevo_calendario.eventos.sort()
        return nuevo_calendario


    def mostrar(self):
        print("-----CALENDARIO-----") # muestra el calendario completo
        if not self.eventos:
            print("No hay eventos programados.")
        for ev in self.eventos:
            print(ev)