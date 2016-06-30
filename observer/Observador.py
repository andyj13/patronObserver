class Observador:
    def __init__(self, operador, sujeto):
        self.operador = operador
        sujeto.registrar(self)

    def actualizar(self, suma, resta):
        if self.operador == "Suma":
            print "Se detecto una suma con el resultado: " + suma
        if self.operador == "Resta":
            print "Se detecto una resta con el resultado: " + resta