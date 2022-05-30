import numpy as np
from plots import plot_function, plot_function_2


plot_function('plot_title', [0, 1, 2, 3, 4, 5, 6], np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                                                             [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                                                             [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]])).show()

my_data = ['plot_title',
           [0, 1, 2, 3, 4, 5, 6],
           np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                     [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                     [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]])]

plot_function_2(my_data).show()


plot_function(*my_data).show()