# *pyquantum*

## 3-Qubits Quantum Fourier Transform circuit
```
from pyquantum.qft.circuit import QFTCircuit

qft3 = QFTCircuit(n_qubits=3)
qft3.draw()
```
![alt text](pyquantum/images/circuit.png?raw=true)

## 7-Qubits Quantum Fourier Transform heatmap
```
from pyquantum.qft.circuit import QFTCircuit

qft7 = QFTCircuit(7)
qft7.set_settings(cmap='hot_r', cbar=True)
qft7
```
![alt text](pyquantum/images/heatmap.png?raw=true)

## Sketch class demonstration
```
from pyquantum.circuit.sketch import Sketch

with Sketch(n_qubits=3, length=4, title='Example Circuit') as s:

    index, target, control = 0, 0, 1
    s.add_square(index=index, target=target, facecolor='lightblue')
    s.add_text(index=index, target=target, text='Gate n°1\nControlled')
    s.add_circle(index=index, target=control)
    s.add_vertical(index=index, targets=[control, target])

    index, target = 1, 1
    s.add_square(index=index, target=target, facecolor='lightcoral')
    s.add_text(index=index, target=target, text='Gate n°2')

    index, target, control = 2, 0, 2
    s.add_square(index=index, target=target, facecolor='lightgreen')
    s.add_text(index=index, target=target, text='Gate n°3\nControlled')
    s.add_circle(index=index, target=control)
    s.add_vertical(index=index, targets=[control, target])

    index, target, control = 3, 1, 2
    s.add_swap(index=index, targets=[control, target])
 ```
![alt text](pyquantum/images/example_circuit.png?raw=true)

## Sinusoid function decomposition
```
from pyquantum.qft.graph import Graph
import numpy as np

graph = Graph('Quantum Fourier Transform')
graph.sinusoid(params={np.sin: {5: 2, 8: 1}}, n_qubits=8)
graph.show()
```
![alt text](pyquantum/images/decomposition.png?raw=true)
