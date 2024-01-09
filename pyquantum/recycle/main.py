"""
Author: @samuel_dubos
Date: November 23, 2023
"""

import matplotlib.colors as mc
import random as rdm
import numpy as np

from pyquantum.core.qubit import Qubit
from pyquantum.core.visualization import BlochSphere
from pyquantum.core.gate import *


def random_xyz(figsize=(10, 10), set_seed=None):
    np.seed(set_seed) if set_seed else None
    theta = rdm.uniform(0, np.pi)
    phi = rdm.uniform(0, 2 * np.pi)
    psi1 = Qubit(theta=theta, phi=phi, name='ψ1')
    x = psi1.apply(X, name='obs_x')
    y = psi1.apply(Y, name='obs_y')
    z = psi1.apply(Z, name='obs_z')
    sphere = BlochSphere(figsize)
    sphere.add_qubit(psi1, color='red')
    sphere.add_qubit(x, color='green')
    sphere.add_qubit(y, color='blue')
    sphere.add_qubit(z, color='yellow')
    sphere.show()


def random_gates(figsize):
    theta = rdm.uniform(0, np.pi)
    phi = rdm.uniform(0, 2 * np.pi)
    psi = Qubit(theta=theta, phi=phi, name='ψ1')
    h = psi.apply(H, name='Hadamard')
    p = psi.apply(P, name='Pi/4')
    t = psi.apply(T, name='Pi/8')
    sphere = BlochSphere(figsize)
    sphere.add_qubit(psi, color='red')
    sphere.add_qubit(h, color='blue')
    sphere.add_qubit(p, color='green')
    sphere.add_qubit(t, color='yellow')
    sphere.show()


def successive(gate, iterations: int = 1):
    theta = rdm.uniform(0, np.pi)
    phi = rdm.uniform(0, 2 * np.pi)
    psi = Qubit(theta=theta, phi=phi, name='ψ1')
    sphere = BlochSphere()
    qubit = psi
    for k in range(iterations):
        sphere.add_qubit(qubit, color=list(mc.TABLEAU_COLORS.values())[k % 10])
        qubit = qubit.apply(gate, name=f'Iteration n°{k + 1}')
    sphere.show()


if __name__ == '__main__':
    # Pauli gates example
    # random_xyz()

    # Successive rotations
    successive(P, iterations=7)
