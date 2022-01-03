#!/usr/bin/pytho3
def no_c(my_string):
    if my_string:
        ret = ''
        for i in my_string:
            if i != 'C' and i != 'c':
                ret = ret + i
    return ret
