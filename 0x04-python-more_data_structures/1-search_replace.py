#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ret = []
    for i in my_list:
        if i == search:
            ret.append(replace)
        else:
            ret.append(i)
    return ret
