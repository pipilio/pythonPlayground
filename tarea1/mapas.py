def creaHeroe(nombre, hitpoints, ataque, velocidad):
    heroe = {}
    heroe["nombre"] = nombre
    heroe["hp"] = hitpoints
    heroe["atk"] = ataque
    heroe["spd"] = velocidad
    return heroe

def calcularPuntajeHeroe(heroe):
    return  heroe.get("attack") * heroe.get("velocidad") + heroe.get("hp")

def encontrarMejorHeroe(listaHeroes):
    return listaHeroes[0]

heroe1 = creaHeroe("Link", 100, 20, 5)
heroe2 = creaHeroe("Samus", 150, 30, 2)
heroe3 = creaHeroe("Patuco", 1000, 1, 4)

misHeroes  = [ heroe1, heroe2, heroe3 ]

mejorHeroe = encontrarMejorHeroe(misHeroes)
print("el mejor heroe es...")
print(mejorHeroe)
