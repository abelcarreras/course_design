from atom import Atom
import numpy as np


class Molecule:
    def __init__(self, atoms_list):
        self._atoms_list = atoms_list

    def get_number_of_atoms(self):
        return len(self._atoms_list)

    def get_mass(self):
        return sum([atom.get_mass() for atom in self._atoms_list])

    def _coordinates_matrix(self):
        return np.array([atom.get_coordinates() for atom in self._atoms_list])

    def get_center_of_mass(self):
        # make sure that they are numpy array
        coordinates = self._coordinates_matrix()
        masses = np.array([atom.get_mass() for atom in self._atoms_list])

        center_of_mass = np.average(coordinates, axis=0, weights=masses)

        return center_of_mass
