"""
Author: @samuel_dubos
Date: December 31, 2023
"""

from numpy.linalg import norm
import numpy as np

from pyquantum.qft.state import State


class Transformer:

    def __init__(self):
        self.states = []

    @staticmethod
    def normalize(state):
        return state / norm(state)

    def sinusoid(self, params, n_qubits=8, label='sinusoid'):
        x = np.arange(0, 1, 1 / (2 ** n_qubits))
        values = sum([amp * func(2 * np.pi * freq * x) for func in params for freq, amp in params[func].items()])
        state = State(x, values, n_qubits, label)
        self.states.append(state)

    def exponential(self, n_qubits=8, label='exponential'):
        x = np.arange(0, 1, 1 / (2 ** n_qubits))
        values = np.exp(x)
        state = State(x, values, n_qubits, label)
        self.states.append(state)

    def personalized(self, function, params=None, n_qubits=8, label=''):
        params = params or ()
        x = np.arange(0, 1, 1 / (2 ** n_qubits))
        values = function(x, *params)
        state = State(x, values, n_qubits, label)
        self.states.append(state)
