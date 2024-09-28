import random


def print_board(board):
    """Prints the current state of the board."""
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Checks for a winner on the board."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def get_computer_move(board):
    """Returns a random move for the computer."""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Player is X, Computer is O

    while True:
        print_board(board)

        if current_player == "X":
            # Player's turn
            while True:
                try:
                    row = int(input("Player, enter your row (0, 1, or 2): "))
                    col = int(input("Player, enter your column (0, 1, or 2): "))
                    if row not in range(3) or col not in range(3):
                        print("Invalid position. Please enter 0, 1, or 2.")
                        continue
                    if board[row][col] != " ":
                        print("Cell already taken. Please choose another cell.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers 0, 1, or 2.")

            board[row][col] = current_player
        else:
            # Computer's turn
            print("Computer's turn:")
            row, col = get_computer_move(board)
            board[row][col] = current_player
            print(f"Computer chose: {row}, {col}")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch turns
        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
