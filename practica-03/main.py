import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from training import Training

patrones = [] # variable global

def handleOnClick(event):
    x = round( event.xdata, 2 )
    y = round( event.ydata, 2 )

    if event.button is MouseButton.LEFT: # guardamos y dibujamos un punto inactivo
        patrones.append( [1, x, y, 0] )
        plt.plot( x, y, marker='o', color='red' )
        plt.draw()
    elif event.button is MouseButton.RIGHT:  # guardamos y dibujamos un punto activo
        patrones.append( [1, x, y, 1] )
        plt.plot(x, y, marker='o', color='green')
        plt.draw()


def handleOnKeyPress(event):
    if event.key == "enter": # inicializamos y ejecutamos el algoritmo de entrenamiento
        if len( patrones ) > 0:
            algoritmo = Training(patrones)
            algoritmo.run()
        else:
            print("[!] ERROR: no hay patrones en la lista.\n")

    elif event.key == "backspace": # limpiamos el gráfico y la lista de patrones
        plt.cla()
        plt.title("Adaline")
        plt.grid(True)
        plt.xlim( [-1, 4] )
        plt.ylim( [-1, 4] )
        plt.draw()


def main():
    print("\n\t\t INTELIGENCIA ARTIFICIAL - PRÁCTICA #3 \n")

    # inicializamos una figura vacía
    fig = plt.figure("Práctica #3")
    plt.title("Adaline")
    plt.grid(True)
    plt.xlim( [-1, 4] )
    plt.ylim( [-1, 4] )

    # añadimos el evento de click
    plt.connect( "button_press_event", handleOnClick )

    # añadimos el evento key press para controlar las acciones del programa
    plt.connect( "key_press_event", handleOnKeyPress )

    # mostramos la figura
    plt.show()


if __name__ == "__main__":
    main()
