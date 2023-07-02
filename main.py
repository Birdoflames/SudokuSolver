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
columns = [
    column1 = [],
    column2,
    column3,
    column4,
    column5,
    column6,
    column7,
    column8,
    column9s
]
for row in Sudoku_Board:
    for i in range(0 - 9):
        current_column = columns[i+1]
        current_column.append(row[i])

print(columns)

# todo: get input
# todo: define rows, columns and 3*3 squares
# todo: check what numbers are 0's
# todo: create function to check if a number is valid
# todo: on each 0 go one by one till sudoku is solved
# todo: deal with cases in which there is more than one option
