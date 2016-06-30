import numpy as np
from Operaciones import Operaciones


class Suma(Operaciones):

    def operacion(self, vector):
        self.total = np.sum(vector)
