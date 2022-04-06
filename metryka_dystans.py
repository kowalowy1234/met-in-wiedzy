import math
import numpy as np


def MetrykaEuklidesowa(lista0, listaX):
    dist = 0
    for i in range(0, len(lista0) - 1):
        dist += (lista0[i] - listaX[i]) ** 2
    return math.sqrt(dist)


def MetrykaNaWektorach(lista0, listaX):
    return math.sqrt(sum((e1 - e2) ** 2 for e1, e2 in zip(lista0, listaX)))


def distancePairs(x, list):
    pairs = []
    for i in list:
        decisive = i[-1]
        distance = MetrykaEuklidesowa(x, i)
        pairs.append((decisive, distance))
    return pairs


def sortDistances(pairs):
    keys = []

    for i in pairs:
        keys.append(i[0])

    keySet = set(keys)
    dict = {}

    for i in keySet:
        dict[i] = []

    for i in pairs:
        dict[i[0]].append(i[1])

    return dict


def shortestDistances(dict, x):
    for i in range(len(dict)):
        dict[i] = sorted(dict[i])
        dict[i] = dict[i][:x]
        sum = 0
        for j in range(len(dict[i])):
            sum += dict[i][j]
        dict[i] = sum
    return dict


lista = []

with open('australian.dat', 'r') as auData:
    for line in auData:
        kolekcja = line.replace('\n', '').split()
        wynik = list(map(lambda e: float(e), kolekcja))
        lista.append(wynik)

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
pairs = distancePairs(x, lista)

dict = sortDistances(pairs)

decision = shortestDistances(dict, 5)
print(decision)
