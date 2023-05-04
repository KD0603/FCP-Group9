import copy
import numpy as np
'''
=============================================================================
Please place the Sudoku Puzzle in the following area and keep the <np,array>.  
=============================================================================
'''
puzzle = np.array([
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]
])
'''
==================================================================
For 3×3 Sudoku puzzle: subgrid rows is 2 and subgrid columns is 3
For 3×2 Sudoku puzzle: subgrid rows is 3 and subgrid columns is 3
==================================================================
'''
# Let the user enter the size of sudoku puzzle
row_sol = int(input('Please enter the number of the subgrid row:'))
col_sol = int(input('Please enter the number of the subgrid column:'))

# Define the length of the Sudoku Puzzle
n = len(puzzle)  # Define the number of rows
m = len(puzzle[0]) # Define the number of columns

# To find the empty cells for the sudoku puzzle
def find_empty(puzzle):
    for r in range(n):
        for c in range(m):
            if puzzle[r][c] == 0:
                return r, c
    return None


# Define the function to get the possible values for an empty cell
def find_possible_values(puzzle, row, col):
    values = set(range(1, row_sol*col_sol+1))  # Using set() and discard() to delete the values

    # Check the duplicate value in the rows and columns and delete the values
    for i in range(m):
        values.discard(puzzle[row][i])
        values.discard(puzzle[i][col])

    # Check the duplicate value in this subgrid and delete the values
    sub_row = (row // row_sol) * row_sol
    sub_col = (col // col_sol) * col_sol
    for r in range(sub_row, sub_row + row_sol):
        for c in range(sub_col, sub_col + col_sol):
            values.discard(puzzle[r][c])
    return values


# Check there is no zero
def check(puzzle):
    return all(0 not in row for row in puzzle)


# Using wavefront propagation to solve the sudoku puzzle
def solve_sudoku(puzzle):
    list_n = [puzzle]  # Initialize the list_n with the starting puzzle
    data = []   # Create an empty list to save all the possible answers

    while list_n:
        puzzle_1 = list_n.pop(0)  # Extract the first row of list_n
        if check(puzzle_1):  # Check if it has been resolved
            data.append(puzzle_1)  # If solved, add it to the data list
            continue

        row, col = find_empty(puzzle_1)  # Define the rows and cols for the empty cells
        poss_values = find_possible_values(puzzle_1, row, col)  # Shows the possible_values for the empty cells

        for k in poss_values:
            puzzle_2 = copy.deepcopy(puzzle_1)  # copy the puzzle for now
            puzzle_2[row][col] = k  # Assign the possible values to the empty cells
            list_n.append(puzzle_2)  # add the puzzle_2 into the data list

    return data


# Call the solve_sudoku function to show the final answer
print(solve_sudoku(puzzle))
print('Sudoku Solved!')
