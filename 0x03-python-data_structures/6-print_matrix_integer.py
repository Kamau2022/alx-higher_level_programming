#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function to print a formatted matrix"""
    result = ('\n'.join([' '.join(['{:d}'.format(item) for item in row])
              for row in matrix]))
    print(result)
