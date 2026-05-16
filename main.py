from pista import Pista, PistaInterior, PistaExterior
from eventos import Evento
from calendario import Calendario
from tarifa import Tarifa
from usuario import Usuario
from deporte import DeporteRaqueta, DeporteEquipo
import random

def main() -> None:
    print("----- SISTEMA DE RESERVAS DE PISTAS DEPORTIVAS -----\n")
    # Creamos diferentes deportes.
    tenis: DeporteRaqueta = DeporteRaqueta("Tenis", min_jugadores=2, necesita_red=True)
    padel: DeporteRaqueta = DeporteRaqueta("Padel", min_jugadores=2, necesita_red=True)
    baloncesto: DeporteEquipo = DeporteEquipo("Baloncesto", min_jugadores=10, duracion_oficial=40)
    futbol_sala: DeporteEquipo = DeporteEquipo("Futbol sala", min_jugadores=10, duracion_oficial=40)
    voleibol: DeporteEquipo = DeporteEquipo("Voleibol", min_jugadores=12, duracion_oficial=60)
    balonmano: DeporteEquipo = DeporteEquipo("Balonmano", min_jugadores=14, duracion_oficial=60)

    # Creamos 10 pistas variadas (5 exteriores, 5 interiores)
    pista1: PistaExterior = PistaExterior("EXT-01", 4, tenis)
    pista2: PistaExterior = PistaExterior("EXT-02", 4, padel)
    pista3: PistaExterior = PistaExterior("EXT-03", 10, futbol_sala)
    pista4: PistaExterior = PistaExterior("EXT-04", 10, baloncesto)
    pista5: PistaExterior = PistaExterior("EXT-05", 4, padel)
    pista1.estado = "Ocupada"  # Pista de tenis ocupada para la liga

    pista6: PistaInterior = PistaInterior("INT-01", 10, futbol_sala)
    pista7: PistaInterior = PistaInterior("INT-02", 10, baloncesto)
    pista8: PistaInterior = PistaInterior("INT-03", 12, voleibol)
    pista9: PistaInterior = PistaInterior("INT-04", 14, balonmano)
    pista10: PistaInterior = PistaInterior("INT-05", 4, tenis)
    pista6.estado = "Ocupada"  # Pista de fútbol sala ocupada para la reserva normal

    todas_las_pistas: list[Pista] = [pista1, pista2, pista3, pista4, pista5, pista6, pista7, pista8, pista9, pista10]

    # Creamos una tarifa general para todas las pistas
    tarifa_base: Tarifa = Tarifa("Estándar", 12.50) # 12.50€ la hora

    # Creamos primeramente los calendarios vacíos
    calendario_oficial: Calendario = Calendario()
    calendario_pachangas: Calendario = Calendario()

    # carga de ficheros binarios
    print("Cargando historial de reservas del sistema...")
    calendario_pachangas.cargar_de_fichero()
    print("-" * 50)

    admin_user: Usuario = Usuario("00000000A", "Admin")
    ev_oficial: Evento = Evento("EV-001", pista1, admin_user, "10:00", 2, 1)  # Prioridad 1 es una liga
    ev_normal: Evento = Evento("EV-006", pista6, admin_user, "12:00", 10, 2)  # Prioridad 2 es una reserva cualquiera

    calendario_oficial.añadir_evento(ev_oficial)
    calendario_pachangas.añadir_evento(ev_normal)

    try:

        # Bucle general, para controlar las diferentes opciones
        while True:
            print(" ----- MENÚ -----")
            print("1. Ver pistas disponibles y restricciones")
            print("2. Crear una reserva nueva")
            print("3. Ver calendario oficial")
            print("4. Fusionar calendarios de Liga y Normal")
            print("5. Consultar tarifas y precios")
            print("6. Salir del programa")
            print()
            opcion: str = input("Elige una opción (1-6): ")

            if opcion == "1":
                print("\n--- ESTADO DE LAS PISTAS ---")
                for p in todas_las_pistas:
                    print(f"{p} | Descripción: {p.descripcion()}")

            elif opcion == "2":
                print("\n--- NUEVA RESERVA ---")
                # Actualizamos el input para que muestre los nuevos deportes
                deporte_deseado: str = input(
                    "¿Qué deporte quieres jugar? (Tenis/Padel/Baloncesto/Futbol sala/Voleibol/Balonmano): ").capitalize() #para poner la primera en mayuscula y las demás en minuscula
                pistas_disponibles: list[Pista] = [] # creamos una lista para ver que listas estan disponibles para reservar
                for p in todas_las_pistas:
                    if p.deporte.nombre == deporte_deseado and p.estado == "Disponible":
                        pistas_disponibles.append(p)

                # vemos si hay alguna libre
                if not pistas_disponibles:
                    print(f"\nLo siento, no hay pistas libres en este momento para {deporte_deseado}.")
                else:
                    pista_asignada: Pista = random.choice(pistas_disponibles)
                    print(f"\nSe te ha asignado la pista: {pista_asignada.id_pista}")

                    # Pedimos los datos al usuario para gestionar la reserva
                    nombre_user: str = input("Tu nombre: ")
                    dni_user: str = input("Tu DNI: ")
                    hora_ev: str = input("Hora de la reserva: ")
                    usuario_actual: Usuario = Usuario(dni_user, nombre_user)
                    nombre_ev: str = input("Ponle un nombre a la reserva: ")
                    nuevo_evento: Evento = Evento(nombre_ev, pista_asignada, usuario_actual, hora_ev, 2, 2)
                    calendario_pachangas.añadir_evento(nuevo_evento)

                    # cambiamos el estado para que no se pueda volver a reservar
                    pista_asignada.estado = "Ocupada"
                    # Implementación de fichero de texto plano (Modo 'a' para añadir sin borrar)
                    with open("datos/registro_reservas.txt", "a", encoding="utf-8") as f:
                        f.write(f"Reserva: {nombre_ev} | Pista: {pista_asignada.id_pista} | Cliente: {usuario_actual.nombre} | Hora: {hora_ev}\n")
                    print(f"\nReserva '{nombre_ev}' creada a cargo de {usuario_actual}")
                    print()

            elif opcion == "3":
                print("\n--- CALENDARIO OFICIAL ---")
                if not calendario_oficial.eventos:
                    print("No hay eventos en el calendario oficial.")
                else:
                    # implementamos un for para imprimir todos los eventos uno debajo de otro
                    for ev in calendario_oficial.eventos:
                        print(f"LIGA | ID: {ev.id_evento} | Pista: {ev.pista.id_pista} | Deporte: {ev.pista.deporte.nombre}")
                print()
            elif opcion == "4":
                print("\nFusionando calendarios usando el operador '+' ...")
                cal_total: Calendario = calendario_oficial + calendario_pachangas

                print("--- CALENDARIO TOTAL COMBINADO ---")
                if not cal_total.eventos:
                    print("El calendario combinado está vacío.")
                else:
                    for ev in cal_total.eventos:
                        tipo: str = "LIGA" if ev.prioridad == 1 else "NORMAL"
                        print(f"{tipo} | ID: {ev.id_evento} | Pista: {ev.pista.id_pista}")
                print()
            elif opcion == "5":
                print("\n--- CONSULTA DE TARIFAS ---")
                print(tarifa_base)
                try:
                    horas: float = float(input("¿Cuántas horas vas a reservar?: "))
                    total: float = tarifa_base.calcular_precio(horas)
                    print(f"El precio total por {horas} horas sería: {total:.2f}€")
                except ValueError:
                    print("\nDebes introducir un número válido (ej: 2 o 1.5).")
                print()
            elif opcion == "6":
                print("\nSaliendo del sistema... ")
                calendario_pachangas.guardar_en_fichero()
                break  # para romper el bucle

            else:
                print("\nOpción no válida. Por favor, elige un número del 1 al 6.")

    except KeyboardInterrupt:
        print("\n\nInterrupción forzada detectada (Ctrl+C).")
    finally:
        print("Cerrando el sistema de reservas deportivas de forma segura. ¡Que tengas un gran día!")


if __name__ == "__main__":
    main()