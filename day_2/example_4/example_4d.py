import matplotlib.pyplot as plt
from itertools import islice


def fibonacci(n):
    f = [0, 1]

    if n > 0:
        yield f[0]

    if n > 1:
        yield f[1]

    for i in range(n-2):
        yield sum(f)
        f.append(sum(f))
        del f[0]


f_sequence = [term for term in fibonacci(3)]
print(f_sequence)

golden_ratio = [(term1 / term2) for term1, term2 in zip(fibonacci(9), islice(fibonacci(9), 1, None))]
print(golden_ratio)

plt.plot(golden_ratio, '-o', color='red')
plt.show()