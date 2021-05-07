import numpy as np
import matplotlib.pyplot as plt
import helpers

class Training:
    def __init__(self, neuronas, factor_aprendizaje, tolerancia, limit): 
        self.neurons = neuronas
        self.learning_factor = factor_aprendizaje
        self.tolerance = tolerancia
        self.era_limit = limit
        self.eras = 0
        self.weights = [
            helpers.getRandomFloat( 0, 1, 4 ),
            helpers.getRandomFloat( 0, 1, 4 ),
            helpers.getRandomFloat( 0, 1, 4 ),
        ]

    def run(self):
        execute = True
        
        while execute:
            for neurona in self.neurons: # por cada patrón    
                neurona.w = self.weights

                # calculamos la salida (y)
                neurona.y = round( neurona.activationFunc(), 4 )

                # calculamos el error (e)
                neurona.e = round( neurona.computeError(), 4 )

                # ajustamos los pesos correspondientes
                self.weights = self.adjustWeights( neurona )
            self.eras += 1 # aumentamos el contador de épocas

            if self.eras % 200 == 0: # mostramos resultados
                print("\n-------------------------- EPOCA # {epoca} ----------------------".format(epoca=self.eras))
                helpers.PrintTabulatedTable( self.neurons )
                self.updatePlot( self.neurons )

            # verificamos errores
            promedio_errores = self.checkErrors( self.neurons )

            # aplicamos la condición de parada
            if promedio_errores <= self.tolerance:
                execute = False
                print("\n-------------------------- EPOCA # {epoca} ----------------------".format(epoca=self.eras))
                helpers.PrintTabulatedTable( self.neurons )
                self.updatePlot( self.neurons )
                print("\n [!] Algoritmo de entrenamiento finalizado. \n")

            # o si no, hasta que llegue al límite de épocas
            if self.eras == self.era_limit:
                print("\n [!] Haz alcanzado el límite de epocas. Finalizando ejecución. \n")
                break

    def adjustWeights(self, neuron):
        w = np.array( neuron.w )
        x = np.array( neuron.x )
        e = neuron.e
        dy = neuron.y * (float(1) - neuron.y)

        new_w = w + (self.learning_factor * x * e * dy)
        return [
            round( new_w[0], 4 ),
            round( new_w[1], 4 ),
            round( new_w[2], 4 )
        ]
    
    def checkErrors(self, neurons):
        suma = 0
        for neurona in neurons:
            square_error = neurona.e * neurona.e
            suma += square_error
        total = suma / len(neurons)
        return total

    def updatePlot(self, neurons):
        plt.clf() # limpiamos el gráfico para actualizarlo
        plt.figure("Práctica #3")
        plt.title("Adaline - ÉPOCA # {epoca}".format(epoca=self.eras))
        plt.grid(True)
        plt.xlim([-1, 4])
        plt.ylim([-1, 4])
        plt.show( block=False )

        line_x = []
        line_y = []

        # dibujamos puntos activos e inactivos
        for neurona in neurons:
            x = neurona.x[1]
            y = neurona.x[2]

            m = -neurona.w[1]/neurona.w[2]
            a = -neurona.w[0]/neurona.w[2]

            line_x.append(x)
            line_y.append(m*x+a)

            if neurona.d == 0:
                plt.scatter(x, y, color="red")
            elif neurona.d == 1:
                plt.scatter(x, y, color="green")
            
        # dibujamos la línea separadora
        plt.plot(line_x, line_y, color="blue")

        plt.draw()
        plt.pause(0.5)