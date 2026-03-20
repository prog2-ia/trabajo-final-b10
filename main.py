from pista import PistaInterior, PistaExterior
from eventos import Evento, Calendario
from tarifa import Tarifa
from usuario import Usuario
from deporte import DeporteRaqueta, DeporteEquipo


def main():
    print("----- SISTEMA DE RESERVAS DE PISTAS DEPORTIVAS -----\n")

    # 1. Instanciamos los deportes REALES
    tenis = DeporteRaqueta("Tenis", min_jugadores=2, necesita_red=True)
    baloncesto = DeporteEquipo("Baloncesto", min_jugadores=10, duracion_oficial=40)

    # 2. Creamos las pistas y les asignamos los deportes
    pista1 = PistaExterior("EXT-01", 4, tenis)
    pista2 = PistaInterior("INT-01", 10, baloncesto)

    # 3. Inicializamos calendarios y metemos datos de prueba
    calendario_oficial = Calendario()
    calendario_pachangas = Calendario()

    ev_oficial = Evento("EV-001", pista1, 2, 1)  # Prioridad 1 (Liga)
    ev_normal = Evento("EV-002", pista2, 10, 2)  # Prioridad 2 (Normal)

    calendario_oficial.añadir_evento(ev_oficial)
    calendario_pachangas.añadir_evento(ev_normal)

    # --- MENÚ DE UNA SOLA EJECUCIÓN ---
    print("=" * 45)
    print("  MENÚ DE PRUEBA - POLIDEPORTIVO B10")
    print("=" * 45)
    print("1. Ver pistas disponibles y restricciones")
    print("2. Crear una reserva nueva")
    print("3. Ver calendario oficial")
    print("4. Fusionar calendarios (Prueba de operador +)")

    opcion = input("\nElige una opción (1-4) para probar: ")

    if opcion == "1":
        print("\n--- ESTADO DE LAS PISTAS ---")
        print(f"{pista1} -> {pista1.descripcion()}")
        print(f"Restricciones: {tenis.obtener_restricciones()}\n")

        print(f"{pista2} -> {pista2.descripcion()}")
        print(f"Restricciones: {baloncesto.obtener_restricciones()}")

    elif opcion == "2":
        print("\n--- NUEVA RESERVA ---")
        id_ev = input("ID del evento (ej. EV-03): ")
        print(f"Creando evento {id_ev} en {pista1.id_pista}...")
        nuevo_evento = Evento(id_ev, pista1, 2, 2)
        calendario_pachangas.añadir_evento(nuevo_evento)
        print("¡Reserva creada con éxito para esta ejecución!")

    elif opcion == "3":
        print("\n--- CALENDARIO OFICIAL ---")
        for ev in calendario_oficial.eventos:
            # Mostramos a qué deporte corresponde la pista del evento
            print(f"🏆 LIGA | ID: {ev.id_evento} | Pista: {ev.pista.id_pista} | Deporte: {ev.pista._deporte.nombre}")

    elif opcion == "4":
        print("\nFusionando calendarios usando el operador '+' ...")
        cal_total = calendario_oficial + calendario_pachangas

        print("--- CALENDARIO TOTAL COMBINADO (Ordenado por prioridad) ---")
        for ev in cal_total.eventos:
            tipo_str = "🏆 LIGA" if ev.prioridad == 1 else "🟢 NORMAL"
            print(f"{tipo_str} | ID: {ev.id_evento} | Pista: {ev.pista.id_pista}")

    else:
        print("\nOpción no válida.")

    print("\n--- Fin de la prueba del modelo ---")


if __name__ == "__main__":
    main()