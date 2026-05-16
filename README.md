[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
# Sistema de Reservas de Pistas Deportivas

## Propósito del Proyecto
Esta aplicación es un sistema interactivo de gestión por consola para un polideportivo. Permite administrar diferentes tipos de pistas (interiores y exteriores), gestionar una gran variedad de deportes (raqueta y equipo), consultar las tarifas vigentes, y organizar un calendario de eventos deportivos. El núcleo del sistema prioriza automáticamente las competiciones oficiales (Ligas) sobre las reservas normales (Pachangas) mediante la sobrecarga de operadores matemáticos.

## Características Técnicas Implementadas
* Programación Orientada a Objetos (POO) con al menos 10 clases estructuradas.
* Clases Abstractas y Herencia simple para la definición de Pistas y Deportes.
* Encapsulamiento de atributos con propiedades (Getters/Setters).
* Sobrecarga de operadores matemáticos (`+`, `<`) para fusionar y ordenar calendarios.
* Sugerencia de tipos (Type Hinting) en todo el código.
* Control de Excepciones personalizado (`ValueError`, `FileNotFoundError`, `KeyboardInterrupt`).
* Persistencia de datos en ficheros binarios (`pickle`) para el guardado automático de reservas.
* Generación de tickets en ficheros de texto plano (`.txt`) con modo *append*.

## Requisitos e Instalación

Clona el repositorio en tu máquina local:
`git clone https://github.com/prog2-ia/trabajo-final-b10`

Accede al directorio del proyecto:
`cd trabajo-final-b10`

Crea y activa un entorno virtual:
`python3 -m venv venv`
`source venv/bin/activate`

## Uso y Ejemplos
Para iniciar el sistema interactivo, asegúrate de tener el entorno virtual activado y ejecuta el archivo principal desde la terminal:
`python main.py`

Al arrancar, el programa cargará automáticamente el historial de reservas desde el fichero binario (si existe) y te mostrará el siguiente menú principal:

```text
----- SISTEMA DE RESERVAS DE PISTAS DEPORTIVAS -----

Cargando historial de reservas del sistema...
 Datos cargados correctamente desde 'datos_calendario.bin'.
--------------------------------------------------
 ----- MENÚ -----
1. Ver pistas disponibles y restricciones
2. Crear una reserva nueva
3. Ver calendario oficial
4. Fusionar calendarios de Liga y Normal
5. Consultar tarifas y precios
6. Salir del programa

Elige una opción (1-6):