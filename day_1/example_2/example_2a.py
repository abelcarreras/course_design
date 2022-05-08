import numpy as np
from tools import get_masses_from_elements, get_center_of_mass
from file_io import get_data_from_file_1 as get_data_from_file


################################################################
#  EXAMPLE 1
################################################################
center_of_mass = get_center_of_mass(coordinates=[[0, 0, 0],
                                                 [1, 1, 1],
                                                 [2, 2, 2]],
                                    masses=[2, 1, 1])

print('center of mass 1', center_of_mass)



################################################################
#  EXAMPLE 2
################################################################
coordinates_2 = np.array([[0, 0, 0],
                          [1, 1, 1],
                          [2, 2, 2]])  # numpy array

masses_2 = (2, 1, 1)  # tuple

center_of_mass_2 = get_center_of_mass(coordinates_2, masses_2)
print('center of mass 2', center_of_mass_2)



################################################################
#  EXAMPLE 3
################################################################

elements_3, coordinates_3 = get_data_from_file('output.out')
masses_3 = get_masses_from_elements(elements_3)

center_of_mass_3 = get_center_of_mass(coordinates_3, masses_3)
print('center of mass 3', center_of_mass_3)

