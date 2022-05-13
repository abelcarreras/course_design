import numpy as np


def get_principal_axis_and_moments_of_inertia_1(cm_coordinates, masses):
    """
    Compute the principal axis and moments of inertia
    (very explicit)

    :param cm_coordinates: list of atomic coordinates
    :param masses: list of atomic masses
    :return: moments of inertia, principal axis of inertia in rows
    """

    # Build inertia tensor
    inertia_tensor = np.zeros((3, 3))
    for m, c in zip(masses, cm_coordinates):
        inertia_tensor[0, 0] += m * (c[1]**2 + c[2]**2)
        inertia_tensor[1, 1] += m * (c[0]**2 + c[2]**2)
        inertia_tensor[2, 2] += m * (c[0]**2 + c[1]**2)

        inertia_tensor[0, 1] += -m * (c[0] * c[1])
        inertia_tensor[0, 2] += -m * (c[0] * c[2])
        inertia_tensor[1, 2] += -m * (c[1] * c[2])

    inertia_tensor[1, 0] = inertia_tensor[0, 1]
    inertia_tensor[2, 0] = inertia_tensor[0, 2]
    inertia_tensor[2, 1] = inertia_tensor[1, 2]

    # Compute eigenvalues and eigenvectors of inertia tensor
    e_values, e_vectors = np.linalg.eigh(inertia_tensor)  # be careful eigenvectors in columns!
    axis_of_inertia = e_vectors.T
    moments_of_inertia = e_values

    return moments_of_inertia, axis_of_inertia


def get_principal_axis_and_moments_of_inertia_2(cm_coordinates, masses):
    """
    Compute the principal axis and moments of inertia
    (closer to equation)

    :param cm_coordinates: list of atomic coordinates
    :param masses: list of atomic masses
    :return: moments of inertia, principal axis of inertia in rows
    """

    def delta(i, j):
        return 1 if i == j else 0

    # Build inertia tensor
    inertia_tensor = np.zeros((3, 3))
    for m, c in zip(masses, cm_coordinates):
        for i in range(3):
            for j in range(3):
                inertia_tensor[i, j] += m * (delta(i, j) * np.dot(c, c) - c[i]*c[j])


    # Compute eigenvalues and eigenvectors of inertia tensor
    e_values, e_vectors = np.linalg.eigh(inertia_tensor)  # be careful eigenvectors in columns!
    axis_of_inertia = e_vectors.T
    moments_of_inertia = e_values

    return moments_of_inertia, axis_of_inertia


def get_principal_axis_and_moments_of_inertia_3(cm_coordinates, masses):
    """
    Compute the principal axis and moments of inertia
    (compact and vectorized)

    :param cm_coordinates: list of atomic coordinates
    :param masses: list of atomic masses
    :return: moments of inertia, principal axis of inertia in rows
    """

    # Build inertia tensor
    inertia_tensor = np.zeros((3, 3))
    for m, c in zip(masses, cm_coordinates):
        inertia_tensor += m * (np.identity(3) * np.dot(c, c) - np.outer(c, c))

    # Compute eigenvalues and eigenvectors of inertia tensor
    e_values, e_vectors = np.linalg.eigh(inertia_tensor)  # be careful eigenvectors in columns!
    axis_of_inertia = e_vectors.T
    moments_of_inertia = e_values

    return moments_of_inertia, axis_of_inertia

