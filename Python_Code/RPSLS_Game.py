import random

winner = None


def print_header():
    print("------------------------------------------")
    print("   Rock, Paper, Scissors, Lizard, Spock")
    print("------------------------------------------")
    print()


def scoring(player_1, roll1, player_2, roll2):
    global winner
    if roll1 == roll2:
        winner = 'tie'
        print(f"{player_1} you tied with {player_2} no one likes a tie.")
    elif roll1 == 'rock':
        if roll2 == 'scissors':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} crushes {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'lizard':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} crushes {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'paper':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} covers {roll1}. Therefore {winner} wins the round!")
        elif roll2 == 'spock':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} vaporizes {roll1}. Therefore {winner} wins the round!")
    elif roll1 == 'paper':
        if roll2 == 'rock':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} covers {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'spock':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} disproves {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'scissors':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} cuts {roll1}. Therefore {winner} wins the round!")
        elif roll2 == 'lizard':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} eats {roll1}. Therefore {winner} wins the round!")
    elif roll1 == 'scissors':
        if roll2 == 'paper':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} cuts {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'lizard':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} decapitates {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'rock':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} crushes {roll1}. Therefore {winner} wins the round!")
        elif roll2 == 'spock':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} smashes {roll1}. Therefore {winner} wins the round!")
    elif roll1 == 'lizard':
        if roll2 == 'paper':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} eats {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'spock':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} poisons {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'rock':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} crushes {roll1}. Therefore {winner} wins the round!")
        elif roll2 == 'scissors':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} decapitates {roll1}. Therefore {winner} wins the round!")
    elif roll1 == 'spock':
        if roll2 == 'rock':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} vaporizes {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'scissors':
            winner = player_1
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll1} smashes {roll2}. Therefore {winner} wins the round!")
        elif roll2 == 'paper':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} disproves {roll1}. Therefore {winner} wins the round!")
        elif roll2 == 'lizard':
            winner = player_2
            print(
                f"{player_1} threw {roll1}; {player_2} threw {roll2}; {roll2} poisons {roll1}. Therefore {winner} wins the round!")

    # Scoring rules for Rock, Paper, Scissors, Lizard, Spock
    #   Rock
    #       wins vs scissors    (crushes scissors)
    #       wins vs lizard      (crushes lizard)
    #       loses vs paper      (covered by paper)
    #       loses vs spock      (vaporized by spock)
    #   Paper
    #       wins vs rock        (covers rock)
    #       wins vs spock       (disproves spock)
    #       loses vs scissors   (cut by scissors)
    #       loses vs lizard     (lizard eats paper)
    #   Scissors
    #       wins vs paper       (cuts paper)
    #       wins vs lizard      (decapitates lizard)
    #       loses vs rock       (crushed by rock)
    #       loses vs spock      (smashed by spock
    #   Lizard
    #       wins vs paper       (eats paper)
    #       wins vs spock       (poisons spock)
    #       loses vs rock       (crushed by rock)
    #       loses vs scissors   (decapitated by scissors)
    #   Spock
    #       wins vs rock        (vaporizes rock)
    #       wins vs scissors    (smashes scissors)
    #       loses vs paper      (disproved by paper)
    #       loses vs lizard     (poisoned by lizard)


def player_1_turn(player_1, rolls):
    roll = input(f"{player_1} what would you like to throw? {rolls} ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(
            f"{player_1} ({roll}) is not a valid roll. Please use one of these options: {rolls}, or check your spelling and try again.")
        roll = input(f"{player_1} what would you like to throw? {rolls} ")
        roll = roll.lower().strip()
        if roll not in rolls:
            print(
                f"{player_1} ({roll}) is not a valid roll. Please use one of these options: {rolls}, or check your spelling and try again.")
            roll = input(f"{player_1} what would you like to throw? {rolls} ")
    return roll


def play_round(user, computer, valid_rolls):
    global winner
    player_1_roll = player_1_turn(user, valid_rolls)
    player_2_roll = random.choice(valid_rolls)
    scoring(user, player_1_roll, computer, player_2_roll)
    # if winner == 'tie':
    # try_again = input(f"{user} you should try again? (yes or no) ")
    # try_again = try_again.lower().strip()
    # if try_again == "yes" or try_again == 'y':
    # player_1_roll = player_1_turn(user, valid_rolls)
    # player_2_roll = random.choice(valid_rolls)
    # scoring(user, player_1_roll, computer, player_2_roll)


def first_to_3(player_1, player_2, valid_rolls):
    global winner
    p1_wins = 0
    p2_wins = 0
    rounds = 0
    while p1_wins < 3 and p2_wins < 3:
        play_round(player_1, player_2, valid_rolls)
        rounds += 1
        if winner == player_1:
            p1_wins += 1
        elif winner == player_2:
            p2_wins += 1
        print(f"after {rounds} rounds the score is: {player_1}: {p1_wins}, and {player_2}: {p2_wins}.")
    if p1_wins >= 3:
        winner = player_1
    elif p2_wins >= 3:
        winner = player_2
    print(f"{winner} takes the game!")


def main():
    global winner
    print_header()
    valid_rolls = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    player_1 = input("Hello player, what is your name? ")
    player_2 = "Computer"
    first_to_3(player_1, player_2, valid_rolls)
    try_again = None
    if winner is not player_1:
        try_again = input(f"{player_1} you lost, would you like to play again? (yes or no) ")
        try_again = try_again.lower().strip()
    else:
        try_again = input(f"{player_1} you won! do you want to push your luck and play again? (yes or no) ")
        try_again = try_again.lower().strip()
    if try_again == 'yes' or try_again == 'y':
        first_to_3(player_1, player_2, valid_rolls)
    else:
        print("OK, have a nice day.")


main()

# <K2>
