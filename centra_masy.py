import math
import random
from collections import defaultdict


def load_file(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista


def print_arr(tab):
    for i in range(len(tab)):
        print(tab[i])


def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b) ** 2
    return math.sqrt(wynik)


def random_klasa_decyzyjna(tab):
    # nadanie randomowej klasy decyzyjnej
    for i in range(len(tab)):
        tab[i][len(tab[0])-1] = random.randint(0, 1)


def grupowanie_po_klasach_dezyjnych(tab):
    """
    Funkcja tworzy słownik pogrupowanych wierszy po klasie decyzyjnej.
    :param tab:
    :return: {klasa_decyzyjna: [wiersze]}
    """
    slownik = defaultdict(list)
    for i in range(len(tab)):
        klasa_decyzyjna = (tab[i][len(tab[0])-1])
        slownik[klasa_decyzyjna].append(tab[i])
    return slownik


def suma_metryk(target, tab):
    """
    Funkcja liczy sumę odległości dla pojedyńczego wiersza
    :param target: wiersz, od którego liczone są odległości
    :param tab: tablica
    :return: suma odległości
    """
    suma = 0
    for i in range(len(tab)):
        suma += metryka_euklidesowa_wektory(target, tab[i])
    return suma


def minimalna_metryka(slownik):
    """
    Funkcja tworzy słownik z minimami sum metryk euklidesowych
    :param slownik: słownik grup
    :return: {klasa_decyzyjna: (wiersz, index_wiersza)}
    """
    slownik_minima = {}
    for key in slownik:
        wiersz = slownik[key][0]
        suma_minimum = suma_metryk(slownik[key][0], slownik[key])
        for i in range(len(slownik[key])):
            suma = suma_metryk(slownik[key][i], slownik[key])
            if suma < suma_minimum:
                suma_minimum = suma
                wiersz = slownik[key][i]
        slownik_minima[key] = wiersz
    return slownik_minima


def kolorowanie(slownik_minim, slownik_pogrupowany):
    """
    Funkcja, która zmienia klasy decyzyjne.

    Sprawdza, do której minimalnej sumy metryki euklidesa ma bliżej dany wiersz z danej grupy.
    Jeżeli wiersz ma 'bliżej' do innej klasy decyzyjnej, to zmienia klasę decyzyjną
    """
    licznik_zmian = 0
    zmiana = False
    nowy_slownik_pogrupowany = defaultdict(list)
    for klasa_decyzyjna in slownik_pogrupowany:
        for i in range(len(slownik_pogrupowany[klasa_decyzyjna])):
            wiersz = slownik_pogrupowany[klasa_decyzyjna][i]
            minimum = 0
            tmp = True
            kd = next(iter(slownik_minim))  # pierwsza klasa decyzyjna w slownk_minum
            for key in slownik_minim:
                suma = metryka_euklidesowa_wektory(wiersz, slownik_minim[key])
                if tmp:
                    minimum = suma
                    tmp = False
                elif suma < minimum:
                    minimum = suma
                    kd = key

            if wiersz[len(wiersz) - 1] != kd:  # aby nie robić powtórzeń, jeżeli klasa decyzyjna wiersza == kd
                wiersz[len(wiersz) - 1] = kd
                zmiana = True
                licznik_zmian += 1

            nowy_slownik_pogrupowany[wiersz[len(wiersz)-1]].append(wiersz)
    return nowy_slownik_pogrupowany, zmiana, licznik_zmian


def hephaestus(plik):
    dane = load_file(plik)
    random_klasa_decyzyjna(dane)
    dane_pogrupowane = grupowanie_po_klasach_dezyjnych(dane)

    slownik_minim_tmp = minimalna_metryka(dane_pogrupowane)
    dane_pokolorowane_pogrupowane, zmiana, licznik = kolorowanie(slownik_minim_tmp, dane_pogrupowane)
    # print(dane_pokolorowane_pogrupowane)
    for i in range(200):
        slownik_minim = minimalna_metryka(dane_pokolorowane_pogrupowane)
        dane_pokolorowane_pogrupowane, zmiana, licznik = kolorowanie(slownik_minim, dane_pokolorowane_pogrupowane)
        # print(f'Pętla: {i}')
        # print(f'Minimalne wiersze: {slownik_minim}')
        # print(f'Licznik zmian w kolorowaniu: {licznik}')
        # print(f'Aktualne dane: {dane_pokolorowane_pogrupowane}')
        if not zmiana:
            break
    return dane_pokolorowane_pogrupowane


def zgodnosc(oryginal, hep):
    o = grupowanie_po_klasach_dezyjnych(oryginal)
    zgodnosc = 0
    for key in o:
        for wiersz in hep[key]:
            if wiersz in o[key]:
                zgodnosc += 1
    return (zgodnosc/len(oryginal))*100

#  ======================
slownik = hephaestus('australian.dat')
print('============== Wynik Hephaestus ==============')
for k in slownik:
    print(f'Klasa decyzyjna: {k}: {slownik[k]}')
oryginal = load_file('australian.dat')
print(f'Zgodność z oryginałem: {zgodnosc(oryginal, slownik)}%')

