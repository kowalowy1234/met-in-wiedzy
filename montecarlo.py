import random
import numpy


def fun(x):
    return x


def monte_carlo_method(start_range, end_range, points):
    integral = 0

    # Wyznaczamy długość przedziału całkowania
    dx = end_range - start_range

    # Wyznaczamy sumę wartości losowo wybranych punktów w funkcji
    for i in range(points):
        integral += fun(start_range + random.uniform(0, dx))

    # Wartość całki to iloczyn sumy wartości funkcji
    # w losowo wybranych punktach z przedziału całkowania
    # i długości przedziału całkowania
    # podzielona przez ilość losowo wyznaczonych punktów
    # w przedziale całkowania
    integral *= dx / points
    return integral


def rectangle_method(start_range, end_range, points):
    # Podział na równe podstawy
    bases = numpy.linspace(start_range, end_range, points)

    # Odległosć między dwoma sąsiednimi punktami
    dx = (bases[-1] - bases[0]) / points
    integral = 0

    # Dla każdego punktu wyznaczamy wartość funkcji w tym punkcie
    # i obliczamy sumę iloczynów wyznaczonych wartości (wysokość prostokąta)
    # przez długość każdej podstawy (szerokość prostokąta)
    # co daje nam sumę pól prostokątnych, tym samym przybliżoną wartość całki oznaczonej

    for i in range(len(bases)):
        integral += dx * fun(bases[i])
    return integral


print(monte_carlo_method(0, 1, 1000))
print(rectangle_method(0, 1, 10))
