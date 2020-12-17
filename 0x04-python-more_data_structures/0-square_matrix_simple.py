#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix[:]
    for i in range(len(a)):
        a[i] = matrix[i][:]
        for j in range(len(a[i])):
            a[i][j] = a[i][j] ** 2
    return a
