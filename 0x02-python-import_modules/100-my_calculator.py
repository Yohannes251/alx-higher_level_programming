#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        elif operator == "*" or operator[0] == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    main()
