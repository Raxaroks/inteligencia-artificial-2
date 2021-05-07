import numpy as np

class Neuron:
    def __init__(self, inputs, weights, wish):
        self.x = inputs
        self.w = weights
        self.d = wish
        self.y = 0
        self.e = 0

    def getV(self):
        x = np.array(self.x)
        w = np.array(self.w)
        dot = np.dot(x, w)
        return dot

    def getDy(self):
        derivative = self.y * (1 - self.y)
        return derivative
