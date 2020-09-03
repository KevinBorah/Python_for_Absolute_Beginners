import random


def print_header():
    print("--------------------------")
    print("   M&M Guessing Game v2")
    print("--------------------------")
    print()


def get_guesses(mnms):
    guesses = 1
    while guesses <= 6:
        guess = input("How many M&M's are there? ")
        guess_num = int(guess)
        if guess_num == mnms:
            print(f"You're right there are {guess} M&M's in the jar. It took you {guesses} attempts to guess the right number.")
            break
        elif guess_num < mnms:
            print(f"You're too low. You have {6 - guesses} Guesses left")
            guesses += 1
        elif guess_num > mnms:
            print(f"You're too high. You have {6 - guesses} Guesses left")
            guesses += 1
    return guesses


def play_game():
    mnms = random.randint(1, 100)
    print_header()
    print("Can you guess the number of M&M's between 1 and 100? I will give you 6 attempts. Good luck!")
    print()
    guesses = get_guesses(mnms)
    if guesses == 7:
        print(f"Sorry that's all of your guesses. The correct number was {mnms}. Better luck next time")


play_game()

# <K2>
