from linear_algebra_b import outer_product, trace, rotate_vector_list
from plotting import plot_bar_vector, plot_simple_vector
import numpy as np


# A more general way to build hamiltonian

# Vector representation of States
v_states = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]

# v_states = rotate_vector_list(v_states, 0.1, axis=[2, 3, 4])

# build Hamiltonian
hamiltonian = np.zeros_like(v_states, dtype=float)

# self energies
energies = [1.0, 1.2, 1.1]
for energy, v_state in zip(energies, v_states):
    hamiltonian += energy * outer_product(v_state, v_state)

# coupling 1
coupling_01 = 0.1
hamiltonian += coupling_01 * outer_product(v_states[0], v_states[1])

# coupling 2
coupling_12 = 0.2
hamiltonian += coupling_12 * outer_product(v_states[1], v_states[2])

# make hamiltonian symmetric
hamiltonian = 0.5 * (hamiltonian + hamiltonian.T)

print('\nHamiltonian')
print(hamiltonian)
print('\nTrace: ', trace(hamiltonian))

eigen_energies = np.linalg.eigvals(hamiltonian)
print('Eigenvalues: ', eigen_energies)

# plot data
plot_bar_vector(energies)
plot_simple_vector(energies).figure()

plot_bar_vector(eigen_energies)
plot_simple_vector(eigen_energies).show()
