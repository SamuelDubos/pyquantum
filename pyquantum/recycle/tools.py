from functools import reduce
import numpy as np

from pyquantum.core.qubit import Qubit


def str2qubit(string: str) -> np.ndarray:
    vectors = [np.array([eval(char), 1 - eval(char)]) for char in string]
    return reduce(lambda a, b: np.kron(a, b), vectors).T


def identical_qubits(n_qubits: int = 1, theta: float = 0, phi: float = 0):
    return reduce(lambda a, b: np.kron(a, b),
                  [Qubit(theta=theta, phi=phi, name=f'ψ{k}').matrix
                   for k in range(n_qubits)])


if __name__ == '__main__':
    STRING = '100'
    decimal = int(STRING, 2)
    print(f'Decimal: {decimal}')
    print(f'Kron1: {str2qubit(STRING)}')
