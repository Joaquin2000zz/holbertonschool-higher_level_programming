#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return j
