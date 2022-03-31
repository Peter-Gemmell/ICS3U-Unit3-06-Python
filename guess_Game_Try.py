#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program is a guessing game with try & catch


import random


def main():
    # this function is a guessing game with try & catch

    # input
    guessed_number_string = input("Guess a number between 0-9: ")
    mystery_Number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    try:
        guessed_Number = int(guessed_number_string)

        if guessed_Number == mystery_Number:
            print("\nYou guessed correctly!")
        else:
            print("You guessed incorrectly. Try again.")
            print("\nThe correct answer was {0}.".format(mystery_Number))

    except Exception:
        print("\nInvalid number, please try again.")
    print("\nDone.")


if __name__ == "__main__":
    main()
