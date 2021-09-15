#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict_list = sorted(a_dictionary.items())
    for item in sorted_dict_list:
        print("{}: {}".format(item[0], item[1]))
