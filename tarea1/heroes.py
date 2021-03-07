def creaHeroe(nombre, hitpoints, ataque, velocidad):
    #crea un heroe
    heroe = {}
    heroe["nombre"] = nombre
    heroe["hp"] = hitpoints
    heroe["atk"] = ataque
    heroe["spd"] = velocidad
    return heroe

def calcularPuntajeHeroe(heroe):
    # calcula el puntaje de un heroe
    return  heroe.get("attack") * heroe.get("velocidad") + heroe.get("hp")

def encontrarMejorHeroe(listaHeroes):
    # se debe buscar entre todos los heroes de la lista
    # cual es el que tiene el mayor puntaje y retornarlo
    # por ahora solo se esta entregando el 1er heroe
    # pero eso debe ser reemplazado por la implementacion suya
    return listaHeroes[0]

heroe1 = creaHeroe("Link", 100, 20, 5)
heroe2 = creaHeroe("Samus", 150, 30, 2)
heroe3 = creaHeroe("Patuco", 1000, 1, 4)

misHeroes  = [ heroe1, heroe2, heroe3 ]

mejorHeroe = encontrarMejorHeroe(misHeroes)
print("el mejor heroe es...")
print(mejorHeroe)
