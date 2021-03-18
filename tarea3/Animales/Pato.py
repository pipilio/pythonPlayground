from .Bipedo import Bipedo

class Pato(Bipedo):
    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        self.tipo = "pato"

    def __str__(self):
        return "cuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuaccuac"

    def hablar(self):
        return "cueck"
    
    def edadHumana(self):
        # TAREA: implementar el metodo edad humana para la clase Iguana
        # vamos a asumir que cada anno de la iguana corresponde a 6 annos humanos
        return 0
