import numpy as np
import Operaciones
import math

class Suma(Operaciones):
    def operacion(self, vector):
        self.total = np.sum(vector)
        return self.total
