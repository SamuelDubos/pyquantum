import matplotlib.pyplot as plt

from pyquantum.qft.transformer import Transformer


class Graph(Transformer):

    def __init__(self, title):
        Transformer.__init__(self)
        self.title = title
        self.fig, self.axes = plt.subplots(2, 1, figsize=(20, 10))

    def show_states(self):
        for state in self.states:
            self.axes[0].plot(state.x, state.values, label=f'{state.label} signal')
            self.axes[1].plot(state.x_freq, state.freq, label=f'{state.label} QFT')

    def show(self):
        self.show_states()
        self.fig.suptitle(self.title)
        for ax in self.axes:
            ax.grid(True)
            ax.legend()
        plt.show()