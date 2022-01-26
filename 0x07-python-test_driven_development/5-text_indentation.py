#!/usr/bin/python3
"""
5-text_identation module
contains text_identations function
it's provided a text to print
"""


def text_indentation(text):
    """
    text_identation void function. prints text and 2 new lines after . ? :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    txt = text.strip()
    count = 0
    for i in range(0, len(txt)):
        if txt[i] == ':' or txt[i] == '.' or txt[i] == '?':
            count += 1
    rows = [""] * (count + 1)
    row = 0
    for i in range(0, len(txt)):
        if txt[i]:
            rows[row] += txt[i]
            if(txt[i] == ':' or txt[i] == '.' or txt[i] == '?'):
                row += 1
    for i in range(0, len(rows)):
        rows[i] = rows[i].strip()
        if rows[i] != "":
            if i > (len(rows) - 1) or rows[i][len(rows[i]) - 1] == ':' or \
               rows[i][len(rows[i]) - 1] == '.' or \
               rows[i][len(rows[i]) - 1] == '?':
                print("{:s}".format(rows[i]), end="\n\n")
            else:
                print("{}".format(rows[i]), end="")
