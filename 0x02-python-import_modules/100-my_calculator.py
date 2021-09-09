#!/usr/bin/python3
import sys
import calculator_1


def main():
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            result = add(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "*" or operator[0] == "*":
            result = mul(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
        elif operator == "/":
            result = div(a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
