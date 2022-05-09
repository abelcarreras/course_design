# better code format
from math import sqrt


charges = [1.0, 8.0, 1.0]
positions = [[0.0, 0.0, 0.0],
             [1.0, 1.0, 1.0],
             [1.0, 1.0, 0.0]]

total_potential = 0
for i in range(len(positions)):
    if i+1 < len(positions):
        total_potential = total_potential + charges[i] * charges[i + 1] / sqrt((positions[i][0] - positions[i + 1][0])**2 +
                                                                               (positions[i][1] - positions[i + 1][1])**2 +
                                                                               (positions[i][2] - positions[i + 1][2])**2)
    else:
        total_potential = total_potential + charges[i] * charges[0] / sqrt((positions[i][0] - positions[0][0])**2 +
                                                                           (positions[i][1] - positions[0][1])**2 +
                                                                           (positions[i][2] - positions[0][2])**2)
print('total_potential: ', total_potential)
