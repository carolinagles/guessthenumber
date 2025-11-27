"""
Game mode and sequential game logic

- Game logic
- Single or Two Player mode
- Store results
"""

import random
import getpass
from datetime import datetime
from .config import difficulty, min_num, max_num, statistics_file
import openpyxl


def select_difficulty():
    while True:
        option = input(
            "Choose difficulty level:\n1. Easy → 20 attempts\n2. Medium → 12 attempts\n3. Hard → 5 attempts\n")
        if option in difficulty:
            return difficulty[option]
        else:
            print("Please choose one of the three levels:")


def play_game(secret_number, max_attempts):
    remaining_attempts = max_attempts
    guessed = False

    while remaining_attempts > 0 and not guessed:
        try:
            guess = int(input(f"You have {remaining_attempts} attempts: "))
            if guess < min_num or guess > max_num:
                print("Please enter a number between 1 and 1000")
                continue
            remaining_attempts -= 1

            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                guessed = True
            elif guess < secret_number:
                print("\nTry with a HIGHER number")
            else:
                print("\nTry with a LOWER number")

        except ValueError:
            print("Remember, number between 1 and 1000")
            continue

    if not guessed:
        print(f"Sorry, you didn't make it this time, {secret_number} was the number")

    attempts_used = max_attempts - remaining_attempts
    return guessed, attempts_used


def save_record(name, mode, configuration, attempts, result):
    try:
        workbook = openpyxl.load_workbook(statistics_file)
        sheet = workbook.active

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = "Won" if result else "Lost"
        level = configuration['level']

        sheet.append([date, name, mode, level, attempts, result_text])
        workbook.save(statistics_file)

    except Exception as e:
        print(f"An error occurred while saving: {e}")


def single_player():
    print("Single Player Mode\n")

    configuration = select_difficulty()
    secret_number = random.randint(min_num, max_num)
    max_attempts = configuration['attempts']

    print(f"Use your {max_attempts} attempts wisely to guess the number.")

    guessed, attempts = play_game(secret_number, max_attempts)

    name = input("\nSave your game\n Enter your name: ")
    save_record(name, "Single", configuration, attempts, guessed)


def two_players():
    print("2 Player Mode\n")

    configuration = select_difficulty()
    max_attempts = configuration['attempts']

    print("Think of the number you want the second player to guess...")
    while True:
        try:
            print("Enter a number between 1 and 1000: ")
            secret_number = int(getpass.getpass(""))
            if min_num <= secret_number <= max_num:
                break
            else: 
                print("Number must be between 1 and 1000.")
        except ValueError:
            print("Remember, number between 1 and 1000")

    print("Enter your first attempt:")

    guessed, attempts = play_game(secret_number, max_attempts)

    name = input("\nSave your game\n Name of the player who guessed: ")
    save_record(name, "Double", configuration, attempts, guessed)