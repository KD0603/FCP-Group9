# -*- coding: utf-8 -*-
"""
Created on Tue May  2 00:02:41 2023

@author: Samwi
"""

import argparse
import numpy as np

==================================================================
For 3×3 Sudoku puzzle: subgrid rows is 3 and subgrid columns is 3
For 3×2 Sudoku puzzle: subgrid rows is 2 and subgrid columns is 3
==================================================================

#User will need to input some information of the sudoku
row_sol = int(input('The row to solve:'))
col_sol = int(input('The column to solve:'))

#This paragraph explains why the code will need a --explain in the configuration to work 
def parse_args():
    parser = argparse.ArgumentParser(description='Solve a Sudoku puzzle.')
    parser.add_argument('--explain', action='store_true', help='Provide step-by-step instructions for solving the Sudoku puzzle.')
    return parser.parse_args()

def solve_sudoku(puzzle, explain=False, step=0):
# Find an empty cell
    for i in range(puzzle.shape[0]):
        for j in range(puzzle.shape[1]):
            if puzzle[i][j] == 0:
                # Try each possible value in the cell
                for k in range(1, puzzle.shape[0]+1):
                    if is_valid(puzzle, i, j, k):
                        puzzle[i][j] = k
                        if explain:
                            step += 1
                            print(f"Step {step}: Place {k} in row {i+1}, column {j+1}")
                            print(puzzle)
                        if solve_sudoku(puzzle, explain, step):
                            return True
                        puzzle[i][j] = 0
                return False
    return True

def is_valid(puzzle, row, col, value):
 # Check if the numbers input by the user is valid, return if the number is not
    if value in puzzle[row]:
        return False

    if value in puzzle[:,col]:
        return False

    subgrid_row = (row // row_sol) * row_sol
    subgrid_col = (col // col_sol) * col_sol
    subgrid = puzzle[subgrid_row:subgrid_row+row_sol, subgrid_col:subgrid_col+col_sol]
    if value in subgrid:
        return False

    return True

def main():
    args = parse_args()

    # Define the puzzle
=============================================================================
Please place the Sudoku Puzzle in the following area and keep the <np,array>.  
=============================================================================
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

    # Solve the puzzle
    if solve_sudoku(puzzle, args.explain):
        print("Sudoku solved!")
        print(puzzle)
    else:
        print("Unable to solve the Sudoku puzzle.")

if __name__ == '__main__':
    main()


