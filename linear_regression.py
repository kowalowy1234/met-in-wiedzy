import numpy as np


def linear_regression(list):
    x_temp = np.array([i[0] for i in list])
    x_transposed = np.array([
        np.ones(len(x_temp)),
        x_temp
    ])
    x = np.transpose(x_transposed)
    y = np.transpose(np.array([i[1] for i in list]))
    x_t_inversed = np.linalg.inv(np.dot(x_transposed, x))
    b = np.dot(x_t_inversed, x_transposed)
    b = np.dot(b, y)
    return b


list = [
    [2, 1],
    [5, 2],
    [7, 3],
    [8, 3],
]

B = linear_regression(list)

print('y = ' + str(B[0]) + ' + ' + str(B[1]) + 'x')