import numpy as np


def get_masses_from_elements(elements):
    """
    returns a list of atomic masses from a list of atomic elements

    :param elements: list of atomic elements
    :return: list of atomic masses
    """

    masses_dict = {'C': 12.0,
                   'H': 1.0,
                   'O': 16.0}

    masses = [masses_dict[e.capitalize()] for e in elements]  # list comprehension
    return masses


def get_center_of_mass(coordinates, masses):
    """
    returns center of mass

    :param coordinates: list of coordinates
    :param masses: list of masses
    :return: center of mass vector
    """

    # make sure that they are numpy array
    coordinates = np.array(coordinates)
    masses = np.array(masses)

    center_of_mass = np.average(coordinates, axis=0, weights=masses)

    return center_of_mass


def rotate_coordinates(coordinates, angle, axis, atoms_list=None, center=(0, 0, 0)):
    """
    Rotate the coordinates (or range of coordinates) with respect a given axis

    :param coordinates: coordinates to rotate
    :param angle: rotation angle
    :param axis: rotation axis
    :param atoms_list: list of atoms to rotate (if None then rotate all)
    :return: rotated coordinates
    """
    axis = np.array(axis) / np.linalg.norm(axis)
    coordinates = np.array(coordinates) - np.array(center)

    cos_term = 1 - np.cos(angle)
    rot_matrix = [[axis[0]**2*cos_term + np.cos(angle),              axis[0]*axis[1]*cos_term - axis[2]*np.sin(angle), axis[0]*axis[2]*cos_term + axis[1]*np.sin(angle)],
                  [axis[1]*axis[0]*cos_term + axis[2]*np.sin(angle), axis[1]**2*cos_term + np.cos(angle),              axis[1]*axis[2]*cos_term - axis[0]*np.sin(angle)],
                  [axis[2]*axis[0]*cos_term - axis[1]*np.sin(angle), axis[1]*axis[2]*cos_term + axis[0]*np.sin(angle), axis[2]**2*cos_term + np.cos(angle)]]

    if atoms_list is not None:
        coordinates[atoms_list] = np.dot(coordinates[atoms_list], rot_matrix)
    else:
        coordinates = np.dot(coordinates, rot_matrix) + np.array(center)

    return coordinates.tolist()

