import numpy as np
'''
=============================================================================
Please place the Sudoku Puzzle in the following area and keep the <np,array>
=============================================================================
'''
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
# Let the user enter the size of sudoku puzzle
row_sol = int(input('Please enter the size of the row:'))
col_sol = int(input('Please enter the size of the column:'))

# Define the length of the sudoku puzzle
n = len(puzzle)  # Define the number of rows
m = len(puzzle[0])  # Define the number of columns


# Check whether the value is valid
def is_valid(puzzle, row, col, value):
    # Check that there is no duplicate value in this row
    if value in puzzle[row]:
        return False

    # Check that there is no duplicate value in this column
    if value in puzzle[:,col]:
        return False

    # Check that there is no duplicate value in this subgrid
    subgrid_row = (row // col_sol) * col_sol
    subgrid_col = (col // row_sol) * row_sol
    subgrid = puzzle[subgrid_row:subgrid_row+col_sol, subgrid_col:subgrid_col+row_sol]
    if value in subgrid:
        return False

    return True

# Solve the Sudoku puzzle using backtracking
def solve_sudoku(puzzle):
    # Find an empty cells for the Sudoku puzzle
    for i in range(n):
        for j in range(m):
            if puzzle[i][j] == 0:
                # Try each possible value in the cell
                for k in range(1, row_sol*col_sol+1):
                    if is_valid(puzzle, i, j, k):
                        puzzle[i][j] = k
                        if solve_sudoku(puzzle):
                            #print('Put ' + str(puzzle[i][j]) + ' in location(' + str(i + 1) + ',' + str(j + 1) + ')')
                            return True
                        puzzle[i][j] = 0
                return False
    return True


# Call the solve_sudoku function to show the final answer
if solve_sudoku(puzzle):
    print(puzzle)
    print("Sudoku solved!")

else:
    print("Unable to solve the Sudoku puzzle.")
