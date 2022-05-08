import numpy as np
from tools import get_masses_from_elements, get_center_of_mass
from file_io import get_data_from_file_1 as get_data_from_file
from inertia import get_principal_axis_and_moments_of_inertia_1 as get_principal_axis_and_moments_of_inertia

# read data from output file
elements, coordinates = get_data_from_file('output.out')
masses = get_masses_from_elements(elements)

# set coordinates respect to the center of mass
center_of_mass = get_center_of_mass(coordinates, masses)
cm_coordinates = coordinates - center_of_mass

# get the principal axis and moments of inertia
moments, principal_axis = get_principal_axis_and_moments_of_inertia(cm_coordinates, masses)

# print results
print('Eigenvalues: ', moments)
print('Eigenvectors')
for i, axis in enumerate(principal_axis):
    print(i+1, axis)

# check orthogonality
print('Check principal axis of inertia')
print(np.dot(principal_axis.T, principal_axis))
