import numpy as np

puzzle = np.array([
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]
])

row_sol = int(input('The number of rows to solve:'))
col_sol = int(input('The number of columns to solve:'))


def is_valid(puzzle, row, col, value):
    # Check row
    if value in puzzle[row]:
        return False
    # Check column
    if value in puzzle[:,col]:
        return False

    # Check subgrid
    subgrid_row = (row // row_sol) * row_sol
    subgrid_col = (col // col_sol) * col_sol
    subgrid = puzzle[subgrid_row:subgrid_row+row_sol, subgrid_col:subgrid_col+col_sol]
    if value in subgrid:
        return False

    return True


## Solve the Sudoku puzzle using backtracking

def solve_sudoku(puzzle):
    # Find an empty cell
    for i in range(len(puzzle)):
        row = puzzle[i]
        for j in range(len(row)):
            if puzzle[i][j] == 0:
                # Try each possible value in the cell
                for k in range(1, row_sol*col_sol+1):
                    if is_valid(puzzle, i, j, k):
                        puzzle[i][j] = k
                        if solve_sudoku(puzzle):
                            return True
                        puzzle[i][j] = 0
                return False
    return True





# Call the solve_sudoku function
if solve_sudoku(puzzle):
    print(puzzle)
    print("Sudoku solved!")
else:
    print("Unable to solve the Sudoku puzzle.")
