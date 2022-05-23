from atom import Atom
from molecule import Molecule
import numpy as np


def get_molecule_from_file(file_name):
    with open(file_name) as f:
        data = f.read().split('\n')

    n_atoms = int(data[0])

    atoms_list = []
    for line in data[2:2+n_atoms]:
        s, c1, c2, c3 = line.split()
        atom = Atom(symbol=s, coordinates=np.array([c1, c2, c3], dtype=float))
        atoms_list.append(atom)

    return Molecule(atoms_list)
