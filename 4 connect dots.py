def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in reversed(board):
        print(row)

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for row in range(6):
        if board[row][col] == 0:
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    
    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    
    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    
    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    
    return False

def play_game():
    board = create_board()
    game_over = False
    turn = 0
    
    while not game_over:
        print_board(board)
        col = int(input(f"Player {turn+1} (1-7): ")) - 1
        
        if 0 <= col <= 6 and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn + 1)
            
            if winning_move(board, turn + 1):
                print_board(board)
                print(f"PLAYER {turn+1} WINS!")
                game_over = True
            
            turn = (turn + 1) % 2
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
