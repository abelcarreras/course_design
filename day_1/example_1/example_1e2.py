# use of general algorithm (alternative)
import numpy as np


charges = [1.0, 8.0, 1.0]
positions = np.array([[0.0, 0.0, 0.0],
                      [1.0, 1.0, 1.0],
                      [1.0, 1.0, 0.0]])

total_potential = 0
for i, q1 in enumerate(charges):
    for j, q2 in enumerate(charges):
        total_potential += 0.5 * q1 * q2 / np.linalg.norm(positions[i] - positions[j]) if (i != j) else 0

print('total_potential: ', total_potential)
