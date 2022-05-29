import numpy as np
from plots import plot_function_2, plot_function_3, plot_function_4


my_data = {'title': 'plot_title',
           'x_data': [0, 1, 2, 3, 4, 5, 6],
           'y_data_array': np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                                     [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                                     [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]])}



plot_function_3(my_data).show()

plot_function_4(**my_data).show()


my_data_2 = {0: 'plot_title',
             1: [0, 1, 2, 3, 4, 5, 6],
             2: np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                          [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                          [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]])}


plot_function_2(my_data_2).show()
