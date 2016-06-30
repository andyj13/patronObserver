import numpy as np
from Observador import Observador
from A import A

def main():
    sujeto = A()
    observadorSuma = Observador("Suma", sujeto)
    observadorResta = Observador("Todas", sujeto)

    array1 = [4,2,1]
    array2 = [10,5,1,3]

    sujeto.agregar(array1, 1)
    sujeto.agregar(array2, 3)


if __name__ == '__main__':
    main()