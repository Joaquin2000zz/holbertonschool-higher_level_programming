#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "":
        return (str)
    if n == 0:
        return (str[1:])
    if n > len(str):
        return ("")
    if n < 0:
        return (str[:len(str) - n])
    if n > 0:
        return (str[: - n])
