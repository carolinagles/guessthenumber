"""
Main Menu

Creates welcome for users
Options to play, view game history, or exit
"""
from .game import single_player, two_players
from .records import records_menu
import getpass
import os


def menu():
    while True:
        print("\nGuess a number between 1 and 1000\n")
        print("Main Menu\n") 
        print("1. Single Player Game\n2. 2 Player Game\n3. Statistics\n4. Exit\n")
        
        option = input("Select a numeric option: ")

        if option == '1':
            print("\nLet's start playing!\n") 
            single_player()
        elif option == '2':
            print("\nLet's start playing!\n") 
            two_players()
        elif option == '3':
            from .records import records_menu
            records_menu()
        elif option == '4':
            print('See you soon!')
            break
        else:
            print("Please select an option between 1-4: ")