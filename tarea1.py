# esta función debe contar la cantidad de vocales que tiene palabra
def cuentaVocales(palabra):
    loweredPalabra = palabra.lower
    vocales = 0
    for i in range(0, len(loweredPalabra)):
        if esVocal(loweredPalabra[i]) == True:
            vocales = vocales + 1
    return vocales

def esVocal(letra):
    return "aeiou".find(letra) != -1

Palabras = cuentaVocales("paralelepipedo")
print(Palabras)