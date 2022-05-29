import numpy as np
from plots import plot_function_5


class PlotData:
    def __init__(self, title, x_data, y_data_array):
        self.title = title
        self.x_data = x_data
        self.y_data_array = y_data_array


my_data = PlotData(title='plot_title',
                   x_data=[0, 1, 2, 3, 4, 5, 6],
                   y_data_array=np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                                          [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                                          [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]]))

plot_function_5(my_data).show()

