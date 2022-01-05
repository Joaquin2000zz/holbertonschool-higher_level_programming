#!/usr/bin/python3
def roman_to_int(roman_string):
    i = 0
    prev = 0
    num = {'M': 1000,
           'D': 500,
           'C': 100,
           'L': 50,
           'X': 10,
           'V': 5,
           'I': 1}
    for c in range(0, len(roman_string)):
        if roman_string[c] not in num:
            return 0
        for n, k in num.items():
            if roman_string[c] == n:
                prev = k
                if c > 0 and num[roman_string[c - 1]] < num[roman_string[c]]:
                    i -= num[roman_string[c]]
                    if i < 0:
                        i *= -1
                else:
                    i += k

    return i
