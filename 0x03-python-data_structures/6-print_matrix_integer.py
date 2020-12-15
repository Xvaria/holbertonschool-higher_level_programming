#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if a < len(matrix[i]):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
            a = a + 1
        a = 1
        print()
