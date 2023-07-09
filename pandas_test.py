import pandas as pd
from tabulate import tabulate
import numpy as np
import math


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
    return get_squares_by_row()[r].intersection(get_squares_by_row()[c])


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
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    df = pd.DataFrame(temp)
    return df[r][c]


def square_maker(r, c):
    y = math.floor(r/3)
    x = math.floor(c/3)
    square = square_df(y, x)


def main():
    zeros = [[0 for r in range(9)] for c in range(9)]
    sudoku = pd.DataFrame(zeros)

    for ci in range(9):
        for ri in range(9):
            rand = np.random.randint(1, 10)

            # if column_valid(c, rand) and row_valid(r, rand):


if __name__ == '__main__':
    main()
