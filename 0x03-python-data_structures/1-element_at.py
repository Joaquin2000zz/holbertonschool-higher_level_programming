#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list[idx] is True and idx > 0:
        return (my_list.pop(idx))
    else:
        return (None)
