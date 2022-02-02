#!/usr/bin/python3
"""
12-pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    ret = []
    auxPrev = []
    for i in range(0, n):
        if i == 0:
            ret.append(1)
            continue
        aux = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                aux.append(1)
                continue
            aux.append(auxPrev[j] + auxPrev[1 - j])
        ret.append(aux)
        auxPrev = aux
    return ret
