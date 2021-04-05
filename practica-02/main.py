import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Button
from training import Training


patrones = [] # variable global


def handleOnClick(event):
    x, y = round(event.xdata, 2), round(event.ydata, 2)
    if event.button is MouseButton.LEFT:
        patrones.append( [ 1, x, y, 0 ] ) # establecemos patrón inactivo
        plt.plot( x, y, marker='o', color='red' )
        plt.draw() # dibujamos
    elif event.button is MouseButton.RIGHT:
        patrones.append( [ 1, x, y, 1 ] ) # establecemos patrón activo
        plt.plot( x, y, marker='o', color='green' )
        plt.draw() # dibujamos


def handleOnKeyPress(event):
    if event.key == 'enter':
        RunTraining( patrones )
    elif event.key == 'backspace':
        patrones.clear()
        plt.cla()
        plt.title("Perceptrón")
        plt.subplots_adjust(bottom=0.25)
        plt.grid(True)
        plt.xlim([-1, 2])
        plt.ylim([-1, 2])
        plt.draw()


def RunTraining( patterns ):
    if len(patterns) > 0:
        algoritmo = Training( patterns )
        algoritmo.run()
    else:
        print("[!] ERROR. No hay patrones en la lista.\n")

def main():
    print("\n\t\t INTELIGENCIA ARTIFICIAL - Práctica #2\n")

    # inicializamos figura
    fig = plt.figure('Práctica #2')
    plt.title( "Perceptrón" )
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.xlim([-1, 2])
    plt.ylim([-1, 2])

    # añadimos el evento de click
    plt.connect('button_press_event', handleOnClick)

    # añadimos el evento de key press para controlar el flujo del programa
    plt.connect('key_press_event', handleOnKeyPress)

    # mostramos una figura vacía con dos botones
    plt.show()


if __name__ == "__main__":
    main()
