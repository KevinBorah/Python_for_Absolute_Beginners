# Create the Board
# Choose an Initial Player
# Until Someone Wins
#   Show the Board
#   Choose Location, Verify the Spot is Empty, and Mark It
#   Toggle Active Player
#   Check for Winner

# Game Over, Active Player Won


def main():
    # Create the Board
    # Board is a list of rows
    # Rows are a list of columns
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Choose an Initial Player
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X", "O"]

    # Until Someone Wins
    while not find_winner(board):
        print("Play a round...")

    print(board)


def find_winner(board):
    # Todo implement how we check for a winner
    return False


if __name__ == '__main__':
    main()

# <K2>
