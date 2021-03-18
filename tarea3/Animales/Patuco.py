from .Pato import Pato

class Patuco(Pato):
    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.tipo = "patuco"

    def __str__(self):
        return "disculpen a mi papa, es idiota"