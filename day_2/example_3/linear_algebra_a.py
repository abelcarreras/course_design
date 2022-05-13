import numpy as np


def dot_product(vector_1, vector_2, dimension):
    my_sum = 0

    # dimension = 4

    for i in range(dimension):
        my_sum += vector_1[i] * vector_2[i]

    return my_sum


def modulus(vector_1, dimension):
    my_sum = 0

    for i in range(dimension):
        my_sum += vector_1[i]**2

    return np.sqrt(my_sum)


def outer_product(vector_1, vector_2, dimension):

    matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(vector_1[i]*vector_2[j])
        matrix.append(row)

    return np.array(matrix)


def trace(matrix, dimension):
    sum = 0
    for i in range(dimension):
        sum += matrix[i][i]

    return sum
