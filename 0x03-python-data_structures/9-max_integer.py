#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_number = sorted(my_list)
    return (max_number[-1])
