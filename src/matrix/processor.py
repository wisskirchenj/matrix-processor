import numpy as np
from numpy import array


def read_matrix() -> np.ndarray:
    rows, columns = map(int, input().split())
    matrix = np.zeros((rows, columns))
    for row in range(rows):
        matrix[row] = array(list(map(int, input().split())))
    return matrix


def print_matrix(matrix: np.ndarray):
    for row in matrix:
        print(*map(int, row))


def main():
    matrix_a = read_matrix()
    matrix_b = read_matrix()
    if matrix_a.shape != matrix_b.shape:
        print('ERROR')
    else:
        print_matrix(matrix_a + matrix_b)


if __name__ == '__main__':
    main()
