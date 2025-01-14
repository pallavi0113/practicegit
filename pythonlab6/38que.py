# Initialize an m×n game board
def initialize_board(m, n):
    return [[' ' for _ in range(n)] for _ in range(m)]

# Print the current game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

# Check if a player has won
def check_winner(board, m, n, k, player):
    # Horizontal check
    for i in range(m):
        for j in range(n - k + 1):
            if all(board[i][j + x] == player for x in range(k)):
                return True

    # Vertical check
    for i in range(m - k + 1):
        for j in range(n):
            if all(board[i + x][j] == player for x in range(k)):
                return True

    # Diagonal check (top-left to bottom-right)
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            if all(board[i + x][j + x] == player for x in range(k)):
                return True

    # Diagonal check (top-right to bottom-left)
    for i in range(m - k + 1):
        for j in range(k - 1, n):
            if all(board[i + x][j - x] == player for x in range(k)):
                return True

    return False

# Game loop
def play_game(m, n, k):
    board = initialize_board(m, n)
    current_player = 'X'
    
    total_moves = m * n
    move_count = 0

    while move_count < total_moves:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get valid user input
        while True:
            try:
                row = int(input(f"Enter the row (0-{m-1}): "))
                col = int(input(f"Enter the column (0-{n-1}): "))
                if board[row][col] == ' ':
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print(f"Invalid input. Please enter row (0-{m-1}) and column (0-{n-1}).")

        # Place the stone on the board
        board[row][col] = current_player
        move_count += 1
        
        # Check if the current player has won
        if check_winner(board, m, n, k, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

    # If the board is full and no winner, it's a draw
    print_board(board)
    print("The game is a draw.")

# Start the game with user-defined board size and k value
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
k = int(input("Enter the number of consecutive stones to win (k): "))

play_game(m, n, k)
