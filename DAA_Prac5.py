def print_board(board):
    n = len(board)
    for row in board:
        print(" ".join(row))
    print()

# Check if a queen can be placed at (row, col)
def is_safe(board, row, col):
    n = len(board)
    
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Backtracking function to place queens
def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        # All queens placed
        print("One of the solutions:")
        print_board(board)
        return True  # return True to find one solution, False to find all solutions

    for col in range(n):
        if board[row][col] != '.':
            # Skip the cell if already has first queen placed
            continue
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = '.'  # backtrack

    return False

# -------- Main Program --------
if __name__ == "__main__":
    n = int(input("Enter size of the board (n): "))
    first_row = int(input(f"Enter row of first queen (0 to {n-1}): "))
    first_col = int(input(f"Enter column of first queen (0 to {n-1}): "))

    # Initialize board
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[first_row][first_col] = 'Q'  # place first queen

    # Start solving from row 0 (skip the row if first queen is placed there)
    start_row = 0 if first_row != 0 else 1
    if not solve_n_queens(board, start_row):
        print("No solution exists for the given first queen position.")
