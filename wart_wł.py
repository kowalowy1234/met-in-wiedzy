import numpy as np


def wartWlasne(Q, A):
    Qinv = np.linalg.inv(Q)
    # return np.dot(np.dot(Qinv, A), Q)
    return Qinv


Q = np.array(
    [
        [0.707, -0.408, 0.577],
        [0, 0.816, 0.577],
        [0.707, 0.408, -0.577]
    ]
)

A = np.array(
    [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]
)

print(wartWlasne(Q, A))
