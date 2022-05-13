import numpy as np
dimension = 3


def dot_product(vector_1, vector_2):
    my_sum = 0

    # dimension = 4

    for i in range(dimension):
        my_sum += vector_1[i] * vector_2[i]

    return my_sum


def modulus(vector_1):
    my_sum = 0

    # dimension = 4

    for i in range(dimension):
        my_sum += vector_1[i]**2

    return np.sqrt(my_sum)


def outer_product(vector_1, vector_2):

    # dimension = 4

    matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            row.append(vector_1[i]*vector_2[j])
        matrix.append(row)

    return np.array(matrix)


def trace(matrix):
    sum = 0
    for i in range(dimension):
        sum += matrix[i][i]

    return sum


def rotate_vector_list(vector_list, angle, axis):
    """
    Rotate a list of vectors with respect a given axis

    :param vector_list: list of vectors to rotate
    :param angle: rotation angle
    :param axis: rotation axis
    :param atoms_list: list of atoms to rotate (if None then rotate all)
    :return: rotated coordinates
    """

    axis = np.array(axis) / np.linalg.norm(axis)
    vector_list = np.array(vector_list)

    cos_term = 1 - np.cos(angle)
    rot_matrix = [[axis[0]**2*cos_term + np.cos(angle),              axis[0]*axis[1]*cos_term - axis[2]*np.sin(angle), axis[0]*axis[2]*cos_term + axis[1]*np.sin(angle)],
                  [axis[1]*axis[0]*cos_term + axis[2]*np.sin(angle), axis[1]**2*cos_term + np.cos(angle),              axis[1]*axis[2]*cos_term - axis[0]*np.sin(angle)],
                  [axis[2]*axis[0]*cos_term - axis[1]*np.sin(angle), axis[1]*axis[2]*cos_term + axis[0]*np.sin(angle), axis[2]**2*cos_term + np.cos(angle)]]

    vector_list = np.dot(vector_list, rot_matrix)

    return vector_list.tolist()
