#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    for tup in my_list:
        numerator += (tup[0] * tup[1])
    for tup in my_list:
        denominator += tup[1]
    return numerator / denominator
