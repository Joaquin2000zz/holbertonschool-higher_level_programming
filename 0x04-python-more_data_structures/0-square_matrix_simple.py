#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    for i in matrix:
        re = map(lambda x: x * x, i)
        ret.append(list(re))
    return ret
