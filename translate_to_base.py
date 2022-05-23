import numpy as np
import math


def check_if_diag(b):
    new_b = np.dot(np.transpose(b), b)
    is_diag = True

    for i in range(0, len(new_b)):
        for j in range(0, len(new_b[i])):
            if j != i and new_b[i][j] != 0:
                is_diag = False
    return is_diag


def diag_norm(b):
    result = []
    new_b = np.transpose(b)
    for i in new_b:
        norm = math.sqrt(np.dot(i, i))
        result.append((i/norm))
    # diag = np.dot(np.transpose(result), result)
    return result


B = np.array([
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, -1, 0, 0, 0],
    [1, 1, -1, 0, 0, 1, 0, 0],
    [1, 1, -1, 0, 0, -1, 0, 0],
    [1, -1, 0, 1, 0, 0, 1, 0],
    [1, -1, 0, 1, 0, 0, -1, 0],
    [1, -1, 0, -1, 0, 0, 0, 1],
    [1, -1, 0, -1, 0, 0, 0, -1],
])


x_a = np.array([8, 6, 2, 3, 4, 6, 6, 5])
ort_normal = diag_norm(B)
print(np.round(ort_normal, 2))
x_b = np.round(np.dot(ort_normal, x_a), 2)
print(x_b)