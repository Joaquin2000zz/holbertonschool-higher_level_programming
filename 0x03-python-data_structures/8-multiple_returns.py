#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        ret = 0, None
        return ret
    ret = len(sentence), sentence[0]
    return ret
