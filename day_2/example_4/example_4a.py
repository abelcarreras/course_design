import numpy as np


# naive approach
sum1 = 0
for i in range(10):
    sum1 = sum1 + i ** 2

sum2 = 0
for i in range(10):
    sum2 = sum2 + np.sqrt(i)

print('Total :', sum1 + sum2)


# compact approach
sum_tot = 0
for i in range(10):
    sum_tot += i ** 2 + np.sqrt(i)

print('Total :', sum_tot)


# list comprehension
sum_tot = sum([i ** 2 + np.sqrt(i) for i in range(10)])
print('Total :', sum_tot)

