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


# generator approach
def weird_function(n):
    for i in range(10):
        sum1 = 0
        for j in range(5):
            sum1 += i ** 2 + j

        sum2 = np.sqrt(i)
        yield sum1, sum2


sum_tot = sum([term1 + term2 for term1, term2 in weird_function(10)])
print('Total :', sum_tot)

sum_tot = sum([term1 * term2 for term1, term2 in weird_function(10)])
print('Total (2):', sum_tot)

sum_tot = sum([term1 + term2 for term1, term2 in weird_function(10) if term1 < 50])
print('Total (3):', sum_tot)
