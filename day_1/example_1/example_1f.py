# use of a more efficient general algorithm
import numpy as np
from itertools import combinations


charges = [1.0, 8.0, 1.0]
positions = np.array([[0.0, 0.0, 0.0],
                      [1.0, 1.0, 1.0],
                      [1.0, 1.0, 0.0]])

total_potential = 0
for i, j in combinations(range(len(charges)), 2):
    total_potential += charges[i] * charges[j] / np.linalg.norm(positions[i] - positions[j])

print('total_potential: ', total_potential)
