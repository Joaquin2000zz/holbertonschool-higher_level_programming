#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ret = (0, 0)
    if tuple_a and tuple_a[0] != 0:
        ret = (tuple_a[0], 0)
        if tuple_b and tuple_b[0] != 0:
            ret = (tuple_a[0] + tuple_b[0], 0)
    else:
        ret = (tuple_b[0], 0)
    if len(tuple_a) == 2:
        ret = (ret[0], tuple_a[1])
        if len(tuple_b) == 2:
            ret = (ret[0], tuple_a[1] + tuple_b[1])
    else:
        ret = (ret[0], tuple_b[1])
    return ret
