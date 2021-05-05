#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    [my_list.remove(j) for j in my_list if j == 'c' or j == 'C']
    return("".join(my_list))
