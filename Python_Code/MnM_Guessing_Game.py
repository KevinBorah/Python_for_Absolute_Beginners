import random
MnMs = random.randint(1, 100)
print("---------------------------")
print("     M&M Guessing Game")
print("---------------------------")
print()

print("Can you guess the number of M&M's between 1 and 100? I will give you 6 attempts. Good luck!")
print()

guesses = 1
while guesses <= 6:
    guess = input("How many M&M's are there? ")
    guessNum = int(guess)
    if guessNum == MnMs:
        print(f"You're right there are {guess} M&M's in the jar. It took you {guesses} attempts to guess the right number.")
        break
    elif guessNum < MnMs:
        print(f"You're too low. You have {6 - guesses} Guesses left")
        guesses += 1
    elif guessNum > MnMs:
        print(f"You're too high. You have {6 - guesses} Guesses left")
        guesses += 1

if guesses == 7:
    print(f"Sorry that's all of your guesses. The correct number was {MnMs}. Better luck next time")

# <K2>
