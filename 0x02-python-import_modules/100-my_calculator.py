#!/usr/bin/python3
from sys import argv
import calculator_1


def main():
    argc = len(argv)
    if argc != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == "+":
        result = calculator_1.add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == "-":
        result = calculator_1.sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == "*" or operator[0] == "*":
        result = calculator_1.mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == "/":
        result = calculator_1.div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))


if __name__ == '__main__':
    main(argv)
