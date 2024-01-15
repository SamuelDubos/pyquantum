"""
Author: @samuel_dubos
Date: January 15, 2024
"""

import numpy as np

from pyquantum.qft.circuit import QFTCircuit


class State:

    def __init__(self, x, values, n_qubits, label):
        self.x = x
        self.n = 2 ** n_qubits
        self.values = values
        self.n_qubits = n_qubits
        self.fe = 1 / self.n
        self.freq = np.array(self.get_freq()[:, :self.n // 2].T)
        self.x_freq = (np.arange(self.n) / (self.n * self.fe))[:self.n // 2]
        self.label = label

    def get_freq(self):
        qft = QFTCircuit(self.n_qubits)
        freq = np.round(qft.matrix @ self.values, 5)
        return np.abs(np.matrix(freq).T).flatten()
