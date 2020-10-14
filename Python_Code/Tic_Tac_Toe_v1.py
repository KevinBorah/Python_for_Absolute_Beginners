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
    players = ["Kevin", "Computer"]
    symbols = ["X", "O"]

    # Until Someone Wins
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That's not a valid play! Try again.")
            continue
        input("pause")


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board.")
    print()


def show_board(board):
    for row in board:
        print(" | ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=' | ')
        print()


def choose_location(board, symbol):
    row = int(input("Choose which row!"))
    column = int(input("Choose which column!"))

    row -= 1
    column -= 1
    if row < 0 or row > 2:
        return False
    if column < 0 or column > 2:
        return False

    cell = board[row][column]
    if cell is not None:
        return False
    board[row][column] = symbol
    return True


def find_winner(board):
    # Todo implement how we check for a winner
    return False


if __name__ == '__main__':
    main()

# <K2>
