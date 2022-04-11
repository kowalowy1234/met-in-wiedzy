import numpy as np
import math


def euclidean_distance_vectors(listA, listB, cut=False):
    if cut == True:
        listA = listA[:-1]
        listB = listB[:-1]
    v1 = np.array(listA)
    v2 = np.array(listB)
    c = v1 - v2
    return math.sqrt(np.dot(c, c))


def mean(list):
    vectorOnes = np.ones(len(list))
    v1 = np.array(list)
    tmp = np.dot(list, vectorOnes)
    mean_ = tmp / len(list)
    return mean_


def variation(list):
    mean_ = mean(list)
    v1 = np.array(list)
    vectorOnes = np.ones(len(list))
    v2 = v1 - mean_ * vectorOnes
    c = np.dot(v2, v2)
    return c / len(list)


def st_deviation():
    return math.sqrt(variation(list))


list = [1, 2, 5, 6]
print(mean(list))
print(st_deviation())
# print(variation(list))

# def st_deviation(list):
#     sum = np.zeros(len(list[0]))
#     mean_value = mean(list)
#     for i in list:
#         sum += (np.array(i) - mean_value) ** 2
#
#     return sum / len(list)**(1/2)
#
#
# def variation(list):
#     sum = np.zeros(len(list[0]))
#     mean_value = mean(list)
#     for i in list:
#         sum += (np.array(i) - mean_value) ** 2
#     return sum / len(list)-1
#
#
# list = open_file('australian.dat')
# dist_0_1 = euclidean_distance_vectors(list[0], list[1])
# mean_ = mean(list)
# st_deviation_ = st_deviation(list)
# variation_ = variation(list)
