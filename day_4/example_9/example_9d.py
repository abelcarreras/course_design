import numpy as np
from plots import plot_function_5, plot_function_4, plot_function_3, plot_function_2, plot_function


class PlotData:
    def __init__(self, title, x_data, y_data_array):
        self.title = title
        self.x_data = x_data
        self.y_data_array = y_data_array

    def __len__(self):
        return 3

    def __getitem__(self, item):
        if item == 'title' or item == 0:
            return self.title
        elif item == 'x_data' or item == 1:
            return tuple(self.x_data)
        elif item == 'y_data_array' or item == 2:
            return self.y_data_array

    def __iter__(self):
        items_dict = {'title': self.title, 'x_data': self.x_data, 'y_data_array': self.y_data_array}
        return (items_dict[item] for item in items_dict)


my_data = PlotData(title='plot_title',
                   x_data=[0, 1, 2, 3, 4, 5, 6],
                   y_data_array=np.array([[3.1, 3.5, 4.3, 5.1, 5.0, 4.9, 3.7],
                                          [2.5, 2.6, 2.8, 2.7, 2.9, 3.0, 3.2],
                                          [1.1, 1.5, 1.2, 1.5, 1.3, 1.6, 1.5]]))

print(my_data[0])
print(my_data['x_data'])
print(len(my_data))

print('--------')

plot_function_5(my_data).show()
plot_function_4(*my_data).show()
plot_function_3(my_data).show()
plot_function_2(my_data).show()
plot_function(*my_data).show()


