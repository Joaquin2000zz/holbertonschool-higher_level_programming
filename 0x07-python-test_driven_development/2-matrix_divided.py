#!/usr/bin/python3
"""
2-matrix_divided module
contains matrix_divided function
parameters: matrix, div
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - returns a new matrix with the calculations
    """
    refLen = 0
    lenCurrent = 0
    valueAppend = 0
    hola = 0

    if type(div) is not int:
        if type(div) is not float or div is None:
            raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    refLen = len(matrix[0])
    ret = [ele[:] for ele in matrix]
    for row in range(0, len(matrix)):
        lenCurrent = len(matrix[row])

        if refLen != lenCurrent:
            raise TypeError("Each row of the matrix must have the same size")
        for value in range(0, len(matrix[row])):
            if type(matrix[row][value]) is not int:
                if type(matrix[row][value]) is not float:
                    raise TypeError("matrix must be a matrix (list of lists\
                                    ) of integers/floats")

            valueAppend = matrix[row][value] / div
            if type(valueAppend) is float:
                valueAppend = round(valueAppend, 2)
            ret[row][value] = valueAppend
    return ret
