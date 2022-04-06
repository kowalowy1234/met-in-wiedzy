import random
import numpy


def fun(x):
    return x * x + 3


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


print(monte_carlo_method(2, 5, 1000))
print(rectangle_method(2, 5, 10))

# def polynomial(x):
#     return(2xx*2)
#
# def rectangle(low, high, f, N):
#     rectangle_edges=np.linspace(low, high, N)
#     area=0
#     for r in range(len(rectangle_edges)):
#         area+=f(low+r(high-low)/N)(high-low)/N
#     return(area)
# print(rectangle(2, 10, polynomial, 10000))
#
# def montecarlo(low, high, f, N):
#     xrand = numpy.zeros(N)
#     for i in range(len(xrand)):
#         xrand[i] = random.uniform(low, high)
#
#     integral = 0.0
#     for i in range(N):
#         integral += polynomial(xrand[i])
#
#     answer = (high-low)/float(N)
#     return answer
#
# print(montecarlo(0, 10, polynomial, 10000))
