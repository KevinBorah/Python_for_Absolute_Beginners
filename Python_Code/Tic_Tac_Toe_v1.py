import random
import time


# Create the Board
# Choose an Initial Player
# Until Someone Wins
#   Show the Board
#   Choose Location, Verify the Spot is Empty, and Mark It
#   Toggle Active Player
#   Check for Winner

# Game Over, Active Player Won


def main():
    print("---------------------------")
    print("        Tic_Tac_Toe")
    print("Can you get three in a row?")
    print("---------------------------")
    print()

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
    players = get_players()
    symbols = ["X", "O"]
    player = players[active_player_index]

    # Until Someone Wins
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol, player):
            print("That's not a valid play! Try again.")
            continue

        # Toggle Active Player
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} Wins the game! Here's the final board:")
    print()
    show_board(board)
    print()


def get_players():
    players = [None, None]
    players[0] = input("Player 1: what is your name?")
    print("Player 1: Do you want to play against a Human or the Computer?")
    player_2 = int(input("(Enter 1 to play against a Human, or enter 2 to play against the Computer)"))
    if player_2 == 1:
        players[1] = input("Player 2: What is your name?")
    else:
        players[1] = "COMPUTER"
    return players


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
    print()


def choose_location(board, symbol, active_player):
    # DECIDING WHETHER THE ACTIVE PLAYER IS THE COMPUTER, IF IT IS THEN IT RANDOMLY SELECTS A BOARD POSITION FOR THE COMPUTER.
    if active_player == "COMPUTER":
        row = random.randint(0, len(board) - 1)
        column = random.randint(0, len(board[row]) - 1)
        cell = board[row][column]
        if cell is not None:
            return False
        board[row][column] = symbol
        return True
    # IF IT'S NOT THE COMPUTER YOU GET TO GO.
    else:
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
    sequences = find_winning_sequences(board)
    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def find_winning_sequences(board):
    sequences = []

    # WIN BY ROWS
    rows = board
    sequences.extend(rows)

    # WIN BY COLUMNS
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        sequences.append(col)

    # WIN BY DIAGONALS
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    sequences.extend(diagonals)
    return sequences


if __name__ == '__main__':
    main()
    time.sleep(3)

# <K2>
