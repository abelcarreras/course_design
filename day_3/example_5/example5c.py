

atomic_masses = {'H': 1.0,
                 'C': 12.0,
                 'O': 16.0}


class Atom:
    def __init__(self, symbol, coordinates):
        self._symbol = symbol  # basic treat
        self._coordinates = coordinates  # object property

    def set_coordinates(self, coordinates):
        self._coordinates = coordinates

    def get_coordinates(self):
        return self._coordinates

    def get_mass(self):
        return atomic_masses[self._symbol]


class Molecule:
    def __init__(self, atoms_list):
        self._atoms_list = atoms_list

    def get_number_of_atoms(self):
        return len(self._atoms_list)

    def get_mass(self):
        return sum([atom.get_mass() for atom in self._atoms_list])


# Instance of an object
hydrogen = Atom('H', [0, 0, 0])
oxygen = Atom('O', [1, 0, 0])
hydrogen_2 = Atom('H', [1, 1, 0])


# create molecule
water_molecule = Molecule([hydrogen, oxygen, hydrogen_2])


# molecule properties
print('Number of atoms', water_molecule.get_number_of_atoms())
print('Molecular mass', water_molecule.get_mass())
