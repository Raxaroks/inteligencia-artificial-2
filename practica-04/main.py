import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from mlp import MLP

NEURONAS_CAPA_OCULTA = 3
FACTOR_APRENDIZAJE  = 0.3333
TOLERANCIA = 0.075
LIMITE_EPOCAS = 2000

entradas = []
salidas = []

def handleOnClick(event):
    coord_x = round(event.xdata, 2)
    coord_y = round(event.ydata, 2)

    if event.button is MouseButton.LEFT:
        plt.scatter(coord_x, coord_y, color="#0069F6", s=50)
        entradas.append([1, coord_x, coord_y])
        salidas.append(0)
    elif event.button is MouseButton.RIGHT:
        plt.scatter(coord_x, coord_y, color="#FF4502", s=50)
        entradas.append([1, coord_x, coord_y])
        salidas.append(1)
    
    plt.draw()

    
def handleOnKeyPress(event):
    # si hay patrones, los cargamos a la red
    if event.key == "enter":
        if len(entradas) > 0:
            # ejecutamos el entrenamiento
            red_neuronal = MLP(entradas, salidas, NEURONAS_CAPA_OCULTA, FACTOR_APRENDIZAJE, TOLERANCIA, LIMITE_EPOCAS)
            red_neuronal.runTraining()
        else:
            print("\n [!] Ocurrió un error al cargar los patrones.")

    elif event.key == "backspace":
        entradas.clear()
        salidas.clear()
        # limpiamos gráfico
        plt.clf()
        plt.title("RED NEURONAL MULTICAPA")
        plt.grid(True)
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.draw()


def main():
    print("\n\t INTELIGENCIA ARTIFICIAL II - Práctica #4")

    # preparamos un gráfico vacío
    plt.figure("Práctica #4")
    plt.title("RED NEURONAL MULTICAPA")
    plt.grid(True)
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])

    # conectamos las funciones de evento onClick y keyPress
    plt.connect("button_press_event", handleOnClick)
    plt.connect("key_press_event", handleOnKeyPress)

    # mostramos el gráfico listo para recibir puntos a marcar
    print("\n [!] Mostrando un gráfico vacío...")
    plt.show()

    
if  __name__ == "__main__":
    main()