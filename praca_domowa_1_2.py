from copy import deepcopy


def zmniejszMacierz(macierz, wiersz, kolumna):
    nowa_macierz = deepcopy(macierz)
    nowa_macierz.remove(nowa_macierz[wiersz])
    for i in range(len(nowa_macierz)):
        nowa_macierz[i].remove(nowa_macierz[i][kolumna])
    return nowa_macierz


def wyznacznik(macierz):
    rozmiar = len(macierz)
    if rozmiar == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    else:
        wynik = 0
        for i in range(len(macierz)):
            rozwiniecie = (-1) ** i * macierz[0][i] * wyznacznik(zmniejszMacierz(macierz, 0, i))
            wynik += rozwiniecie
        return wynik


macierz = [
    [-1, 2, 1],
    [3, -1, 0],
    [1, -2, 3]
]

print(wyznacznik(macierz))
