import numpy as np
import math


def open_file(filename):
    lista = []
    with open(filename, 'r') as auData:
        for line in auData:
            kolekcja = line.replace('\n', '').split()
            wynik = list(map(lambda e: float(e), kolekcja))
            lista.append(wynik)
    for i in lista:
        i.pop()
    return lista


def euclidean_distance_vectors(listA, listB, cut=False):
    if cut == True:
        listA = listA[:-1]
        listB = listB[:-1]
    v1 = np.array(listA)
    v2 = np.array(listB)
    c = v1 - v2
    return math.sqrt(np.dot(c, c))


def mean(list):
    sum = np.zeros(len(list[0]))
    for i in list:
        sum += np.array(i)
    return sum / len(list)


def st_deviation(list):
    sum = np.zeros(len(list[0]))
    mean_value = mean(list)
    for i in list:
        sum += (np.array(i) - mean_value) ** 2

    return sum / len(list)**(1/2)


def variation(list):
    sum = np.zeros(len(list[0]))
    mean_value = mean(list)
    for i in list:
        sum += (np.array(i) - mean_value) ** 2
    return sum / len(list)-1


list = open_file('australian.dat')
dist_0_1 = euclidean_distance_vectors(list[0], list[1])
mean_ = mean(list)
st_deviation_ = st_deviation(list)
variation_ = variation(list)
