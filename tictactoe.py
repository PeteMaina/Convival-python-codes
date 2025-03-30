def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, enter your move (row and column: 0 1): ")
        
        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers (0-2).")
            continue
        
        board[row][col] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins! 🎉")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
