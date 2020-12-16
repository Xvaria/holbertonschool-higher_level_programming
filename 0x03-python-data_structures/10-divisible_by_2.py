#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = my_list[:]
    j = 0
    for i in my_list:
        if i % 2 == 0:
            a[j] = True
        else:
            a[j] = False
        j = j + 1
    return a
