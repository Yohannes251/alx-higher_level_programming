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
        op = sys.argv[2]
        if op == "+":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, add(a, b)))
        elif op == "-":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, sub(a, b)))
        elif op == "*" or op[0] == "*":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, mul(a, b)))
        elif op == "/":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, div(a, b)))


if __name__ == "__main__":
    main()
