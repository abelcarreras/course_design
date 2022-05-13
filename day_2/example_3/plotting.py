import matplotlib.pyplot as plt

title_name = 'plot vector'


def plot_bar_vector(vector):
    labels = ['state {}'.format(i+1) for i in range(len(vector))]
    plt.title('Bar ' + title_name)
    plt.bar(labels, vector)
    return plt


def plot_simple_vector(vector):
    plt.title('Simple ' + title_name)
    plt.plot(vector, 'o-', color='red')
    return plt

