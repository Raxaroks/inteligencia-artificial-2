from adaline import Adaline
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from training import Training

ETA = 0.002
TOLERANCIA = 0.05
LIMITE_EPOCAS = 2000

# patrones = [] # variable global
neuronas = []

def handleOnClick(event):
    x = round( event.xdata, 2 )
    y = round( event.ydata, 2 )

    if event.button is MouseButton.LEFT: # guardamos y dibujamos un punto inactivo
        # patrones.append( [1, x, y, 0] )
        neuronas.append( Adaline([1, x, y], 0) )
        plt.plot( x, y, marker='o', color='red' )
        plt.draw()
    elif event.button is MouseButton.RIGHT:  # guardamos y dibujamos un punto activo
        # patrones.append( [1, x, y, 1] )
        plt.plot(x, y, marker='o', color='green')
        neuronas.append( Adaline([1, x, y], 1) )
        plt.draw()


def handleOnKeyPress(event):
    if event.key == "enter": # inicializamos y ejecutamos el algoritmo de entrenamiento
        if len( neuronas ) > 0:
            algoritmo = Training( neuronas, ETA, TOLERANCIA, LIMITE_EPOCAS )
            algoritmo.run()
        else:
            print("[!] ERROR: no hay patrones en la lista.\n")

    elif event.key == "backspace": # limpiamos el gráfico y la lista de patrones
        neuronas.clear()
        plt.cla()
        plt.title("Adaline")
        plt.grid(True)
        plt.xlim([-1, 4])
        plt.ylim([-1, 4])
        plt.draw()


def main():
    # inicializamos una figura vacía
    plt.figure("Práctica #3")
    plt.title("Adaline")
    plt.grid(True)
    plt.xlim([-1, 4])
    plt.ylim([-1, 4])

    # añadimos el evento de click
    plt.connect( "button_press_event", handleOnClick )

    # añadimos el evento key press para controlar las acciones del programa
    plt.connect( "key_press_event", handleOnKeyPress )

    # mostramos la figura
    plt.show()


if __name__ == "__main__":
    main()
