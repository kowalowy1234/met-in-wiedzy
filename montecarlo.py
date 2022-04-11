import random
import numpy


def fun(x):
    return x
           # * x + 3


def monte_carlo_method(start_range, end_range, points):
    integral = 0
    dx = end_range - start_range
    for i in range(points):
        integral += fun(start_range + random.uniform(0, dx))
    integral *= dx / points
    return integral


def rectangle_method(start_range, end_range, points):
    bases = numpy.linspace(start_range, end_range, points)
    dx = (bases[-1] - bases[0]) / points
    integral = 0
    for i in range(len(bases)):
        integral += dx * fun(bases[i])
    return integral


print(monte_carlo_method(0, 1, 1000))
print(rectangle_method(0, 1, 1000))

