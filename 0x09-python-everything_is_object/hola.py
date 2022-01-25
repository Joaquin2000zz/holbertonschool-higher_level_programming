#!/usr/bin/python3

def increment(n):
    n += 1
    return n
b = 1
print("id b: {} id b: {}".format(b, id(b)))
increment(b)
#print(a is b)
print("id b: {} id b: {}".format(b, id(b)))
