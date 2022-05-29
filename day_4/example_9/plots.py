import matplotlib.pyplot as plt


def plot_function(title, x_data, y_data_array):
    plt.title(title)

    for y_data in y_data_array:
        plt.plot(x_data, y_data)

    return plt


def plot_function_2(my_data):
    title = my_data[0]
    x_data = my_data[1]
    y_data_array = my_data[2]
    plt.title(title)

    for y_data in y_data_array:
        plt.plot(x_data, y_data)

    return plt


def plot_function_3(my_data):
    title = my_data['title']
    x_data = my_data['x_data']
    y_data_array = my_data['y_data_array']

    plt.title(title)

    for y_data in y_data_array:
        plt.plot(x_data, y_data)

    return plt


def plot_function_4(title='', x_data=(), y_data_array=(())):

    plt.title(title)
    for y_data in y_data_array:
        plt.plot(x_data, y_data)

    return plt


def plot_function_5(plot_data):

    plt.title(plot_data.title)
    for y_data in plot_data.y_data_array:
        plt.plot(plot_data.x_data, y_data)

    return plt
