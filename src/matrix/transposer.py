import numpy as np

MAIN_DIAG = 1
SIDE_DIAG = 2
VERTICAL_LINE = 3
HORIZONTAL_LINE = 4


def transpose(matrix: np.ndarray, mode: int) -> np.ndarray:
    if mode == MAIN_DIAG:
        return matrix.transpose()
    elif mode == SIDE_DIAG:
        return np.rot90(matrix, 2).transpose()
    elif mode == VERTICAL_LINE:
        return np.flip(matrix, axis=1)
    elif mode == HORIZONTAL_LINE:
        return np.flip(matrix, axis=0)
    else:
        return matrix
