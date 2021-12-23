#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
if len(argv) == 1:
    print(0)
else:
    if len(argv) == 2:
        print("{0:d}".format(int(argv[1])))
    else:
        res = 0
        for i in range(1, len(argv)):
            res = res + int(argv[i])
        print("{:d}".format(res))
