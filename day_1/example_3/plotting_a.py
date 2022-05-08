import matplotlib.pyplot as plt


def plot_bar_vector(vector, title_name):
    labels = ['state {}'.format(i+1) for i in range(len(vector))]
    plt.title('Bar ' + title_name)
    plt.bar(labels, vector)
    plt.show()


def plot_simple_vector(vector, title_name):
    plt.title('Simple ' + title_name)
    plt.plot(vector, 'o-', color='red')
    plt.show()

