# Version 2 uses Data sets instead of if elif statements to check for a winner.


import random
import time

rolls = {
    'rock': {
        'defeats': {
            'scissors': {'Just as it always has rock crushes scissors'},
            'lizard': {'rock crushes lizard'},
        },
        'defeated_by': {
            'paper': {'paper cover rock'},
            'spock': {'spock vaporizes rock'},
        },
    },
    'paper': {
        'defeats': {
            'rock': {'paper cover rock'},
            'spock': {'paper disproves spock'}
        },
        'defeated_by': {
            'scissors': {'scissors cuts paper'},
            'lizard': {'lizard eats paper'}
        },
    },
    'scissors': {
        'defeats': {
            'paper': {'scissors cuts paper'},
            'lizard': {'scissors decapitates lizard'}
        },
        'defeated_by': {
            'rock': {'Just as it always has rock crushes scissors'},
            'spock': {'spock crushes scissors'}
        },
    },
    'lizard': {
        'defeats': {
            'paper': {'lizard eats paper'},
            'spock': {'lizard poisons spock'}
        },
        'defeated_by': {
            'rock': {'rock crushes lizard'},
            'scissors': {'scissors decapitates lizard'}
        },
    },
    'spock': {
        'defeats': {
            'rock': {'spock vaporizes rock'},
            'scissors': {'spock crushes scissors'}
        },
        'defeated_by': {
            'paper': {'paper disproves spock'},
            'lizard': {'lizard poisons spock'}
        },
    },
}

winner = None


def print_header():
    print("-----------------------------------------------------")
    print("       Rock, Paper, Scissors, Lizard, Spock v2")
    print()
    print('  rules:')
    print('''      "Scissors cuts Paper, Paper covers Rock,
    Rock crushes Lizard, Lizard poisons Spock,
Spock smashes Scissors, Scissors decapitates Lizard,
      Lizard eats Paper, Paper disproves Spock,
   Spock vaporizes Rock, and just as it always has
              Rock crushes Scissors"
                                 --Sheldon Cooper
                                        <K2>
''')
    print("-----------------------------------------------------")
    print()


def scoring(player_1, roll1, player_2, roll2):
    global winner
    outcomes = rolls.get(roll1)
    if roll1 == roll2:
        winner = 'tie'
        print(f"{player_1} you tied with {player_2} by both throwing {roll1}. No one likes a tie.")
    elif roll2 in outcomes.get('defeats'):
        defeats = outcomes.get('defeats')
        winning_text = str(defeats.get(roll2)).replace('{', '').replace('}', '')
        print(
            f"{player_1} threw {roll1} and {player_2} threw {roll2}: {winning_text} Therefore {player_1} takes the round!")
        winner = player_1
    elif roll2 in outcomes.get('defeated_by'):
        defeated_by = outcomes.get('defeated_by')
        winning_text = str(defeated_by.get(roll2)).replace('{', '').replace('}', '')
        print(
            f"{player_1} threw {roll1} and {player_2} threw {roll2}: {winning_text} Therefore {player_2} takes the round!")
        winner = player_2


def player_1_turn(player_1, valid_rolls):
    print()
    print("Available rolls:", end=' ')
    for index, r in enumerate(valid_rolls, start=1):
        print(f"{index}. {r}", end=' ')
    print()
    roll = int(input(f"{player_1} what would you like to throw? (Select 1-5 above) ")) - 1
    if roll < 0 or roll >= len(valid_rolls):
        print(f"{player_1} ({roll + 1}) is not a valid roll. Please try again.")
        print("Available rolls:", end=' ')
        for index, r in enumerate(valid_rolls, start=1):
            print(f"{index}. {r}", end=' ')
        print()
        roll = int(input(f"{player_1} what would you like to throw? ")) - 1
    print()

    return valid_rolls[roll]


def play_round(user, computer, valid_rolls):
    global winner
    player_1_roll = player_1_turn(user, valid_rolls)
    # player_2_roll = 'lizard'
    player_2_roll = random.choice(valid_rolls)
    scoring(user, player_1_roll, computer, player_2_roll)


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
    print()
    print(f"{winner} takes the game!")
    print()


def main():
    global winner
    print_header()
    valid_rolls = list(rolls.keys())
    player_1 = input("Hello player, what is your name? ")
    player_2 = "Computer"
    first_to_3(player_1, player_2, valid_rolls)
    if winner is not player_1:
        try_again = input(f"{player_1} you lost, would you like to play again? (yes or no) ")
        try_again = try_again.lower().strip()
    else:
        try_again = input(f"{player_1} you won! do you want to push your luck and play again? (yes or no) ")
        try_again = try_again.lower().strip()
    if try_again == 'yes' or try_again == 'y' or try_again == '1':
        first_to_3(player_1, player_2, valid_rolls)
    else:
        print("OK, have a nice day.")


main()
time.sleep(3)

# <K2>
