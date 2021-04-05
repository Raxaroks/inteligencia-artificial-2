import numpy as np
from matplotlib import pyplot as plt
from numpy.core.shape_base import block
from adaline import Adaline
import helpers

ETA = 0.00675
ERA_LIMIT = 100

class Training:
    
    def __init__(self, patrones):
        self.patterns = patrones
        self.eras = 0
        self.weights = []


    def run(self):
        execute = True # bandera para ejecutar el programa
        self.weights = [
            helpers.getRandomFloat( 0, 1, 3 ),
            helpers.getRandomFloat( 0, 1, 3 ),
            helpers.getRandomFloat( 0, 1, 3 ),
        ]
        self.eras += 1

        print("primer conjunto de pesos!!!", self.weights)

        while execute:
            neuronas = []
            for patron in self.patterns:
                x = [ patron[0], patron[1], patron[2] ]
                d = patron[3]
                neurona = Adaline( x, d )
                neurona.w = self.weights

                # calculamos la salida 'y'
                neurona.y = round( neurona.activationFunc( neurona.computeResult() ), 3 )

                # calculamos el error 'e'
                neurona.e = round( neurona.computeError(), 3 )

                # ajustamos los pesos para resolver el siguiente patrón de la neurona
                self.weights = self.adjustWeights( neurona )

                neuronas.append( neurona )

            if self.eras % 2 == 0:
                self.PrintEra(neuronas) # mostramos los resultados de la neurona en consola
                self.UpdatePlot(neuronas) # mostramos los resultados en una gráfica

            self.eras += 1 # aumentamos el contador de épocas

            # verificamos si hay errores
            execute = self.checkForErrors( neuronas )
            if execute == False:
                print("\n ALGORITMO DE ENTRENAMIENTO FINALIZADO. \n")

            # establecemos el límite de épocas
            if self.eras > ERA_LIMIT:
                print("\n [!] Se ha alcanzado el límite de épocas establecido. Terminando el algoritmo. \n")
                break


    def adjustWeights(self, neuron):
        new_weights = []
        actual_weights = np.array( self.weights )
        actual_inputs = np.array( neuron.x )
        actual_error = neuron.e
        dy = neuron.y * (1-neuron.y)

        new_weights = actual_weights + ((ETA * actual_inputs) * actual_error * dy)

        # print("\n\n")
        # print("Ajustando pesos . . .")
        # print("W(k+1) = ", new_weights)
        # print("\n\n")

        return [
            round(new_weights[0], 3),
            round(new_weights[1], 3),
            round(new_weights[2], 3),
        ]


    def checkForErrors(self, neurons):
        flag = False
        for neuron in neurons:
            if neuron.e != 0:
                flag = True
        return flag


    def UpdatePlot(self, neurons):
        x_array = []
        y_array = []

        actives = []
        inactives = []

        for n in neurons:
            if n.d == 0:
                inactives.append( [n.x[1], n.x[2] ] )
            else:
                actives.append([n.x[1], n.x[2]])
            
        for n in neurons:
            x = n.x[1]
            m = -(n.w[1]/n.w[2])
            a = n.w[0]/n.w[2]
            y = m * x + a
            x_array.append(x)
            y_array.append(y)
        
        plt.clf()

        plt.title("Adaline - ÉPOCA #{epoca}".format(epoca=self.eras))
        plt.grid(True)
        plt.xlim( [-1, 4] )
        plt.ylim( [-1, 4] )

        plt.scatter( [element[0] for element in inactives], [element[1] for element in inactives], color="red" )
        plt.scatter( [element[0] for element in actives], [element[1] for element in actives], color="green" )
        plt.plot( x_array, y_array, color='blue' )

        plt.show( block=False )
        plt.pause(0.5)



    def PrintEra(self, neurons):
        print("\n---------------------------------- ÉPOCA #{era} ------------------------------------------".format(era=self.eras))
        helpers.PrintTabulatedTable(neurons)
