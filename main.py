from pista import PistaInterior, PistaExterior
from eventos import Evento, Calendario
from tarifa import Tarifa
from usuario import Usuario
from deporte import DeporteRaqueta, DeporteEquipo
import random

def main():
    print("----- SISTEMA DE RESERVAS DE PISTAS DEPORTIVAS -----\n")

    # Creamos diferentes deportes. Para esta demo crearemos unicamente 2.
    tenis=DeporteRaqueta("Tenis", min_jugadores=2, necesita_red=True)
    baloncesto=DeporteEquipo("Baloncesto", min_jugadores=10, duracion_oficial=40)

    # Como creamos 2 deportes vamos a crear únicamente 2 pistas.
    pista1=PistaExterior("EXT-01", 4, tenis)
    pista1.estado="Ocupada"
    pista2=PistaInterior("INT-01", 10, baloncesto)
    pista2.estado="Ocupada"
    pista3=PistaExterior("EXT-02", 4, tenis)
    pista4=PistaInterior("INT-02", 10, baloncesto)
    todas_las_pistas=[pista1,pista2,pista3,pista4]

    # Creamos una tarifa general para todas las pistas
    tarifa_base=Tarifa("Estándar", 12.50) # 12.50€ la hora

    # Creamos primeramente los calendarios vacíos
    calendario_oficial=Calendario()
    calendario_pachangas=Calendario()

    ev_oficial=Evento("EV-001", pista1, 2, 1)  # Prioridad 1 es una liga
    ev_normal=Evento("EV-002", pista2, 10, 2)  # Prioridad 2 es una reserva cualquiera

    calendario_oficial.añadir_evento(ev_oficial)
    calendario_pachangas.añadir_evento(ev_normal)

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
        opcion = input("Elige una opción (1-6): ")

        if opcion=="1":
            print("\n--- ESTADO DE LAS PISTAS ---")
            for p in todas_las_pistas:
                print(f"{p} | Descripción: {p.descripcion()}")


        elif opcion=="2":
            print("\n--- NUEVA RESERVA ---")
            deporte_deseado = input("¿Qué deporte quieres jugar? (Tenis/Baloncesto): ").capitalize() #para poner la primera en mayuscula y las demás en minuscula
            pistas_disponibles=[] # creamos una lista para ver que listas estan disponibles para reservar
            for p in todas_las_pistas:
                if p._deporte.nombre==deporte_deseado and p.estado=="Disponible":
                    pistas_disponibles.append(p)

            # vemos si hay alguna libre
            if not pistas_disponibles:
                print(f"\nLo siento, no hay pistas libres en este momento para {deporte_deseado}.")
            else:
                pista_asignada=random.choice(pistas_disponibles)
                print(f"\nSe te ha asignado la pista: {pista_asignada.id_pista}")

                # Pedimos los datos al usuario para gestionar la reserva
                nombre_user=input("Tu nombre: ")
                dni_user=input("Tu DNI: ")
                usuario_actual=Usuario(dni_user, nombre_user)
                nombre_ev=input("Ponle un nombre a la reserva: ")
                nuevo_evento=Evento(nombre_ev, pista_asignada, 2, 2)
                calendario_pachangas.añadir_evento(nuevo_evento)

                # cambiamos el estado para que no se pueda volver a reservar
                pista_asignada.estado="Ocupada"
                print(f"\nReserva '{nombre_ev}' creada a cargo de {usuario_actual}")
                print()


        elif opcion=="3":
            print("\n--- CALENDARIO OFICIAL ---")
            if not calendario_oficial.eventos:
                print("No hay eventos en el calendario oficial.")
            else:
                # implementamos un for para imprimir todos los eventos uno debajo de otro
                for ev in calendario_oficial.eventos:
                    print(f"LIGA | ID: {ev.id_evento} | Pista: {ev.pista.id_pista} | Deporte: {ev.pista._deporte.nombre}")
            print()


        elif opcion=="4":
            print("\nFusionando calendarios usando el operador '+' ...")
            cal_total=calendario_oficial + calendario_pachangas

            print("--- CALENDARIO TOTAL COMBINADO ---")
            if not cal_total.eventos:
                print("El calendario combinado está vacío.")
            else:
                for ev in cal_total.eventos:
                    tipo="LIGA" if ev.prioridad==1 else "NORMAL"
                    print(f"{tipo} | ID: {ev.id_evento} | Pista: {ev.pista.id_pista}")
            print()


        elif opcion=="5":
            print("\n--- CONSULTA DE TARIFAS ---")
            print(tarifa_base)
            horas=float(input("¿Cuántas horas vas a reservar?: "))
            total=tarifa_base.calcular_precio(horas)
            print(f"El precio total por {horas} horas sería: {total:.2f}€")
            print()


        elif opcion=="6":
            print("\nSaliendo del sistema... ")
            break  # para romper el bucle

        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 6.")


if __name__=="__main__":
    main()

# cuando se tenga mas tiempo, podremos reservar pistas en diferentes días para hacerlo más realista.