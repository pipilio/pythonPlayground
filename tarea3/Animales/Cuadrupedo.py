from .Animal import Animal

class Cuadrupedo(Animal):

    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.cantidadPatas = 4

    def costoBaño(self):
        return super().costoBaño() + 10 * self.peso
