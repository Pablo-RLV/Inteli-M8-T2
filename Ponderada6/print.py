import numpy as np
from perceptron import Gate

gate = Gate()

inputs = [
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1)
]

logic_gates = {
    'AND': gate.AND_Function,
    'OR': gate.OR_Function,
    'NAND': gate.NAND_Function,
    'NOR': gate.NOR_Function,
    'XOR': gate.XOR_Function
}

for gate_name, gate_function in logic_gates.items():
    print(f"\nTesting {gate_name} gate:")
    for input_values in inputs:
        result = gate_function(np.array(input_values))
        print(f"{gate_name}({input_values[0]}, {input_values[1]}) = {result}")
