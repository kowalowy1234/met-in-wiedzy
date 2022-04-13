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
print("Wektor: "+str(list))
print("Średnia: " +str(mean(list)))
print("Wariancja: " +str(variation(list)))
print("Odchylenie standardowe: " +str(st_deviation()))
