import numpy as np


def read_xyz_file(file_name):
    with open(file_name) as f:
        data = f.read().split('\n')

    n_atoms = int(data[0])

    coordinates = []
    symbols = []
    for line in data[2:2+n_atoms]:
        s, c1, c2, c3 = line.split()
        coordinates.append([c1, c2, c3])
        symbols.append(s)

    coordinates = np.array(coordinates, dtype=float)
    return symbols, coordinates
