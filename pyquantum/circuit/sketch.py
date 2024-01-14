"""
Author: @samuel_dubos
Date: January 14, 2024
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Sketch:

    def __init__(self, n_qubits: int = 1, length: int = 0, title: str = ''):
        self.n_qubits = n_qubits
        self.length = length
        self.title = title
        self.fig, self.ax = None, None
        self.settings = None
        self.gates = []
        self.cmap = 'viridis'
        self.cbar, self.square = True, True
        self.fontsize, self.linewidth = 16, 4
        self.update()

    def update(self):
        self.settings = {'cmap': self.cmap, 'cbar': self.cbar, 'square': self.square,
                         'ha': 'center', 'va': 'center', 'fontsize': self.fontsize,
                         'color': 'black', 'edgecolor': 'black',
                         'linewidth': self.linewidth, 'fontweight': 'bold'}

    def filter_settings(self, *keys):
        self.update()
        return {key: self.settings[key] for key in keys if key in self.settings}

    def add_vertical(self, index, targets):
        settings = self.filter_settings('color', 'linewidth')
        self.ax.plot([index + 0.25, index + 0.25], [-targets[0], -targets[1]], zorder=1, **settings)

    def add_horizontal(self, target):
        settings = self.filter_settings('color', 'linewidth')
        self.ax.plot([-0.5, len(self.gates)], [-target, -target], zorder=1, **settings)

    def add_square(self, index, target, facecolor, size=0.5):
        settings = self.filter_settings('linewidth', 'edgecolor')
        rectangle = patches.Rectangle((index, -target - 0.25), size, size, facecolor=facecolor, zorder=2, **settings)
        self.ax.add_patch(rectangle)

    def add_text(self, index, target, text):
        settings = self.filter_settings('fontsize', 'ha', 'va', 'color', 'fontweight')
        self.ax.text(index + 0.25, -target, text, zorder=3, **settings)

    def add_cross(self, x, y, height=0.15, width=0.25):
        settings = self.filter_settings('edgecolor', 'linewidth')
        for k in [-1, 1]:
            coords = [(x - width, y + k * height), (x + width, y - k * height)]
            cross = patches.Polygon(coords, **settings)
            self.ax.add_patch(cross)

    def add_circle(self, index, target):
        circle = patches.Circle((index + 0.25, -target), self.settings['linewidth'] / 40, facecolor='black')
        self.ax.add_patch(circle)

    def add_swap(self, index, targets):
        self.add_vertical(index, targets)
        self.add_cross(index + 0.25, -targets[0])
        self.add_cross(index + 0.25, -targets[1])

    def add_hadamard(self, index, target):
        self.add_square(index, target, 'lightblue')
        self.add_text(index, target, 'H')

    def add_shift(self, index, control, target):
        self.add_square(index, target, 'lightcoral')
        self.add_text(index, target, f'R{abs(control - target) + 1}')
        self.add_vertical(index, [control, target])
        self.add_circle(index, control)

    def initialize(self):
        self.fig, self.ax = plt.subplots(figsize=(20, 10))
        self.fig.suptitle(self.title, fontsize=20, fontweight='bold')
        for qubit in range(self.n_qubits):
            self.add_horizontal(qubit)
            self.add_text(-1.05, qubit, f'|x{qubit}⟩')

    def show(self):
        self.ax.axis('equal')
        self.ax.axis('off')
        plt.show()

    def __enter__(self):
        self.gates = self.length * [None]
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.show()

    def draw(self):
        self.initialize()
        for index, gate in enumerate(self.gates):
            name, *params = gate
            if name == 'swap':
                self.add_swap(index, params)
            elif name == 'hadamard':
                self.add_hadamard(index, *params)
            elif name == 'shift':
                self.add_shift(index, *params)
        self.show()
