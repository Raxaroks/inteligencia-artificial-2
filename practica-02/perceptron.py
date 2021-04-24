import numpy as np

class Perceptron:
    def __init__(self, inputs, wished_result):
        self.x = inputs
        self.d = wished_result
        self.w = []
        self.y = 0
        self.e = 0

    def solveY(self):
        a = np.array( [self.x[1], self.x[2]] )
        b = np.array( [self.w[1], self.w[2]] )
        res = np.dot(a, b) - self.w[0]
        return res
    
    def solveE(self):
        error = self.d - self.y
        return error
