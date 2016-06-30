from Sujeto import Sujeto
from Suma import Suma
from Resta import Resta

class A(Sujeto):
    def __init__(self):
        self.observadores = []
        self.arrayA = []
        self.suma = Suma()
        self.resta = Resta()

    def agregar(self, b, op):
        self.arrayA.append(b)

        if op == 1:
            self.operar(1, b)
        if op == 2:
            self.operar(2, b)
        if op == 3:
            self.operar(3, b)

    def operar(self, op, b):
        if op == 1:
            self.suma.operacion(b)
            self.notificar(self.suma.total, 0)
        if op == 2:
            self.resta.operacion(b)
            self.notificar(0, self.resta.total)
        if op == 3:
            self.suma.operacion(b)
            self.resta.operacion(b)
            self.notificar(self.suma.total, self.resta.total)


    def registrar(self, observador):
        self.observadores.append(observador)

    def notificar(self, suma, resta):
        for o in self.observadores:
            o.actualizar(suma, resta)