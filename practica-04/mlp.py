from helpers import getRandomFloat, PrintTabulatedTable
from neuron import Neuron
import numpy as np
import matplotlib.pyplot as plt

"""
    ALGORITMO DE ENTRENAMIENTO DE UNA RED NEURONAL MULTICAPA

    Paso 1: 
        Inicializamos todos los pesos al azar, de todas las neuronas de la red.

    Paso 2:
        Por cada patrón de entrenamiento:
        -> calcular la salida de toda la red neuronal (etapa hacia adelante); calcular el resultado de la capa de salida.
        -> calcular el error; el cual es la diferencia entre el resultado deseado y el resultado de la capa de salida.
        -> ajustar pesos de toda la red neuronal (etapa hacia atrás): empezando desde la última capa, recorriendo capa por capa hasta llegar a la primera.

    Paso 3:
        Verificar la condición de parada: al terminar de procesar todos los patrones de la red, se eleva al cuadrado el error (o errores) de cada salida y se promedia, para verificar si pasa el rango de tolerancia; si esto se cumple, se ejecuta otra época, si no, se termina la ejecución del algoritmo.
"""

MOD_VAL = 100
DECIMALES = 5

class MLP:
    def __init__(self, inputs, outputs, hidden_layer_length, learn_factor, threshold, epoch_limit):
        self.inputs = inputs
        self.outputs = outputs
        self.hidden_layer_length = hidden_layer_length
        self.learn_factor = learn_factor
        self.threshold = threshold
        self.epoch_limit = epoch_limit
        self.current_weights = []

    def runTraining(self):
        epoca = 0
        cantidad_patrones = len(self.inputs)

        # PASO 1: inicializamos pesos aleatorios, por cada neurona en toda la red
        for i in range(self.hidden_layer_length+1):
            self.current_weights.append([
                getRandomFloat(-1, 1, DECIMALES),
                getRandomFloat(-1, 1, DECIMALES),
                getRandomFloat(-1, 1, DECIMALES),
            ])

        execute = True
        while execute:
            errores = []
            resultados = []

            # PASO 2: el entrenamiento se divide en 3 etapas, por cada conjunto de patrones de entradas 
            for i in range(cantidad_patrones):
                # if i == 1:
                #     break
                x = self.inputs[i]
                d = self.outputs[i]

                # -> etapa hacia adelante: calcular la salida de la red
                # formamos y procesamos las neuronas de la capa oculta
                hidden_layer = []
                for j in range(self.hidden_layer_length):
                    nrn = Neuron(x, self.current_weights[j], d)
                    # calculamos salida y
                    nrn.y = round(self.logisticFunc(nrn.getV()), DECIMALES)
                    # # calculamos error e
                    # nrn.e = round((nrn.d - nrn.y), DECIMALES)
                    hidden_layer.append(nrn)

                # procesamos la capa de salida, la cual en esta implementación, consta de una sola neurona
                output_x = []
                for neuron in hidden_layer:
                    inp = neuron.y
                    output_x.append(inp)

                output_nrn = Neuron(output_x, self.current_weights[ len(self.current_weights) - 1 ], d)
                # calculamos salida y
                output_nrn.y = round(self.logisticFunc(output_nrn.getV()), DECIMALES)
                # # calculamos error e
                output_nrn.e = round((output_nrn.d - output_nrn.y), DECIMALES)
                errores.append(output_nrn.e)

                # -> etapa hacia atrás: ajuste de pesos
                # comenzamos con la capa de salida
                output_local_gradient = self.outputLayer_localGradient(output_nrn.getDy(), output_nrn.e)

                # print("\npesos de salida ------------->", output_nrn.w)
                output_nrn.w = self.adjustWeights(output_nrn.w, output_local_gradient, output_x)
                # print("pesos de salida ajustados --->", self.adjustWeights(output_nrn.w, output_local_gradient, output_x))

                # continuamos con la capa oculta
                pos = 0
                for neuron in hidden_layer:
                    hidden_local_gradient = self.hiddenLayer_localGradient(
                        neuron.getDy(), output_nrn.w[pos], output_local_gradient
                    )
                    # print("neurona oculta {index} ----------->".format(index=pos), neuron.w)
                    neuron.w = self.adjustWeights(neuron.w, hidden_local_gradient, x)
                    # print("neurona oculta ajustada {index} -->".format(index=pos), neuron.w)
                    pos += 1

                # almacenamos los pesos ajustados para la siguiente iteración
                self.current_weights.clear()
                for neuron in hidden_layer:
                    self.current_weights.append(neuron.w)
                self.current_weights.append(output_nrn.w)

                # guardamos los resultados de esta iteración -> [entradas, salida_d, salida_y, error, pesos]
                resultados.append([x, d, output_nrn.y, output_nrn.e, output_nrn.w])
            epoca += 1

            if epoca == self.epoch_limit:
                self.showResults(epoca, resultados, final=True)    
                print("\n [!] LÍMITE DE EPOCAS ALCANZADO.\n")
                break

            # mostramos los resultaddos de la época
            if epoca % MOD_VAL == 0:
                self.showResults(epoca, resultados, final=False)

            # PASO 3: verificar la condición de parada   
            execute = self.checkErrors(errores)
            if execute == False:
                self.showResults(epoca, resultados, final=True)    
                print("\n [!] ALGORITMO FINALIZADO.\n")


    def logisticFunc(self, nrn_v):
        result = 1 / (1 + np.exp(-nrn_v))
        return result

    def adjustWeights(self, current_weights, current_local_gradient, previous_outputs):
        # print("\n ajuste de pesos")
        # print(current_weights, current_local_gradient, previous_outputs)
        # print("\n")
        result = current_weights + self.learn_factor * (np.multiply(current_local_gradient, previous_outputs))
        return  [
            round(result[0], DECIMALES),
            round(result[1], DECIMALES),
            round(result[2], DECIMALES),
        ]

    def checkErrors(self, error_list):
        for i in range( len(error_list) ):
            error_list[i] = error_list[i] * error_list[i]
        average_error = sum(error_list)/len(error_list)
        # print("error promedio -->", average_error)
        if average_error > self.threshold:
            return True
        else:
            return False

    def outputLayer_localGradient(self, output_y_derivative, current_error):
        # print("\n gradiente local capa salida")
        # print(output_y_derivative, current_error)
        # print("\n")
        result = output_y_derivative * current_error
        return result

    def hiddenLayer_localGradient(self, output_y_derivative, previous_weight, previous_local_gradient):
        result = output_y_derivative * np.multiply(previous_weight, previous_local_gradient)
        return result

    def trainGrid(self):
        # procesamos los parámetros para convertirlos en patrones de entrada
        def_weights = self.current_weights
        x = np.linspace(-2, 2, 20)
        y = np.linspace(-2, 2, 20)
        xx, yy = np.meshgrid(x, y)

        coords = []
        for a, b in zip(xx, yy):
            for ax, bx in zip(a, b):
                coords.append((ax, bx))

        for patron in coords:
            entradas = [1, patron[0], patron[1]]
            # procesamos capa oculta
            hidden = []
            for n in range(self.hidden_layer_length):
                neurona = Neuron(entradas, def_weights[n], 0)
                neurona.y = self.logisticFunc(neurona.getV())
                hidden.append(neurona)
            
            next_inputs = []
            for n in hidden:
                next_inputs.append(n.y)
            
            # calculamos su resultado en base a la neurona de salida
            neurona_salida = Neuron(next_inputs, def_weights[len(def_weights)-1], 0)
            neurona_salida.y = self.logisticFunc(neurona_salida.getV())

            if neurona_salida.y >= 0.5:
                plt.scatter( entradas[1], entradas[2], color="#48E723", s=10 )
            else:
                plt.scatter( entradas[1], entradas[2], color="#FBC402", s=10 )
        

                
    def graph(self, epoch, iteration):
        # fig, ax = plt.subplots()
        plt.clf()
        plt.title("RED NEURONAL MULTICAPA - ÉPOCA #{epoca}".format(epoca=epoch))
        plt.grid(True)
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])

        self.trainGrid()

        # marcamos puntos
        for element in iteration:
            x = element[0]
            y = element[2]

            if y >= 0.5:
                plt.scatter(x[1], x[2], color="#FF4502", s=50)
            else:
                plt.scatter(x[1], x[2], color="#0069F6", s=50)

        plt.draw()
        plt.show(block=False)
        plt.pause(1.0)

    def showResults(self, epoch, iteration, final):
        print("\n------------------------- ÉPOCA #{epoca} ----------------------------".format(epoca=epoch))
        PrintTabulatedTable(iteration)
        self.graph(epoch, iteration)

        if final: 
            # guarda el ultimo gráfico en una imagen
            plt.savefig("results_{epoca}.png".format(epoca=epoch), dpi=400, )

    