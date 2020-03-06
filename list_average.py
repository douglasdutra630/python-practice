num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 187]

def mean_finder():
    list_sum = 0
    for y in num_list:
        for x in num_list:
            x = len(num_list)
        list_sum += y
        mean = list_sum / x
    print(mean)

mean_finder()

from functools import reduce

def mean_reducer (num_list):
    total = (reduce(
            lambda total, element: total + element), 
            num_list)

    return total / len(num_list)

print(mean_reducer(num_list))

