"""
Author: @samuel_dubos
Date: January 9, 2024
"""

import numpy as np


class Gate:

    def __init__(self, matrix, name=''):
        self.matrix = np.matrix(matrix)
        self.dimension = self.matrix.shape[0]
        self.name = name

    @property
    def controlled(self):
        matrix = np.kron(B00, I2) + np.kron(B11, self.matrix)
        return Gate(matrix, f'C{self.name}')

    @property
    def is_unitary(self):
        return np.allclose(self.matrix @ self.matrix.H, np.eye(self.dimension))

    def set_name(self, name, inplace=False):
        self.name = name
        if not inplace:
            return self

    def __add__(self, other):
        return self.matrix + other.matrix

    def __sub__(self, other):
        return self.matrix - other.matrix

    def __mul__(self, other):
        if not isinstance(other, Gate):
            if not isinstance(other, np.matrix):
                return other * self.matrix
            return self.matrix @ other
        return np.kron(self.matrix, other.matrix)

    def __repr__(self):
        return self.name


def qft_matrix(dimension=None, n_qubits: int = 1):
    dimension = dimension or 2 ** n_qubits
    roots = [np.exp(2 * k * np.pi * 1j / dimension) for k in range(dimension)]
    fn = np.ones((dimension, dimension), dtype=complex)
    for i in range(1, dimension):
        for j in range(1, dimension):
            fn[i][j] = roots[(i * j) % dimension]
    return np.matrix(np.round(fn / np.sqrt(dimension), 5))


def phase(m):
    theta = 2 * np.pi / 2 ** m
    matrix = np.matrix([[1, 0], [0, np.exp(1j * theta)]])
    return np.round(matrix, 5)


B00 = np.matrix([[1, 0], [0, 0]])
B11 = np.matrix([[0, 0], [0, 1]])
I2 = np.eye(2)

X = Gate([[0, 1], [1, 0]], 'X')
Y = Gate([[0, -1j], [1j, 0]], 'Y')
Z = Gate([[1, 0], [0, -1]], 'Z')
H = Gate((X + Z) / np.sqrt(2), 'H')
CX = X.controlled.set_name('CNOT')
CZ = Z.controlled
P = Gate(phase(2), 'P')
T = Gate(phase(3), 'T')

__all__ = ['Gate', 'B00', 'B11', 'I2', 'X', 'Y', 'Z', 'H', 'P', 'T', 'phase', 'qft_matrix']
