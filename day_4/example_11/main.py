__version__ = 1.2


class CoreProgram:
    def __init__(self, symbols, coordinates):
        self._symbols = symbols
        self._coordinates = coordinates

    def print_molecule_info(self, title, spaces=1):

        print(title)
        print('\n' * (spaces-1))
        for s, c in zip(self._symbols, self._coordinates):
            print('{}    {} {} {}'.format(s, c[0], c[1], c[2]))
