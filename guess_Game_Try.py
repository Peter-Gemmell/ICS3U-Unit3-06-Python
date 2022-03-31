#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants


import random


def main():
    # this function is the game

    # input
    guessed_number_string = input("Guess a number between 0-9: ")
    mystery_Number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guessed_Number = int(guessed_number_as_string)

        if guessed_Number == mystery_Number:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly. Try again.")
            print("\nThe correct answer was {0}.".format(some_variable))

    except Exception:
        print("Invalid number guessed, please try again.")
    print("\nDone.")


if __name__ == "__main__":
    main()
