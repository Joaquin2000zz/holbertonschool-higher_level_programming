#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = {}
    for i, v in a_dictionary.items():
        ret[i] = v * 2
    return ret
