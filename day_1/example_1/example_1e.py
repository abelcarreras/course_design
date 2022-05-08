# use of general algorithm
import numpy as np


charges = [1.0, 8.0, 1.0]
positions = np.array([[0.0, 0.0, 0.0],
                      [1.0, 1.0, 1.0],
                      [1.0, 1.0, 0.0]])

total_potential = 0
for q1, p1 in zip(charges, positions):
    for q2, p2 in zip(charges, positions):
        if np.linalg.norm(p1 - p2) != 0:
            total_potential += 0.5 * q1 * q2 / np.linalg.norm(p1 - p2)

print('total_potential: ', total_potential)
