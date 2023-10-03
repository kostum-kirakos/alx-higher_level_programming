#!/usr/bin/python3
"""matrix_devided function"""


def matrix_divided(matrix, div):
    """

    -------------------------------------TESTING TYPE------------------------------------------
    -------------------------------------------------------------------------------------------

    >>> matrix = [[1, "hi", 3], [4, "name", 6, 7]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[1, 4, 3, 2], "777"]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats


    ------------------------------------TESTING INT ~ FLOAT------------------------------------
    -------------------------------------------------------------------------------------------

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 6)
    [[0.17, 0.33, 0.5], [0.67, 0.83, 1.0]]

    >>> matrix = [[1, 2.1, 3], [4.11, 5, 6]]
    >>> matrix_divided(matrix, 11)
    [[0.09, 0.19, 0.27], [0.37, 0.45, 0.55]]

    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    >>> matrix_divided(matrix, "test")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

    -------------------------------------TESTING OTHER ERRORS----------------------------------
    -------------------------------------------------------------------------------------------

    >>> matrix = [[4, 5, 3], [7, 7, 6, 5]]
    >>> matrix_divided(matrix, 1)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[1, 2, 3, 4, 5, 4], [4, 6, 6, 4]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[], [1, 3]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

    ----------------------------------------EXTRA TESTING-------------------------------------
    ------------------------------------------------------------------------------------------
    >>> matrix = [[]]
    >>> matrix_divided([[3]], 3)
    [[1.0]]

    >>> print(matrix_divided(matrix, 2))
    [[]]

    >>> matrix_divided([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0], [2.33, 2.67, 3.0]]

    >>> matrix_divided([[14, 7], [21, -49], [21, 65]], float('inf'))
    [[0.0, 0.0], [0.0, -0.0], [0.0, 0.0]]
    """
    if not isinstance(matrix, list):
        raise ValueError("Input matrix must be a list")

    for i in range(len(matrix)):
        if not isinstance(i, list):
            raise ValueError("matrix must be a matrix (list of lists) "
                             "of integers/floats")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        new_list = []
        for j in range(len(matrix[i])):
            division = round(matrix[i][j] / div, 2)
            new_list.append(division)
        new_matrix.append(new_list)
    return new_matrix

