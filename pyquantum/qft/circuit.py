from numpy import allclose
from pyquantum.circuit.circuit import Circuit
from pyquantum.core.gate import *


class QFTCircuit(Circuit):

    def __init__(self, n_qubits):
        Circuit.__init__(self, n_qubits)
        self.run()

    def run(self):
        for qubit in range(self.n_qubits):
            self.hadamard(qubit)
            for i in range(1, self.n_qubits - qubit):
                self.shift(qubit + i, qubit)
        for qubit in range(self.n_qubits // 2):
            self.swap(qubit, self.n_qubits - 1 - qubit)
        self.update()

    def close2qft(self):
        qft = qft_matrix(self.n_qubits)
        return allclose(qft, self.matrix, atol=1e-6, rtol=1e-2)


if __name__ == '__main__':
    circuit = QFTCircuit(3)
    circuit.set_settings(cmap='hot', square=False)
    print(circuit.close2qft())
    #
    # circuit = Circuit(3)
    # circuit.hadamard(1)
    # circuit.hadamard(2)
    # circuit.shift(0, 2)

    print(circuit)
    circuit.draw()
