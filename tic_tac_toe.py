def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    return (board[0][0] == board[1][1] == board[2][2] == player) or \
           (board[0][2] == board[1][1] == board[2][0] == player)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Invalid move, try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input, try again.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
