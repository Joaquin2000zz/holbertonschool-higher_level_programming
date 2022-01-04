#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    j = 0
    for i in val_list:
        if i > j:
            j = i
    print("sali del if al final d iteracion con val list {}".format(j))
    r = key_list[val_list.index(j)]
    return r
