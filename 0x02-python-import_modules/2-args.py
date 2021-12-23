#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
if len(argv) == 1:
    print("0 arguments")
else:
    if len(argv) == 2:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv)))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
