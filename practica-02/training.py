from matplotlib import pyplot as plt
from numpy.core.defchararray import mod
from numpy.core.shape_base import block
import helpers
from perceptron import Perceptron
import numpy as np

LIMITE_EPOCAS = 200  # constante
ETHA = 0.008

class Training:
    def __init__(self, patterns):
        self.patrones = patterns # de aquí formamos las neuronas ( x1, x2, d )
        self.epocas = 0
        self.pesos = []

    def run(self):
        execute = True
        self.pesos = [
            helpers.getRandomFloat( 0, 1, 2 ),
            helpers.getRandomFloat( 0, 1, 2 ),
            helpers.getRandomFloat( 0, 1, 2 ),
        ]  # inicializamos de manera aleatoria el primer conjunto de pesos (ya incluye el bias/umbral)

        self.epocas += 1 # iniciamos en la primera época

        while execute:
            neuronas = []  # lista de neuronas vacía
            for patron in self.patrones:  # por cada patrón
                # formamos la neurona
                x = [ patron[0], patron[1], patron[2] ]     
                d = patron[3]  
                neurona = Perceptron(x, d)
                neurona.w = self.pesos # asignamos el peso correspondiente                  

                # calculamos salida 'y'
                if neurona.solveY() > 0: # función de activación
                    neurona.y = 1
                else :
                    neurona.y = 0

                # calculamos error 'e'
                neurona.e = neurona.solveE()
                
                # ajustamos los pesos para el siguiente patrón
                self.pesos = self.adjustWeights(neurona)  

                neuronas.append( neurona )

            # mostramos los resultados de la neurona en consola
            if self.epocas % 10 == 0:
                print("--------------------- ÉPOCA {epoca} -----------------------------------------------------------".format(epoca = self.epocas))
                print("X0\t", "X1  \t", "X2  \t", "d  \t", "y  \t", "e  \t", "W0  \t", "W1  \t", "W2  \t")
                for n in neuronas:
                    print(n.x[0], "\t", n.x[1], "\t", n.x[2], "\t", n.d, "\t", n.y, "\t", n.e, "\t", n.w[0], "\t", n.w[1], "\t", n.w[2], "\t")
                print("-----------------------------------------------------------------------------------------\n")
                # mostramos la línea separadora graficando en cada época
                self.plotLine(neuronas)
            
            self.epocas = self.epocas + 1 # actualizamos el número de épocas

            # verificamos si hay errores
            execute = self.checkForErrors(neuronas)
            if execute == False:
                self.plotLine(neuronas)
                print("--------------------- ÉPOCA {epoca} -----------------------------------------------------------".format(epoca=self.epocas))
                print("X0\t", "X1  \t", "X2  \t", "d  \t", "y  \t", "e  \t", "W0  \t", "W1  \t", "W2  \t")
                print("\n LÍMITE DE ÉPOCAS ALCANZADO!!!")
                print("\n ENTRENAMIENTO FINALIZADO!!!")
            if self.epocas > LIMITE_EPOCAS:
                self.plotLine(neuronas)
                print("--------------------- ÉPOCA {epoca} -----------------------------------------------------------".format(epoca=self.epocas))
                print("X0\t", "X1  \t", "X2  \t", "d  \t", "y  \t", "e  \t", "W0  \t", "W1  \t", "W2  \t")
                print("\n LÍMITE DE ÉPOCAS ALCANZADO!!!")
                break

    def adjustWeights(self, neuron):
        w = np.array(self.pesos)
        x = np.array(neuron.x)
        e = neuron.e
        new_weights = w + ( ETHA * ( x * e ) )
        return [ round(new_weights[0], 2), round(new_weights[1], 2), round(new_weights[2], 2) ]

    def checkForErrors(self, neurons):
        flag = False
        for neuron in neurons:
            if neuron.e != 0:
                flag = True
        return flag

    def plotLine(self, neurons):
        x_array = []
        y_array = []

        actives = []
        inactives = []

        for n in neurons:
            if n.d == 0: # inactivo
                inactives.append( [ n.x[1], n.x[2] ] )
            else:
                actives.append( [ n.x[1], n.x[2] ] )

        for n in neurons:
            x = n.x[1]
            m = -(n.w[1] / n.w[2])
            a = n.w[0] / n.w[2]
            y = m * x + a
            x_array.append( x )
            y_array.append( y )
        
        plt.clf()

        plt.title("Perceptrón - ÉPOCA #{epoca}".format(epoca=self.epocas))
        plt.subplots_adjust(bottom=0.25)
        plt.grid(True)
        plt.xlim([-1, 2])
        plt.ylim([-1, 2])

        plt.scatter( [elemento[0] for elemento in inactives], [elemento[1] for elemento in inactives], color='red', ) # puntos inactivos
        plt.scatter( [elemento[0] for elemento in actives], [elemento[1] for elemento in actives], color='green', ) # puntos activos
        plt.plot( x_array, y_array, color="blue" ) # línea separadora
        plt.show(block=False)
        plt.pause(0.5)

