#!/usr/bin/python3


from sys import stderr


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as er:
        stderr.write("Exception: {}\n".format(er))
        ret = None
    return ret
