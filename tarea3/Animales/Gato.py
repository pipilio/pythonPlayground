from .Cuadrupedo import Cuadrupedo

class Gato(Cuadrupedo):

    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.tipo = "gato"
        self.cantidadBigotes = 6

    def maullar(self):
        return "miau"

    def edadHumana(self):
        # el primer anno de un gato equivale a 15 annos humanos
        # el segundo anno equivale a 9 annos humanos
        # de ahi en adelante cada anno equivale a 4 annos humanos
        if self.edad == 1:
            return 15
        if self.edad == 2:
            return 24
        else:
            return 24 + self.edad * 4

    def costoBaño(self):
        return super().costoBaño() + 1000 * self.cantidadBigotes