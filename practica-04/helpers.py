import random
from tabulate import tabulate

def getRandomFloat(start, end, accuracy):
    """ Funcion para generar un número flotante aleatorio, dado un rango de inicio y fin, y un número de decimales
        después del punto """
    return round( random.uniform(start, end), accuracy )

def PrintTabulatedTable(list):
    """ Función para imprimir los datos correspondientes de una manera tabulada. """
    data = []
    for element in list:
        data.append([ element[0], element[1], element[2], element[3], element[4], ])
    print( tabulate(data, headers=["Entradas", "Salidas deseadas", "Salidas", "Errores", "Pesos"]) )
