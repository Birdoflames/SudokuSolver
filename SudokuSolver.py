import pandas as pd
sudoku = []


def get_row(cell):
    pass


def get_column(cell):
    pass


def get_square(cell):
    pass


def check_row(row, cell):
    pass


def check_column(column, cell):
    pass


def check_square(square, cell):
    pass



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
    for cell in board:
        if cell == 0:
            empty_cells.append(cell)
    return empty_cells


def solve_sudoku(board):
    cells_to_fill = check_0(board)
    fill_cells(cells_to_fill)


if __name__ == '__main__':
    solve_sudoku(sudoku)
