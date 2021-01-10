#!/usr/bin/python3
'divide matrix'


def matrix_divided(matrix, div):
    '''Function to divide matrix of list integers or floats

    Args:
        matrix: list of int or float
        div: divisor int or float

    Returns:
        new matrix with result to divide for div

    Raises:
        TypeError or ZeroDivisionError
    '''
B
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if type(div) == int or type(div) == float:
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    a = len(matrix[0])
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        if a != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) == int or type(j) == float or type(i) == list:
                continue
            else:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    r = []
    for k in matrix:
        d = []
        for l in k:
            d.append(round(l/div, 2))
        r.append(d)
    return(r)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
