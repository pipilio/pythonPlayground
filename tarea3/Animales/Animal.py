class Animal():

    def __init__(self, nombre, peso, edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.tipo = ""
        self.cantidadPatas = 0

    def __str__(self):
        return "Hola, soy " + self.nombre + " el " + self.tipo + ". Tengo " + str(self.edad) + " annos y peso " + str(self.peso) + " kilos."

    def temperatura(self):
        return self.peso * 2

    def costoBaño(self):
        return 100

