import numpy as np


def create_diag(sigmas, shape):
    result = np.zeros(shape)
    for i in range(0, len(result)):
        for j in range(0, len(result[i])):
            if i == j:
                result[i][j] = sigmas[i]
    return result


def get_u(eigenvalues, left_a):
    U = []
    for i in range(len(eigenvalues)):
        lambda_i = np.eye(np.shape(left_a)[0]) * eigenvalues[i]
        temp_left_a = left_a - lambda_i
        v = np.linalg.eig(temp_left_a)[1]
        U.append(v / np.linalg.norm(v))
    return np.array(U)


def get_v(a, u, sigmas):
    V = []
    for i in range(len(sigmas)):
        if sigmas[i] != 0:
            v = np.dot(np.transpose(a), u[i]) / sigmas[i]
            V.append(v)
        else:



def svd(A):
    left_A = np.dot(A, np.transpose(A))
    left_eigenvalues = np.linalg.eigvals(left_A)
    sigmas = np.ndarray.sort(np.sqrt(left_eigenvalues))
    create_diag(sigmas, np.shape(A))
    Sigma = create_diag(sigmas, np.shape(A))
    U = get_u(left_eigenvalues, left_A)
    right_A = np.dot(np.transpose(A), A)
    right_eigenvalues = np.ndarray.sort(np.linalg.eigvals(left_A))

A = np.array([
    [1, 2, 0],
    [2, 0, 2]
])

svd(A)

np.printoptions(supress=True)
U, Sig, V = np.linalg.svd(A)
print(U)
# print(Sig)
# print(V)
