from linear_algebra_a import trace
from plotting_a import plot_bar_vector, plot_simple_vector
import numpy as np

# dimensions
dimension = 3
title_name = 'plot vector'

print('dimension', dimension)
print('tile name', title_name)

# build Hamiltonian
hamiltonian = np.zeros((3, 3))

# self energies
energies = [1.0, 1.2, 1.1]
hamiltonian[0, 0] = energies[0]
hamiltonian[1, 1] = energies[1]
hamiltonian[2, 2] = energies[2]

# coupling 1
coupling_01 = 0.1
hamiltonian[0, 1] = coupling_01
hamiltonian[1, 0] = coupling_01

# coupling 2
coupling_12 = 0.2
hamiltonian[1, 2] = coupling_12
hamiltonian[2, 1] = coupling_12


print('\nHamiltonian')
print(hamiltonian)
print('\nTrace: ', trace(hamiltonian, dimension))

eigen_energies = np.linalg.eigvals(hamiltonian)
print('Eigenvalues: ', eigen_energies)

# plot data
plot_bar_vector(energies, title_name)
plot_simple_vector(energies, title_name)

plot_bar_vector(eigen_energies, title_name)
plot_simple_vector(eigen_energies, title_name)
