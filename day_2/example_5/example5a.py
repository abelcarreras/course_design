

class Atom:
    def __init__(self, symbol, coordinates):
        self._symbol = symbol  # basic treat
        self._coordinates = coordinates  # object property

    def set_coordinates(self, coordinates):
        self._coordinates = coordinates

    def get_coordinates(self):
        return self._coordinates


# Instance of an object
hydrogen = Atom('H', [0, 0, 0])
oxygen = Atom('O', [1, 0, 0])

hydrogen_2 = Atom('H', [1, 1, 0])


# create molecule
water_molecule = [hydrogen, oxygen, hydrogen_2]


# molecule properties
n_atoms = len(water_molecule)
print('Number of atoms', n_atoms)
