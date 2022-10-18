#!/usr/bin/python3

def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    new_matrix = [[matrix[i][j] / div for j in range(len(matrix[0]))] for i in
                  range(len(matrix))]
    for i in matrix:
        if not(isinstance(i, (list))):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not(isinstance(div, (int, float))) or div != div:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = float("{0:.2f}" .format(new_matrix[i][j]))
    return new_matrix
