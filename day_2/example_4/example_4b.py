import numpy as np


# naive approach
sum1 = 0
for i in range(10):
    for j in range(5):
        sum1 = sum1 + i ** 2 + j

sum2 = 0
for i in range(10):
    sum2 = sum2 + np.sqrt(i)

print('Total :', sum1 + sum2)


# compact approach
sum_tot = 0
for i in range(10):
    sum1 = 0
    for j in range(5):
        sum1 = sum1 + i ** 2 + j

    sum_tot += sum1 + np.sqrt(i)

print('Total :', sum_tot)

# list comprehension
sum_tot = sum([sum([i ** 2 + j for j in range(5)]) + np.sqrt(i)  for i in range(10)])
print('Total :', sum_tot)

