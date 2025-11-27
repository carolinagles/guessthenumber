"""
Modo y lógica secuencial de juego

- Lógica 
- Modo Solitario o Doble
- Almacenar resultados 

"""

import random
import getpass
from datetime import datetime
from .configuraciones import dificultad, num_min, num_max, estadisticas
import openpyxl


def nivel_dificultad():
    while True:
        opcion = input(
            "Elige el nivel de dificultad:\n1. Fácil → 20 intentos\n2. Medio → 12 intentos\n3. Difícil → 5 intentos\n")
        if opcion in dificultad:
            return dificultad[opcion]
        else:
            print("Elige uno de los tres niveles:")


def partidas(incognita, max_int):
    intentos_restantes = max_int
    adivinado = False

    while intentos_restantes > 0 and not adivinado:
        try:
            intento = int(input(f"Tienes {intentos_restantes} intentos: "))
            if intento < num_min or intento > num_max:
                print("Ingresa un número entre 1 y 1000")
                continue
            intentos_restantes -= 1

            if intento == incognita:
                print("¡Lo lograste, adivinaste el número!")
                adivinado = True
            elif intento < incognita:
                print("\nIntenta con un numero MAYOR")
            else:
                print("\nIntenta con un numero MENOR")

        except ValueError:
            print("Recuerda, número entre 1 y 1000")
            continue

    if not adivinado:
        print(f"Lo siento, no lo lograste esta vez, {incognita} era el número")

    intentos = max_int - intentos_restantes
    return adivinado, intentos


def guardar_historial(nombre, modo, configuracion, intentos, resultado):
    try:
        workbook = openpyxl.load_workbook(estadisticas)
        hoja = workbook.active

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_texto = "Ganado" if resultado else "Perdido"
        nivel = configuracion['nivel']

        hoja.append([fecha, nombre, modo, nivel,
                    intentos, resultado_texto])
        workbook.save(estadisticas)

    except Exception as e:
        print(f"Ocurrió un error al guardar: {e}")


def solitario():
    print("Modo Solitario\n")

    configuracion = nivel_dificultad()
    numero_secreto = random.randint(num_min, num_max)
    max_intentos = configuracion['intentos']

    print(f"Cuida tus {max_intentos} intentos para lograr adivinar el número.")

    adivinado, intentos = partidas(numero_secreto, max_intentos)

    nombre = input("\nRegistra tu partida\n Dame tu nombre: ")
    guardar_historial(nombre, "Solitario", configuracion, intentos, adivinado)


def doble():
    print("Modo 2 Jugadores\n")

    configuracion = nivel_dificultad()
    max_intentos = configuracion['intentos']

    print("Piensa el número que quieres que adivine el segundo jugador...")
    while True:
        try:
            print("Escribe el número entre 1 y 1000: ")
            numero_secreto = int(getpass.getpass(""))
            if num_min <= numero_secreto <= num_max:
                break
            else: 
                print("Número entre 1 y 1000.")
        except ValueError:
            print("Recuerda, número entre 1 y 1000")

    print("Ingresa tu primer intento:")

    adivinado, intentos = partidas(numero_secreto, max_intentos)

    nombre = input("\nRegistra tu partida\n Nombre de quien adivinó: ")
    guardar_historial(nombre, "Doble", configuracion, intentos, adivinado)