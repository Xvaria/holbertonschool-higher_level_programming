#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list[:]
    if idx >= 0 and idx < len(a):
        a[idx] = element
    return a
