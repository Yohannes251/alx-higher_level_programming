#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, ops[argv[2]](a, b)))
