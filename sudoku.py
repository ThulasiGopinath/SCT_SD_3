def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_valid(grid, row, col, num):
    # Check if 'num' is not in the given row and column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    
    # Check if 'num' is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Puzzle solved
    row, col = empty_cell

    for num in range(1, 10):  # Numbers 1-9
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Place the number

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Backtrack

    return False  # Trigger backtracking

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # Return the row and column of the empty cell
    return None

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku Puzzle:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
