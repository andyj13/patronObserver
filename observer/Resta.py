from Operaciones import Operaciones
class Resta(Operaciones):

    def operacion(self, vector):
        resta = vector[0]
        for i in range(1, len(vector)):
            resta = resta - vector[i]

        self.total = resta
