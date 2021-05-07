import math
import numpy as np

class Adaline:
    def __init__(self, inputs, wished_result):
        self.x = inputs
        self.d = wished_result
        self.w = []
        self.y = 0
        self.e = 0

    def computeResult(self):
        x = np.array(self.x)
        w = np.array(self.w)
        result = np.dot( x, w )
        return result

    def activationFunc(self):
        res = 1 / (1 + np.exp( - self.computeResult() ))
        return res

    def computeError(self):
        error = self.d - self.y
        return error
