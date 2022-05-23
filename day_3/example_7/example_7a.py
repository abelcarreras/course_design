

class Simulation:
    def __init__(self, potential):
        self._potential = potential

    def set_positions(self, positions):
        self._positions = positions

    def set_velocites(self, velocities):
        self._velocites = velocities

    def set_masses(self, masses):
        self._masses = masses

    def calculate(self):
        kinetic = sum([0.5 * m * v**2 for m, v in zip(self._masses, self._velocites)])
        potential = sum([self._potential(p) for p in self._positions])
        self._calculation = kinetic + potential

    def get_results(self):
        return self._calculation


# my data
positions = [1, 2, 3]
velocities = [0, 1, -1]
masses = [1, 1, 1]


def potential(x):
    return x ** 2


simulation_1 = Simulation(potential)

simulation_1.set_positions(positions)
simulation_1.set_velocites(velocities)
simulation_1.set_masses(masses)

simulation_1.calculate()

result = simulation_1.get_results()

print(result)



