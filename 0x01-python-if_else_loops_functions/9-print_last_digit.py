#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        aux = -number % 10
    else:
        aux = number % 10
    print(aux, end='')
    return(aux)
