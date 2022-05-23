import numpy as np


class SpinOperator:
    def __init__(self, vector):
        """
        Build spin operator

        :param vector:  3D unit vector indicating the xyz direction of spin
        """

        s_x = np.array([[0, 1],
                        [1, 0]])

        s_y = np.array([[ 0, 1.j],
                        [-1.j, 0]])

        s_z = np.array([[-1, 0],
                        [ 0, 1]])

        self._s = [s_x, s_y, s_z]
        self._vector = vector

    def get_matrix_representation(self):
        s_matrix = sum([a*si for a, si in zip(self._vector, self._s)])
        return s_matrix

    def __str__(self):
        txt = 'Spin Operator\n'
        txt += 'Real: \n'
        txt += self.get_matrix_representation().real.__str__()
        txt += '\nImaginary: \n'
        txt += self.get_matrix_representation().imag.__str__()
        return txt

    def __add__(self, other):
        if isinstance(other, SpinOperator):
            sum_vector = np.add(other._vector, self._vector)
            return SpinOperator(sum_vector)
        raise Exception('Addition between these objects is not implemented')


operator_1 = SpinOperator([0, 1, 0])
operator_2 = SpinOperator([1, 0, 0])

print('Matrix representation')
print(operator_1.get_matrix_representation())
print(operator_2.get_matrix_representation())

print('Addition')
operator_3 = operator_1 + operator_2
print(operator_3)

