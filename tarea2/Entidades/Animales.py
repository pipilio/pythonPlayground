class Gato:

    def __init__(self, nombre, peso, edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

    def __str__(self):
        return "Hola, soy " + self.nombre + " el gato. Tengo " + str(self.edad) + " annos y peso " + str(self.peso) + " kilos."

    def hablar(self):
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

class Perro:
    def __init__(self, nombre, peso, edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

    def __str__(self):
        return "Hola, soy " + self.nombre + " el perruchito. Tengo " + str(self.edad) + " annos y peso " + str(self.peso) + " kilos."
    
    def hablar(self):
        return "guau"

    def edadHumana(self):
        # TAREA: implementar el metodo edad humana para la clase Perro
        return 0

class Iguana:
    def __init__(self, nombre, peso, edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

    def __str__(self):
        return "Hola, soy " + self.nombre + " la iguana. Tengo " + str(self.edad) + " annos y peso " + str(self.peso) + " kilos."

    def hablar(self):
        return "..."
    
    def edadHumana(self):
        # TAREA: implementar el metodo edad humana para la clase Iguana
        # vamos a asumir que cada anno de la iguana corresponde a 6 annos humanos
        return 0
