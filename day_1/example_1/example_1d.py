# use of external modules for better notation
import numpy as np


charges = [1.0, 8.0, 1.0]
positions = [[0.0, 0.0, 0.0],
             [1.0, 1.0, 1.0],
             [1.0, 1.0, 0.0]]

positions = np.array(positions)

total_potential = 0
for i in range(len(positions)):
    if i+1 < len(positions):
        total_potential = total_potential + charges[i] * charges[i + 1] / np.linalg.norm(positions[i] - positions[i + 1])
    else:
        total_potential = total_potential + charges[i] * charges[0] / np.linalg.norm(positions[i] - positions[0])

print('total_potential: ', total_potential)
