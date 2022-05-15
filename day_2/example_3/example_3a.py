from linear_algebra_a import dot_product, modulus, outer_product, trace


# dimensions
dimension = 3
title_name = 'plot vector'

vector_1 = [1, 2, 1]
vector_2 = [1, 2, 3]

matrix = [[1, 0, 0],
          [0, 2, 0],
          [0, 0, 3]]

print('dimension', dimension)
print('tile name', title_name)

dot = dot_product(vector_1, vector_2, dimension)

print('dot', dot)

mod = modulus(vector_1, dimension)

print('modulus', mod)

out = outer_product(vector_1, vector_2, dimension)
print('outer_product\n', out)

t = trace(matrix, dimension)
print('trace', t)

