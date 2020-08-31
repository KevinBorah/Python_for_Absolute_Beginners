print("----------------------------")
print("   Rock Paper Scissors v1")
print("----------------------------")
print()

player_1 = input("Enter Player 1's name: ")
player_2 = input("Enter Player 2's name: ")

rolls = ['rock', 'paper', 'scissors']

roll1 = input(f"{player_1} what is your roll? {rolls}: ")
roll1 = roll1.lower().strip()
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} is not a valid play!")
    roll1 = input(f"{player_1} what is your roll? {rolls}: ")
roll2 = input(f"{player_2} what is your roll? {rolls}: ")
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f"Sorry {player_2}, {roll2} is not a valid play!")
    roll2 = input(f"{player_2} what is your roll? {rolls}: ")

print(f"{player_1} rolls {roll1}")
print(f"{player_2} rolls {roll2}")

# Test for a winner
winner = None

if roll1 == roll2:
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
    print("The game was a tie")
else:
    print(f"{winner} wins the game!")

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

# <K2>
