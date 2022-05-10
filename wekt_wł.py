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


def get_eigenvalues_eigenvectors(A_):
    Q_, R_ = np.linalg.qr(A)
    next_A = np.round(np.dot(Q_, R_))
    eigenvectors = Q_
    while not check_if_upper_triangular(next_A):
        next_A = np.dot(np.dot(np.transpose(Q_), next_A), Q_)
        Q_, R_ = np.linalg.qr(next_A)
        eigenvectors = (np.dot(eigenvectors, Q_))
    return result(next_A), np.round(eigenvectors)


A = np.array([
    [1, 1, 0],
    [1, 8, 1],
    [0, 1, 1]
])

eigenvalues, eigenvectors = get_eigenvalues_eigenvectors(A)

np.set_printoptions(suppress=True)
print(eigenvalues, "\n")
print(eigenvectors)
