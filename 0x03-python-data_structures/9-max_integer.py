#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    ret = -99999999
    for i in my_list:
        if i > ret:
            ret = i
    return ret
