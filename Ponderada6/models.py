import numpy as np

class Model:
    def unitStep(self, v):
        if v >= 0:
            return 1
        else:
            return 0
        
    def perceptronModel(self, x, w, b):
        v = np.dot(w, x) + b
        y = self.unitStep(v)
        return y