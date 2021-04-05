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
        a = np.array( [self.x[1], self.x[2]] )
        b = np.array( [self.w[1], self.w[2]] )
        dot = np.dot( a, b )
        return dot


    def activationFunc(self, v):
        result = 1 / (1 + math.exp(-v))
        return result


    def computeError(self):
        error = self.d - self.y
        return error
