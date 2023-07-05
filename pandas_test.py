import pandas as pd
from tabulate import tabulate
import numpy as np
Sudoku_Board = [
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
if __name__ == '__main__':
    df = pd.DataFrame(Sudoku_Board)
    df.index = np.arange(1, len(df) + 1)
    df.columns = np.arange(1, len(df) + 1)
    #print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    empty_cells = []
    for row in Sudoku_Board:
        for cell in row:
            if cell == 0:
                empty_cells.append(df.iloc(cell))
    print(empty_cells)