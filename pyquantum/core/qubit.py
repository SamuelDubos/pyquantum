"""
Author: @samuel_dubos
Date: January 14, 2024
"""

import numpy.linalg as nl
import numpy as np

from pyquantum.core.gate import Gate


class Qubit:

    def __init__(self, theta: float = np.pi / 2,
                 phi: float = np.pi,
                 name: str = '') -> None:
        self.theta = theta
        self.phi = phi
        self.name = name
        self.alpha = np.cos(self.theta / 2)
        self.beta = np.exp(self.phi * 1j) * np.sin(self.theta / 2)
        self.matrix = np.matrix([[self.alpha], [self.beta]])

    @property
    def dual(self):
        return np.array(self.matrix.H)

    @property
    def probabilities(self):
        p0 = nl.norm(self.alpha) ** 2
        p1 = nl.norm(self.beta) ** 2
        return p0, p1

    @property
    def angles(self):
        return f'θ: {self.theta}, φ: {self.phi}'

    def __mul__(self, other):
        return np.kron(self.matrix, other.matrix)

    def apply(self, gate: Gate, name: str = ''):
        observation = gate * self.matrix
        r = observation[0, 0].real / np.cos(np.angle(observation[0, 0]))
        theta = 2 * np.arccos(r)
        phi = (np.angle(observation[1, 0]) - np.angle(observation[0, 0]))
        return Qubit(theta, phi, name)

    def __format__(self, format_spec):
        precision = 2
        if format_spec == 'n':
            return f'{self.alpha:.{precision}f} ' \
                   f'{self.beta:.{precision}f}'
        elif format_spec == 's':
            return f'{self.alpha:+.{precision}f}|0>  ' \
                   f'{self.beta:+.{precision}f}|1>'
        else:
            return f'{self.alpha} {self.beta}'

    def __repr__(self):
        return f'{self:s}'
