#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ret = 0
    weights = 0
    for i in my_list:
        ret += i[0] * i[1]
        weights += i[1]
    return ret/weights
