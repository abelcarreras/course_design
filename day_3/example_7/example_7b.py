
class Particle:
    def __init__(self, position, velocity, mass):
        self._position = position
        self._velocity = velocity
        self._mass = mass

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def get_mass(self):
        return self._mass


def compute_energy(particle1, particle2, particle3):

    def potential(x):
        return x ** 2

    particle_list = [particle1, particle2, particle3]

    velocities = [p.get_velocity() for p in particle_list]
    positions = [p.get_position() for p in particle_list]
    masses = [p.get_mass() for p in particle_list]

    kinetic = sum([0.5 * m * v ** 2 for m, v in zip(masses, velocities)])
    potential = sum([potential(p) for p in positions])
    return kinetic + potential


# my data
positions = [1, 2, 3]
velocities = [0, 1, -1]
masses = [1, 1, 1]

particle1 = Particle(position=1, velocity=0, mass=1)
particle2 = Particle(position=2, velocity=1, mass=1)
particle3 = Particle(position=3, velocity=-1, mass=1)

result = compute_energy(particle1, particle2, particle3)
print(result)


