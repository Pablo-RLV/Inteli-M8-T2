import numpy as np
from models import Model

class Gate:
    def __init__(self):
        self.model = Model()

    def NOT_Function(self, x):
        wNOT = -1
        bNOT = 0.5
        return self.model.perceptronModel(x, wNOT, bNOT)

    def AND_Function(self, x):
        w = np.array([1, 1])
        bAND = -1.5
        return self.model.perceptronModel(x, w, bAND)

    def OR_Function(self, x):
        w = np.array([1, 1])
        bOR = -0.5
        return self.model.perceptronModel(x, w, bOR)

    def NAND_Function(self, x):
        output_AND = self.AND_Function(x)
        output_NOT = self.NOT_Function(output_AND)
        return output_NOT

    def NOR_Function(self, x):
        output_OR = self.OR_Function(x)
        output_NOT = self.NOT_Function(output_OR)
        return output_NOT

    def XOR_Function(self, x):
        output_AND = self.AND_Function(x)
        output_NOT = self.NOT_Function(output_AND)
        output_OR = self.OR_Function(x)
        w = np.array([output_NOT, output_OR])
        output_XOR = self.AND_Function(w)
        return output_XOR