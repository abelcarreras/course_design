
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
        return atomic_masses[self._symbol.capitalize()]
