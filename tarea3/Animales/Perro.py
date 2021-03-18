from .Cuadrupedo import Cuadrupedo

class Perro(Cuadrupedo):
    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.tipo = "perro"

    def ladrar(self):
        return "guau"

    def hablar(self):
        return "guau"

    def edadHumana(self):
        # TAREA: implementar el metodo edad humana para la clase Perro
        return 0