#!/usr/bin/python3


from sys import stderr


def safe_function(fct, *args):
    try:
        ret = fct(args[0], args[1])
    except Exception as er:
        stderr.write("Exception: {}\n".format(er))
        ret = None
    return ret
