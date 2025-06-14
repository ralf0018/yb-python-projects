'''Define a tic-tac-toe game'''
import random

def new_board():
    """Create a new Tic-tac-toe board."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def display(board):
    """Display the Tic-tac-toe board."""
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 9)

def get_O_or_X():
    """Get the player's choice of O or X."""
    while True:
        choice = input("Choose your marker (O or X): ").upper()
        if choice in ['O', 'X']:
            return choice
        print("Invalid choice. Please choose O or X.")

def game_over(board):
    """Check if the game is over."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(cell != ' ' for row in board for cell in row)

def other_player(player):
    """Return the other player."""
    return 'O' if player == 'X' else 'X'

def play_one_turn(board, current_player, human_player):
    if current_player == human_player:
        make_human_move(board, current_player)
    else:
        make_computer_move(board, current_player)

def make_human_move(board, current_player):
    """Make a move for the human player."""
    while True:
        try:
            move = input(f"Player {current_player}, enter your move (row and column, e.g., 1 2): ")
            row, col = map(int, move.split())
            row -= 1  # Adjust for 0-indexing
            col -= 1  # Adjust for 0-indexing
            
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = current_player
                return
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter valid row and column numbers between 1 and 3.")

def make_computer_move(board, current_player):
    """Make a move for the computer player."""
    candidates = empty_squares(board)
    choice = random_in_range(0, len(candidates))
    row, col = candidates[choice]
    board[row][col] = current_player

def empty_squares(board):
    """Return a list of empty squares on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def random_in_range(start, end):
    """Return a random integer in the range [start, end)."""
    return random.randint(start, end - 1)

def play_game(board, human_player):
    """Play a Tic-tac-toe game."""
    current_player = human_player
    while not game_over(board) and not is_board_full(board):
        display(board)
        play_one_turn(board, current_player, human_player)
        
        if game_over(board):
            display(board)
            if current_player == human_player:
                return "win"
            else:
                return "lose"
        
        if is_board_full(board):
            display(board)
            return "draw"
        
        current_player = other_player(current_player)   
        
def print_result(outcome):
    """Print the result of the game."""
    if outcome == "win":
        print("Congratulations! You win!")
    elif outcome == "lose":
        print("Sorry, you lose. Better luck next time!")
    else:
        print("It's a draw!")
   

def main():
    board = new_board()
    human_player = get_O_or_X()
    outcome = play_game(board, human_player)
    print_result(outcome)
    
if __name__ == "__main__":
    main()