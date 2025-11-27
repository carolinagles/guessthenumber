"""
Menu principal

Se crea la bienvenida a usarios
opciones para jugar, ver historial de juegos o salir
"""
from .juego import solitario, doble
from .historial import historial
import getpass
import os


def menu():
    while True:
        print("\nAdivina un número entre 1 y 1000\n")
        print("Menú pricipal\n") 
        print("1. Partida modo solitario\n2. Partido 2 jugadores\n3. Estadística\n4. Salir\n")
        
        opcion = input("Selecciona una opción númerica: ")

        if opcion == '1':
            print("\n¡Comenzemos a jugar!\n") 
            solitario()
        elif opcion == '2':
            print("\n¡Comenzemos a jugar!\n") 
            doble()
        elif opcion == '3':
            from .historial import historial
            historial()
        elif opcion == '4':
            print('¡Nos vemos pronto!')
            break
        else:
            print("Selecciona una opción entre 1-4: ")