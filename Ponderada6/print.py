import numpy as np
from perceptron import Gate

gate = Gate()

test1 = np.array([0, 0])
test2 = np.array([1, 0])
test3 = np.array([0, 1])
test4 = np.array([1, 1])

print("AND({}, {}) = {}".format(0, 0, gate.AND_Function(test1)))
print("AND({}, {}) = {}".format(1, 0, gate.AND_Function(test2)))
print("AND({}, {}) = {}".format(0, 1, gate.AND_Function(test3)))
print("AND({}, {}) = {} \n".format(1, 1, gate.AND_Function(test4)))

print("OR({}, {}) = {}".format(0, 0, gate.OR_Function(test1)))
print("OR({}, {}) = {}".format(1, 0, gate.OR_Function(test2)))
print("OR({}, {}) = {}".format(0, 1, gate.OR_Function(test3)))
print("OR({}, {}) = {} \n".format(1, 1, gate.OR_Function(test4)))

print("NAND({}, {}) = {}".format(0, 0, gate.NAND_Function(test1)))
print("NAND({}, {}) = {}".format(1, 0, gate.NAND_Function(test2)))
print("NAND({}, {}) = {}".format(0, 1, gate.NAND_Function(test3)))
print("NAND({}, {}) = {} \n".format(1, 1, gate.NAND_Function(test4)))

print("NOR({}, {}) = {}".format(0, 0, gate.NOR_Function(test1)))
print("NOR({}, {}) = {}".format(1, 0, gate.NOR_Function(test2)))
print("NOR({}, {}) = {}".format(0, 1, gate.NOR_Function(test3)))
print("NOR({}, {}) = {} \n".format(1, 1, gate.NOR_Function(test4)))

print("XOR({}, {}) = {}".format(0, 0, gate.XOR_Function(test1)))
print("XOR({}, {}) = {}".format(1, 0, gate.XOR_Function(test2)))
print("XOR({}, {}) = {}".format(0, 1, gate.XOR_Function(test3)))
print("XOR({}, {}) = {} \n".format(1, 1, gate.XOR_Function(test4)))