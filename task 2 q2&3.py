import numpy as np
import argparse
'''
=============================================================================
Please place the Sudoku Puzzle in the following area and keep the <np,array>.
=============================================================================
'''
puzzle = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

'''
==================================================================
For 3×3 Sudoku puzzle: subgrid rows is 3 and subgrid columns is 3
For 3×2 Sudoku puzzle: subgrid rows is 2 and subgrid columns is 3
==================================================================
'''
# Let the user enter the size of sudoku puzzle
row_sol = int(input('Please enter the number of the subgrid rows:'))
col_sol = int(input('Please enter the number of the subgrid columns:'))

def print_solution(puzzle):
    print("Solution:")
    for i in range(row_sol*col_sol):
        for j in range(row_sol*col_sol):
            print(puzzle[i][j], end=' ')
        print()

def possible_values(puzzle, row, col):
    if puzzle[row][col] != 0:
        return [puzzle[row][col]]

    values = set(range(1, row_sol*col_sol+1))
    values -= set(puzzle[row,:])   # Check row
    values -= set(puzzle[:,col])   # Check column

    # Check subgrid
    subgrid_row = (row // row_sol) * row_sol
    subgrid_col = (col // col_sol) * col_sol
    subgrid = puzzle[subgrid_row:subgrid_row+row_sol, subgrid_col:subgrid_col+col_sol]
    values -= set(subgrid.flatten())

    return list(sorted(values))


def solve_sudoku(puzzle):
    # Find an empty cell
    for i in range(row_sol*col_sol):
        for j in range(row_sol*col_sol):
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


def hint_sudoku(puzzle, n):
    """
    Given a Sudoku puzzle and an integer N, this function returns a grid with N values filled in.
    """
    solution = puzzle.copy()

    # Find an empty cell
    for i in range(row_sol*col_sol):
        for j in range(row_sol*col_sol):
            if solution[i][j] == 0:
                # Try each possible value in the cell
                values = possible_values(solution, i, j)
                for k in values:
                    solution[i][j] = k
                    if n > 1:
                        # Recursively solve the puzzle until N values are filled in
                        if solve_sudoku(solution):
                            # Found a solution with at least N values filled in
                            if np.count_nonzero(solution) >= (row_sol*col_sol - n):
                                return solution
                            else:
                                # Not enough values filled in, continue searching
                                hint = hint_sudoku(solution, n-1)
                                if hint is not None:
                                    return hint
                    else:
                        # Only need to fill in one value
                        if solve_sudoku(solution):
                            return solution
                # No valid value found, backtrack
                solution[i][j] = 0
    return None

#This code checks if the --hint flag is passed in as a command line argument, and if so, calls the hint_sudoku function 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", nargs=2, metavar=("INPUT", "OUTPUT"), help="solve the Sudoku puzzle in INPUT file and save solution to OUTPUT file")
parser.add_argument("--explain", action="store_true", help="include explanation of the solution in the output")
parser.add_argument("--hint", type=int, metavar="N", help="return a grid with N values filled in")
args = parser.parse_args()


if args.file is not None:
    input_file, output_file = args.file
    puzzle = read_puzzle(input_file)
    if solve_sudoku(puzzle):
        write_puzzle(puzzle, output_file)
        print("Sudoku solved! Solution saved to", output_file)
        if args.explain:
            explain_puzzle(puzzle, input_file, output_file)
    else:
        print("Unable to solve the Sudoku puzzle.")
else:
    # solve the puzzle provided in the code
    if solve_sudoku(puzzle):
        print("Sudoku solved!")
        if args.hint is not None:
            hint_puzzle(puzzle, args.hint)
        else:
            print_solution(puzzle)
            if args.explain:
                explain_puzzle(puzzle)
    else:
        print("Unable to solve the Sudoku puzzle.")
