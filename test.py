import random


def peselRandom(pesel):
    peselChars = [char for char in pesel]
    randomPesel = ''
    for i in range(4):
        randomPesel += str(peselChars[random.randint(0, len(peselChars)-1)])
    return randomPesel


def generuj(imie, nazwisko, pesel):
    imie = str(imie)
    nazwisko = str(nazwisko)
    pesel = str(pesel)
    result = '' + imie[0] + nazwisko + peselRandom(pesel)

    return str(result)


print(generuj('Piotr', 'Kowalski', '091234587'))
