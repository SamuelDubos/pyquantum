"""
Author: @samuel_dubos
Date: January 14, 2024
"""

import matplotlib.pyplot as plt
from seaborn import heatmap
from sys import stderr
import numpy as np

from functools import reduce

from pyquantum.circuit.sketch import Sketch
from pyquantum.core.gate import *


class Circuit(Sketch):

    def __init__(self, n_qubits: int = 1):
        self.n_qubits = n_qubits
        self.matrices = []
        self.matrix, self.ax, self.settings = None, None, None
        Sketch.__init__(self, n_qubits)

    def update(self):
        self.matrix = reduce(np.dot, self.matrices) if self.matrices else None
        self.fontsize = 120 / max(self.n_qubits, len(self.gates))
        self.linewidth = np.sqrt(self.fontsize)
        self.settings = {'cmap': self.cmap, 'cbar': self.cbar, 'square': self.square,
                         'ha': 'center', 'va': 'center', 'fontsize': self.fontsize,
                         'color': 'black', 'edgecolor': 'black',
                         'linewidth': self.linewidth, 'fontweight': 'bold'}

    def set_settings(self, **kwargs):
        self.update()
        for key, value in kwargs.items():
            if key in self.settings:
                self.__setattr__(key, value)
            else:
                stderr.write(f'The parameter {key} is not accepted.')
        return self

    @staticmethod
    def conk(matrices):
        return reduce(lambda a, b: np.kron(a, b), matrices)

    def swap(self, *targets, inplace=True):
        matrix = sum([self.conk(np.array([matrix if k in targets else I2
                                       for k in range(self.n_qubits)])).real
                      for matrix in [I2, X.matrix, Y.matrix, Z.matrix]])
        self.matrices.append((matrix / 2).astype(int))
        self.gates.append(['swap', *targets])
        if not inplace:
            return self

    def hadamard(self, target, inplace=True):
        matrix = self.conk([H.matrix if k is target else I2 for k in range(self.n_qubits)])
        self.matrices.append(matrix)
        self.gates.append(['hadamard', target])
        if not inplace:
            return self

    def shift(self, control, target, inplace=True):
        r = phase(abs(control - target) + 1)
        mat1 = self.conk([I2 if k is target else B00 if k is control else I2 for k in range(self.n_qubits)])
        mat2 = self.conk([r if k is target else B11 if k is control else I2 for k in range(self.n_qubits)])
        self.matrices.append(mat1 + mat2)
        self.gates.append(['shift', control, target])
        if not inplace:
            return self

    def heatmap(self, matrix=None):
        self.update()
        matrix = matrix if matrix is not None else self.matrix
        settings = self.filter_settings('cmap', 'cbar', 'square')
        parts, titles = [matrix.real, matrix.imag], ['Real', 'Imaginary']
        if not np.any(np.iscomplex(matrix)):
            parts, titles = parts[0:1], titles[0:1]
        elif np.all(np.iscomplex(matrix)):
            parts, titles = parts[1:], titles[1:]
        _, axes = plt.subplots(1, len(parts), figsize=(20, 10))
        axes = [axes] if len(parts) == 1 else axes
        for i, (part, title) in enumerate(zip(parts, titles)):
            heatmap(part, ax=axes[i], **settings)
            axes[i].set_title(f'{title} part', fontweight='bold')
            axes[i].set_xticks([])
            axes[i].set_yticks([])
        plt.show()

    def __repr__(self):
        self.heatmap()
        return f'{self.n_qubits}-Qubits circuit'

    def __format__(self, format_spec):
        if format_spec == 'm':
            return repr(self)
        elif format_spec == 'd':
            return self.draw()


if __name__ == '__main__':
    c = Circuit(3)
    c.swap(2, 0)
