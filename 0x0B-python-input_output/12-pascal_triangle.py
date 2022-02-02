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
    aux = [1]
    for i in range(0, n):
        if i == 0:
            ret.append(aux)
            continue
        aux = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                aux.append(1)
                continue
            aux.append(int(auxPrev[j]) + int(auxPrev[1 - j]))
        ret.append(aux)
        auxPrev = aux
    return ret
