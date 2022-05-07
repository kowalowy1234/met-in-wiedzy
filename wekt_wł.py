import numpy as np


def get_next_A(Q_, A_):
    return np.dot(np.dot(np.transpose(Q_), A_), Q_)


def check_if_upper_triangular(A_):
    for i in range(1, len(A_)):
        for j in range(0, i):
            if abs(A_[i][j]) > 0.001:
                return False
    return True


def result(A_):
    eigenvalues = []
    for i in range(len(A_)):
        for j in range(len(A_)):
            if i == j:
                eigenvalues.append(A_[i][j])
    return eigenvalues


def get_eigenvalues(A_):
    Q_, R_ = np.linalg.qr(A)
    next_A = np.round(np.dot(Q_, R_))
    while not check_if_upper_triangular(next_A):
        next_A = np.dot(np.dot(np.transpose(Q_), next_A), Q_)
        Q_, R_ = np.linalg.qr(next_A)
    return result(next_A)


A = np.array([
    [1, 1, 0],
    [1, 8, 1],
    [0, 1, 1]
])

eig_values = get_eigenvalues(A)
