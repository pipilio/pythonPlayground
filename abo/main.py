class Nodo():
    def __init__(self):
        self.valor = None
        self.izq = None
        self.der = None

    def insertar(self, valor):
        if self.valor is None:
            self.valor = valor
        elif valor > self.valor:
            #tirarlo para la derecha
            if self.der is None:
                self.der = Nodo()
            self.der.insertar(valor)
        else:
            #tirarlo para la izquiera
            if self.izq is None:
                self.izq = Nodo()
            self.izq.insertar(valor)

    def mostrarArbol(self):
        if self.valor is None:
            return
        print("valor", self.valor)
        if (self.izq is not None):
            print("izquierda de", self.valor)
            self.izq.mostrarArbol()
        if (self.der is not None):
            print("derecha de", self.valor)
            self.der.mostrarArbol()





abo = Nodo()
nums = [11, 0, 4, 12, 5, 9, 7, 1000]
for i in nums:
    abo.insertar(i)

abo.mostrarArbol()





