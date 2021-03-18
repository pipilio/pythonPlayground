from .Cuadrupedo import Cuadrupedo

class Iguana(Cuadrupedo):
    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.tipo = "Iguana"

    def hablar(self):
        return "..."
    
    def edadHumana(self):
        # TAREA: implementar el metodo edad humana para la clase Iguana
        # vamos a asumir que cada anno de la iguana corresponde a 6 annos humanos
        return 0
