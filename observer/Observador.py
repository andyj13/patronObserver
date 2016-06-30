class Observador:
    def __init__(self, suma, resta, sujeto):
        self.suma = suma
        self.resta = resta
        sujeto.registrar(self)

    def actualizar(self):
        if(self.suma):
            print "Se detecto una suma"
        if(self.resta):
            print "Se detecto una resta"