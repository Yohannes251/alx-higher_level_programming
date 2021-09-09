#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    names.sort()
    for c in names:
        if c[:2] != "__":
            print("{}".format(c))

if __name__ == "__main__":
    main()
