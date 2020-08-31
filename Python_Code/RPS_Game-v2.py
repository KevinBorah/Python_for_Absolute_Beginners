import random


def main():
    print_header()

    player = input("What's your name: ")
    ai = "Computer"

    play_game(player, ai)


def print_header():
    print("----------------------------")
    print("   Rock Paper Scissors v2")
    print("----------------------------")
    print()


def play_game(player_1, player_2):

    rolls = ['rock', 'paper', 'scissors']

    roll1 = input(f"{player_1} what is your roll? {rolls}: ")
    roll1 = roll1.lower().strip()
    if roll1 not in rolls:
        print(f"Sorry {player_1}, {roll1} is not a valid play!")
        roll1 = input(f"{player_1} what is your roll? {rolls}: ")
    roll2 = random.choice(rolls)

    print(f"{player_1} rolls {roll1}")
    print(f"The {player_2} rolls {roll2}")

    # Test for a winner
    winner = None

    if roll1 == roll2:
        print()
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'rock':
            winner = player_1
        elif roll2 == 'scissors':
            winner = player_2
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1

    print("The round is over!")
    if winner is None:
        print("The game was a tie. Better luck next time.")
    elif winner == player_2:
        print(f"Boo! {winner} wins the game. :( Better luck next time.")
    else:
        print(f"Yay! {winner} wins the game! :)")

    # Rules for scoring.
    # Rock
    #   Rock -> Tie
    #   Paper -> Lose
    #   Scissors -> Win
    # Paper
    #   Rock -> Win
    #   Paper -> Tie
    #   Scissors -> Lose
    # Scissors
    #   Rock -> Lose
    #   Paper -> Win
    #   Scissors -> Tie


if __name__ == '__main__':
    main()

# <K2>
