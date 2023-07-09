import pandas as pd
import numpy as np
from tabulate import tabulate
sudoku = [
    [0, 2, 5, 6, 3, 1, 8, 4, 7],
    [6, 1, 8, 5, 0, 4, 2, 9, 3],
    [3, 7, 4, 9, 8, 2, 5, 0, 1],
    [7, 4, 9, 8, 2, 6, 0, 3, 5],
    [8, 5, 2, 4, 1, 0, 9, 7, 6],
    [1, 6, 0, 7, 9, 5, 4, 8, 2],
    [2, 0, 7, 3, 5, 9, 6, 1, 4],
    [4, 9, 1, 0, 6, 7, 3, 5, 8],
    [5, 3, 6, 1, 4, 8, 7, 2, 0]
]

df = pd.DataFrame(sudoku)
df.index = np.arange(1, len(df) + 1)
df.columns = np.arange(1, len(df) + 1)


def get_row(cell):
    return cell[0]


def get_column(cell):
    return cell[1]


index_to_square = {
    0: [0],
    1: [0],
    2: [0
        ]
}

square1 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
square2 = [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
square3 = [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]]
square4 = [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]]
square5 = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]]
square6 = [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]]
square7 = [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]]
square8 = [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]]
square9 = [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]
squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]


def get_square(cell):
    for square_index, square in enumerate(squares):
        for i in square:
            if cell == i:
                return square_index+1


def check_row(row, cell):
    for i in row:
        if df.iloc(cell) == i:
            return False
    return True

def check_column(column, cell):
    for i in column:
        if df.iloc(cell) == i:
            return False
    return True


def check_square(square, cell):
    for i in squares[square-1]:
        if df.iloc(cell) == i:
            return False
    return True



def check_cell(num, cell):
    row = get_row(cell)
    column = get_column(cell)
    square = get_square(cell)
    row_valid = check_row(row, cell)
    column_valid = check_column(column, cell)
    square_valid = check_square(square, cell)
    if row_valid and column_valid and square_valid:
        return True
    return False


def fill_cells(cells):
    filled_cells = []
    for cell in cells:
        for i in range(1, 10):
            cell_valid = check_cell(i, cell)
            if cell_valid:
                cell = i
                filled_cells.append(cell)
    return filled_cells


def check_0(board):
    empty_cells = []
    for i in range(0, 9):
        for j in range(0, 9):
            if df.iat[i, j] == 0:
                empty_coords = [i, j]
                empty_cells.append(empty_coords)
    return empty_cells


def solve_sudoku(board):
    cells_to_fill = check_0(board)
    fill_cells(cells_to_fill)


if __name__ == '__main__':
    #test = [6, 7]
    #print(check_square(1, test))
    print(df[2])

    #solve_sudoku(sudoku)
