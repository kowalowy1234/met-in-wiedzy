import math

import numpy as np


def proj(u, v):
    return (np.dot(v, u) / np.dot(u, u)) * u


def norm(v):
    return math.sqrt(np.dot(np.transpose(v), v))


def u_to_e(u):
    return u / norm(u)


def generate_Q(A):
    U = [A[0]]
    for i in range(1, len(A)):
        v_i = A[i]
        u_i = v_i - proj(A[i - 1], v_i)
        U.append(u_i)
    Q = []
    for i in U:
        Q.append(u_to_e(i))
    return np.array(Q)


def generate_R(Q, A):
    return np.dot(Q, np.transpose(A))


def generate_A(Q, R):
    return np.dot(np.transpose(Q), R)


A = np.array([
    [1, 1, 0],
    [0, 1, 1],
])
Q = generate_Q(A)
R = generate_R(Q, A)
print(np.transpose(Q))
print(R)
