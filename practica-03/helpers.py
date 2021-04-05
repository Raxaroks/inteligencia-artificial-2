import random
from tabulate import tabulate

def getRandomFloat(start, end, precision):
    return round(random.uniform(start, end), precision)

def PrintTabulatedTable( list ):
    data = []
    for i in range(len(list)):
        element = list[i]
        data.append( [element.x, element.d, element.y, element.e, element.w] )
    print( tabulate( data, headers=["X0   X1   X2", "d", "Y", "e", "W0   W1   W2"] ) )
