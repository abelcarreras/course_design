import numpy as np


def get_data_from_file_1(filename):
    """
    Naive parser

    :param filename:
    :return:
    """
    with open(filename) as f:
        data = f.readlines()

    elements = []
    coordinates = []

    n_atoms = 6
    atoms_data = data[5:5 + n_atoms]
    for line in atoms_data:
        element = line[11:12]
        coordinate_x = line[13:30]
        coordinate_y = line[35:50]
        coordinate_z = line[52:65]

        elements.append(element)
        coordinates.append([coordinate_x, coordinate_y, coordinate_z])

    coordinates = np.array(coordinates, dtype=float)

    return elements, coordinates


def get_data_from_file_2(filename):
    """
    better parser but still weak

    :param filename:
    :return:
    """
    with open(filename) as f:
        data = f.readlines()

    elements = []
    coordinates = []

    n_atoms = 6
    atoms_data = data[5:5 + n_atoms]
    for atom in atoms_data:
        element = atom.split()[1]
        coordinate = atom.split()[2:5]

        elements.append(element)
        coordinates.append(coordinate)

    coordinates = np.array(coordinates, dtype=float)

    return elements, coordinates


def get_data_from_file_3(filename):
    """
    more robust parser but requires number of atoms

    :param filename:
    :return:
    """
    with open(filename) as f:
        data = f.readlines()

    elements = []
    coordinates = []

    i_line = 0
    for i_line, line in enumerate(data):
        if 'Standard Nuclear Orientation' in line:
            break

    start_atoms = i_line + 3

    n_atoms = 6
    atoms_data = data[start_atoms:start_atoms + n_atoms]
    for atom in atoms_data:
        element = atom.split()[1]
        coordinate = atom.split()[2:5]

        elements.append(element)
        coordinates.append(coordinate)

    coordinates = np.array(coordinates, dtype=float)

    return elements, coordinates


def get_data_from_file_4(filename):
    """
    parser structured in functions and detects number of atoms


    :param filename:
    :return:
    """
    with open(filename) as f:
        data = f.readlines()

    elements = []
    coordinates = []

    def get_line_index_for(text):
        for i_line, line in enumerate(data):
            if text in line:
                return i_line

        raise Exception('Line not found')

    def get_number_of_atoms(data_atom):
        for i_line, line in enumerate(data_atom):
            if '----------' in line:
                return i_line

    start_atoms = get_line_index_for('Standard Nuclear Orientation') + 3
    n_atoms = get_number_of_atoms(data[start_atoms:])

    atoms_data = data[start_atoms:start_atoms + n_atoms]
    for atom in atoms_data:
        element = atom.split()[1]
        coordinate = atom.split()[2:5]

        elements.append(element)
        coordinates.append(coordinate)

    coordinates = np.array(coordinates, dtype=float)

    return elements, coordinates


def get_data_from_file_5(filename):
    """
    Parser that makes better use of build-in functions

    :param filename:
    :return:
    """

    with open(filename) as f:
        data = f.read()

    elements = []
    coordinates = []

    i_line = data.find('Standard Nuclear Orientation')
    i_initial = data[i_line:].find('\n -----')
    i_final = data[i_line+i_initial+1:].find('\n ----')

    atoms_data = data[i_line + i_initial: i_line + i_initial + i_final].split('\n')[2:]

    for atom in atoms_data:
        element = atom.split()[1]
        coordinate = atom.split()[2:5]

        elements.append(element)
        coordinates.append(coordinate)

    coordinates = np.array(coordinates, dtype=float)

    return elements, coordinates


def get_data_from_file_6(filename):
    """
    Memory efficient parser but less readable and robust

    :param filename:
    :return:
    """

    mark_line = False
    mark_block = False
    elements = []
    coordinates = []

    with open(filename) as f:
        for line in f:
            if 'Standard Nuclear Orientation' in line:
                mark_line = True
                continue

            if '--------' in line and mark_line is True and mark_block is False:
                # atoms block start
                mark_block = True
                continue

            if '--------' in line and mark_line is True and mark_block is True:
                # atoms block finish
                break

            if mark_block is True:

                element = line.split()[1]
                coordinate = line.split()[2:5]

                elements.append(element)
                coordinates.append(coordinate)

        coordinates = np.array(coordinates, dtype=float)

        return elements, coordinates

