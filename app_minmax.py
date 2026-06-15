"""Tic Tac Toe game with AI using minimax algorithm."""

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


def get_player_move(board):
    while True:
        try:
            choice = input("Your turn (choose a square 1-9): ").strip()
            index = int(choice) - 1
            if index < 0 or index >= len(board):
                print("Please choose a number between 1 and 9.")
                continue
            if board[index] != " ":
                print("That square is already taken. Choose another one.")
                continue
            return index
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9.")


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm to find the best move.
    - is_maximizing: True for computer (O), False for human (X)
    - Returns: score (1 if O wins, -1 if X wins, 0 for draw)
    """
    winner = check_winner(board)
    
    # Base cases
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(board):
        return 0
    
    if is_maximizing:
        # Computer's turn - maximize score
        max_score = float("-inf")
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                max_score = max(score, max_score)
        return max_score
    else:
        # Human's turn - minimize score
        min_score = float("inf")
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                min_score = min(score, min_score)
        return min_score


def get_computer_move(board):
    """
    Computer makes the best move using minimax algorithm.
    Returns the index of the best move.
    """
    best_score = float("-inf")
    best_move = None
    
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move


def main():
    board = create_board()

    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O")
    display_board(board)

    while True:
        # Human player move
        move = get_player_move(board)
        board[move] = "X"
        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins! {'You won!' if winner == 'X' else 'Computer won!'}")
            break

        if is_draw(board):
            print("It's a draw! No more moves left.")
            break

        # Computer move
        print("Computer is thinking...")
        move = get_computer_move(board)
        board[move] = "O"
        print(f"Computer chose square {move + 1}")
        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins! {'You won!' if winner == 'X' else 'Computer won!'}")
            break

        if is_draw(board):
            print("It's a draw! No more moves left.")
            break


if __name__ == "__main__":
    main()
