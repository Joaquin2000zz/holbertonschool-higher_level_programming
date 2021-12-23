#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import exit, argv

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    if argv[2] == '+':
        res = add(int(argv[1]), int(argv[3]))
    elif argv[2] == '-':
        res = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == '/':
        res = div(int(argv[1]), int(argv[3]))
    elif argv[2] == '*':
        res = mul(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2], int(argv[3]), res))
