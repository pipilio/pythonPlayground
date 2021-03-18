from .Animal import Animal

class Bipedo(Animal):

    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.cantidadPatas = 2

    def costoBaño(self):
        return super().costoBaño() + 2 * self.peso