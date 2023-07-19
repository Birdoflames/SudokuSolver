import pandas as pd
from tabulate import tabulate
import numpy as np
import math
import random
import time


def get_squares_by_column():
    return {
        0: {1, 4, 7},
        1: {1, 4, 7},
        2: {1, 4, 7},
        3: {2, 5, 8},
        4: {2, 5, 8},
        5: {2, 5, 8},
        6: {3, 6, 9},
        7: {3, 6, 9},
        8: {3, 6, 9}
    }


def get_squares_by_row():
    return {
        0: {1, 2, 3},
        1: {1, 2, 3},
        2: {1, 2, 3},
        3: {4, 5, 6},
        4: {4, 5, 6},
        5: {4, 5, 6},
        6: {7, 8, 9},
        7: {7, 8, 9},
        8: {7, 8, 9}
    }


def get_row(df, r):
    row = []
    for i in df.iloc[r].tolist():
        if type(i) == list:
            row.append(0)
        else:
            row.append(i)
    return row


def get_column(df, c):
    col = []
    for i in df[c].tolist():
        if type(i) == list:
            col.append(0)
        else:
            col.append(i)
    return col


def get_square(r, c):
    return list(get_squares_by_column()[c].intersection(get_squares_by_row()[r]))


def row_valid(df, r, num):
    if num not in get_row(df, r):
        return True
    return False


def column_valid(df, c, num):
    if num not in df[c].to_list():
        return True
    return False


def square_df(r, c):
    temp = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    df = pd.DataFrame(temp)
    return df.iloc[r, c]


def get_squares():
    return {
        0: [], 1: [], 2: [],
        3: [], 4: [], 5: [],
        6: [], 7: [], 8: [],
    }


def square_maker(r, c):
    y = math.floor(r / 3)
    x = math.floor(c / 3)
    square = square_df(y, x)
    return square


def square_valid(row, column, value, squares):
    square = square_maker(row, column)
    for item in squares[square]:
        if item == value:
            return False
    return True


def numbers():
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}


def numbers_in_square(row, column, squares):  # squares = dict of squares
    square = square_maker(row, column)  # square number
    current_square = squares[square]
    current_square_nums = [x for x in current_square if x != 0]
    return current_square_nums


def numbers_in_row(df, r):
    row = get_row(df, r)
    row = [x for x in row if x != 0]
    return row


def numbers_in_column(df, c):
    column_values = get_column(df, c)
    return [x for x in column_values if x != 0]


def get_nums(row, column, df, squares):
    square_nums = set(get_square(row, column))
    row_nums = set(get_row(df, row))
    col_nums = set(get_column(df, column))
    av_nums = numbers().difference(
        square_nums,
        row_nums,
        col_nums
    )
    av_nums_list = list(av_nums)
    # print('what my length ',av_nums_list)
    # print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    # random.shuffle(av_nums_list)
    # print(av_nums_list)
    return av_nums_list


def fill_cell(df, row, column, value, squares):

    if column_valid(df, column, value) and row_valid(df, row, value) and square_valid(row, column, value, squares):
        df.iloc[row, column] = value
        squares[square_maker(row, column)].append(value)
        return True
    return False


def get_square_coords(r, c, s):
    coords = []
    for c in range(9):
        for r in range(9):
            if square_maker(r, c) == s:
                coords.append([r, c])
    return coords


def main():
    start_time = time.time()
    df = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for r in range(9)] for c in range(9)]
    sudoku = pd.DataFrame(df)
    squares = get_squares()
    for ci in range(9):
        for ri in range(9):
            nums = get_nums(ri, ci, sudoku, squares)
            min_options_lost = float('inf')
            number_used = None
            for num in nums:
                items_affected_coords = [[0, ci], [1, ci], [2, ci], [3, ci], [4, ci], [5, ci], [6, ci], [7, ci], [8, ci], [ri, 0], [ri, 1], [ri, 2], [ri, 3], [ri, 4], [ri, 5], [ri, 6], [ri, 7], [ri, 8]]
                coords = get_square_coords(ri, ci, get_square(ri, ci)[0])
                for coord in coords:
                    items_affected_coords.append(coord)
                # affected_set = set(items_affected_coords)
                options_lost = 0
                print(items_affected_coords)
                for item in items_affected_coords:
                    options_lost += len(list(sudoku.iloc[item[0], item[1]])) - len(get_nums(item[0], item[1], sudoku, squares))
                if options_lost < min_options_lost:
                    min_options_lost = options_lost
                    number_used = num
                    sudoku.iloc[item[0]][item[1]] = get_nums(item[0], item[1], sudoku, squares)
            if number_used != 0:
                fill_cell(sudoku, ri, ci, number_used, squares)

    print(tabulate(sudoku, headers='keys', tablefmt='fancy_grid'))
    elapsed_time = time.time() - start_time
    print(f'Elapsed time: {elapsed_time:.5f} seconds')


if __name__ == '__main__':
    main()
