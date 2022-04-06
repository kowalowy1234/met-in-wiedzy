import math
import random
import numpy as np


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


def euclidean_distance(list0, listX):
    dist = 0
    for i in range(0, len(list0) - 1):
        dist += (list0[i] - listX[i]) ** 2
    return math.sqrt(dist)


def apply_random_class(list):
    for i in list:
        i.append(float(random.randint(0, 1)))
    return list


def define_empty_dict(classes):
    dict = {}
    for i in range(classes):
        dict[i] = []
    return dict


def group_by_class(list, classes):
    dict = define_empty_dict(classes)
    for i in range(len(list)):
        decisive_class = list[i][-1]
        dict[decisive_class].append(list[i])
    return dict


def sum_of_distances(row, list):
    sum = 0
    for i in list:
        sum += euclidean_distance(row, i)
    return sum


def define_new_CoM_dict(grouped_list, classes_=2):
    CoM_dict = define_empty_dict(classes_)

    for key in grouped_list:
        row = grouped_list[key][0]
        min = sum_of_distances(row, grouped_list[key])
        for i in range(len(grouped_list[key])):
            current_row = grouped_list[key][i]
            current_class_elements = grouped_list[key]
            sum = sum_of_distances(current_row, current_class_elements)
            if sum < min:
                row = current_row
                min = sum
        CoM_dict[key] = row
    return CoM_dict


def group_by_distance(dict_of_CoM, data, classes_):
    data_regrouped = define_empty_dict(classes_)
    change = False
    for key in data_regrouped:
        for i in range(len(data[key])):
            row = data[key][i]
            distance = 0
            decisive_class = next(iter(data))
            for key_2 in dict_of_CoM:
                if key_2 == 0:
                    distance = euclidean_distance(row, dict_of_CoM[key_2])
                elif distance > euclidean_distance(row, dict_of_CoM[key_2]):
                    decisive_class = key_2
                if row[-1] != decisive_class:
                    row[-1] = decisive_class
                    change = True
            data_regrouped[row[-1]].append(row)
    return data_regrouped, change


def k_means(list_, classes_, iterations):
    grouped_data = group_by_class(list_, classes_)
    dict_of_CoM = define_new_CoM_dict(grouped_data)
    final_groups, change = group_by_distance(dict_of_CoM, grouped_data, classes_)

    for i in range(iterations):
        if change:
            new_dict_of_CoM = define_new_CoM_dict(final_groups)
            final_groups, change = group_by_distance(new_dict_of_CoM, final_groups, classes_)
        else:
            break
    return final_groups


list = open_file('australianShorter.dat')
list_random_class = apply_random_class(list)

new_classes = k_means(list_random_class, 2, 200)

for i in new_classes[0]:
    print(i)

print('====================================================')

for i in new_classes[1]:
    print(i)

# for i in new_classes:
#     print(i)


# classes = 2
# centeroids = define_new_centeroids(list, classes)
# print(centeroids)

# list = open_file('australian.dat')
# list_random_class = apply_random_class(list)
# list_after_k_means = k_means(list_random_class, list_random_class, range(1))
# print(list_after_k_means[:4])
