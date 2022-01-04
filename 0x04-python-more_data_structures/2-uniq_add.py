#!/usr/bin/python3
def uniq_add(my_list=[]):
    ret = set(my_list)
    r = 0
    for i in ret:
        r += i
    return r
