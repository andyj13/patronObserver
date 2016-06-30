class Sujeto:
    def __init__(self):
        self.observadores = []

    def registrar(self, observador):
        self.observadores.append(observador)

    def notificar(self):
        pass