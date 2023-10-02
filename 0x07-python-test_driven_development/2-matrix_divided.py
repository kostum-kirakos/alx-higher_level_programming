#!/usr/bin/python3
"""matrix_devided function"""


def matrix_divided(matrix, div):
	"""
    Function that performs devision of a matrix.

    Returns :
        new_matrix the matrix devided by dev

    Raises :
        TypeError in case the elements are not int nor float
        TypeError in case the rows of the matrix are not the same size
        TypeError in case div is not int nor float
        ZeroDivisionError in case the div is equals to zero
    	"""
    new_matrix = []
    	for row in matrix:
    		for element in row:
			if not isinstance(element, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) "
						"of integers/floats")
	if len(row

    	for row in matrix:
        	new_row = []
        	for element in row:
            		new_element = element / div
            		new_row.append(new_element)
        		new_matrix.append(new_row)
    	return new_matrix
