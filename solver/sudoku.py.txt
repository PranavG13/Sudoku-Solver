def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def check(grid, row, col, num):
    for k in range(9):
        if grid[row][k] == num or grid[k][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
            
    return True

def solve_sudoku(grid, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, 10):
        if check(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            
        grid[row][col] = 0  # Backtrack

    return False
