"""
Author: @samuel_dubos
Date: January 9, 2024
"""

import matplotlib.pyplot as plt
import numpy as np

from pyquantum.core.qubit import Qubit


class BlochSphere:

    def __init__(self, figsize=(10, 10)) -> None:
        self.figsize = figsize
        self.qubits = []

    def add_qubit(self, qubit: Qubit, color: str = 'k') -> None:
        self.qubits.append([qubit, color])

    def show(self) -> None:
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection='3d')
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        ax.scatter(0, 0, 0, color='k', marker='o')
        ax.plot_surface(np.outer(np.cos(u), np.sin(v)),
                             np.outer(np.sin(u), np.sin(v)),
                             np.outer(np.ones(np.size(u)), np.cos(v)),
                             alpha=0.05, edgecolors='k', linewidth=0.2)
        for qubit, color in self.qubits:
            x = np.sin(qubit.theta) * np.cos(qubit.phi)
            y = np.sin(qubit.theta) * np.sin(qubit.phi)
            z = np.cos(qubit.theta)
            ax.plot([0, x], [0, y], [0, z], color=color, label=qubit.name)
            ax.scatter(x, y, z, color=color, marker='o')
        ax.set_box_aspect([1, 1, 1])
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')
        plt.legend()
        plt.show()
