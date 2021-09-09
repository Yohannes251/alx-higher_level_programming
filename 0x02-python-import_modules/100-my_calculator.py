#!/usr/bin/python3
import sys
import calculator_1


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
            print("{} {} {} = {}".format(a, op, b, calculator_1.add(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, calculator_1.sub(a, b)))
        elif op == "*" or op[0] == "*":
            print("{} {} {} = {}".format(a, op, b, calculator_1.mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, calculator_1.div(a, b)))


if __name__ == "__main__":
    main()
