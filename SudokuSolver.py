import math
import random
import time

import pandas as pd
from tabulate import tabulate


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
    return df.iloc[r].to_list()


def get_column(df, c):
    return df[c]


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
    column_values = df[c].tolist()
    return [x for x in column_values if x != 0]


def get_nums(row, column, df, squares):
    av_nums = numbers().difference(
        numbers_in_square(row, column, squares),
        numbers_in_row(df, row),
        numbers_in_column(df, column)
    )
    av_nums_list = list(av_nums)
    # print('what my length ',av_nums_list)
    # print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    random.shuffle(av_nums_list)
    return av_nums_list


def fill_cell(df, row, column, value, squares):

    if column_valid(df, column, value) and row_valid(df, row, value) and square_valid(row, column, value, squares):
        df.iloc[row, column] = value
        squares[square_maker(row, column)].append(value)
        return True
    return False


def solve_sudoku():
    if sudoku.iloc[ci, ri] == 0:
        if len(get_nums(ri, ci, sudoku, squares)) == 0:
            av_nums = get_nums(ri, ci, sudoku, squares)
            if ci == 0:
                av_nums1 = get_nums(ci, ri - 1, sudoku, squares)
                fill_cell(sudoku, ci, ri - 1, av_nums1[0], squares)
            else:
                av_nums2 = get_nums(ci - 1, ri, sudoku, squares)
                fill_cell(sudoku, ri, ci - 1, av_nums2[0], squares)
            fill_cell(sudoku, ci, ri, av_nums, squares)


def main():
    start_time = time.time()
    zeros = [[0 for r in range(9)] for c in range(9)]
    sudoku = pd.DataFrame(zeros)
    squares = get_squares()
    for ri in range(9):
        for ci in range(9):


    print(tabulate(sudoku, headers='keys', tablefmt='fancy_grid'))
    elapsed_time = time.time() - start_time
    print(f'Elapsed time: {elapsed_time:.5f} seconds')


if __name__ == '__main__':
    main()
