import numpy as np
import random


class Board:
    def __init__(self):
        # Initialize an empty Sudoku grid
        self.grid = np.zeros((9, 9), dtype=int)

    def set_value(self, row, col, value):
        # Set the value of a cell in the Sudoku grid
        self.grid[row][col] = value

    def get_value(self, row, col) -> int:
        # Get the value of a cell in the Sudoku grid
        return self.grid[row, col]

    def is_valid_move(self, row, col, value):
        # Check if placing a value in a cell is a valid move
        return (
                self.is_valid_row(row, value) and
                self.is_valid_column(col, value) and
                self.is_valid_subgrid(row, col, value)
        )

    def is_valid_row(self, row, value):
        # Check if placing a value in a row is valid
        return value not in self.grid[row]

    def is_valid_column(self, col, value):
        # Check if placing a value in a column is valid
        return value not in self.grid[:, col]

    def is_valid_subgrid(self, row, col, value):
        # Check if placing a value in a 3x3 subgrid is valid
        subgrid_row_start = (row // 3) * 3
        subgrid_col_start = (col // 3) * 3
        subgrid_values = self.grid[subgrid_row_start:subgrid_row_start + 3, subgrid_col_start:subgrid_col_start + 3]
        return value not in subgrid_values

    def generate_sudoko_puzzle(self):
        grid = np.zeros((9, 9), dtype=int)
        for i in range(3):
            for j in range(3):
                subgrid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for m in range(3):
                    for n in range(3):
                        random.shuffle(subgrid)
                        grid[i * 3 + m][j * 3 + n] = subgrid.pop()

        # Remove all numbers except for 10 to create the puzzle
        remaining_cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(remaining_cells)
        for _ in range(81 - 15):
            row, col = remaining_cells.pop()
            grid[row][col] = 0
        self.grid = grid
        return self.grid

    def generate_empty_sudoko(self):
        self.grid = np.zeros((9, 9), dtype=int)
        return self.grid



def is_valid_sudoku(grid):
    # Check rows and columns
    print("1")
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if grid[i][j] and (grid[i][j] in row or grid[j][i] in col):
                return False
            row.add(grid[i][j])
            col.add(grid[j][i])

    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = set()
            for m in range(3):
                for n in range(3):
                    if grid[i+m][j+n] in subgrid and grid[i+m][j+n]:
                        return False
                    subgrid.add(grid[i+m][j+n])

    return True

