"""Tic Tac Toe game - 2 player (human vs human)."""

BOARD_SIZE = 3


def create_board():
    return [" "] * (BOARD_SIZE * BOARD_SIZE)


def display_board(board):
    print("\nCurrent board:")
    for row in range(BOARD_SIZE):
        cells = []
        for col in range(BOARD_SIZE):
            index = row * BOARD_SIZE + col
            cells.append(board[index] if board[index] != " " else str(index + 1))
        print(" {} | {} | {} ".format(*cells))
        if row < BOARD_SIZE - 1:
            print("---+---+---")
    print()


def check_winner(board):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return all(cell != " " for cell in board)


def get_player_move(board, player):
    while True:
        try:
            choice = input(f"Player {player}'s turn (choose a square 1-9): ").strip()
            index = int(choice) - 1
            if index < 0 or index >= len(board):
                print("Invalid! Please choose a number between 1 and 9.")
                continue
            if board[index] != " ":
                print("That square is already taken! Choose another.")
                continue
            return index
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")


def main():
    board = create_board()
    current_player = "X"

    print("Welcome to Tic Tac Toe - 2 Player Game!")
    print("Player 1: X")
    print("Player 2: O")
    print("Squares are numbered 1-9 (left to right, top to bottom)\n")

    while True:
        display_board(board)

        # Get player move
        move = get_player_move(board, current_player)
        board[move] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins! Congratulations!")
            break

        # Check for draw
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
