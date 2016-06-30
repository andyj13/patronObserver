class Observador:
    def __init__(self, operador, sujeto):
        self.operador = operador
        sujeto.registrar(self)

    def actualizar(self, suma, resta, op):
        if self.operador == "Suma" and op == 1:
            print "Se detecto una suma con el resultado: " + str(suma)
        if self.operador == "Resta" and op == 2:
            print "Se detecto una resta con el resultado: " + str(resta)
        elif op == 3:
            print "Se detecto una suma con el resultado: " + str(suma)
            print "Se detecto una resta con el resultado: " + str(resta)