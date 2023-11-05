import numpy as np
from numpy import array

from matrix.menu import Menu, EXIT, LOOP
from matrix.transposer import transpose

MENU = '''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit'''

TRANSPOSE_MENU = '''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line'''


def read_matrix(position: str) -> np.ndarray:
    rows, columns = map(int, input(f'Enter size of{position} matrix: ').split())
    matrix = np.zeros((rows, columns))
    print(f'Enter{position} matrix:')
    for row in range(rows):
        matrix[row] = array(list(map(float, input().split())))
    return matrix


def print_matrix(matrix: np.ndarray):
    print('The result is:')
    for row in matrix:
        print(*map(lambda num: f'{num:.10g}', row))


def mult():
    matrix_a = read_matrix(" first")
    matrix_b = read_matrix(" second")
    if matrix_a.shape[1] != matrix_b.shape[0]:
        print('ERROR')
    else:
        print_matrix(matrix_a @ matrix_b)
    return LOOP


def trans():
    print(TRANSPOSE_MENU)
    mode = int(input("Your choice: "))
    matrix = read_matrix("")
    print_matrix(transpose(matrix, mode))
    return LOOP


def add():
    matrix_a = read_matrix(" first")
    matrix_b = read_matrix(" second")
    if matrix_a.shape != matrix_b.shape:
        print('ERROR')
    else:
        print_matrix(matrix_a + matrix_b)
    return LOOP


def scale():
    matrix = read_matrix("")
    factor = float(input("Enter constant:"))
    print_matrix(factor * matrix)
    return LOOP


def main():
    Menu(MENU, {'1': add, '2': scale, '3': mult, '4': trans, '0': lambda: EXIT}).loop()


if __name__ == '__main__':
    main()
