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
    return  heroe.get("atk") * heroe.get("spd") + str(heroe.get("hp"))


def encontrarMejorHeroe(listaHeroes):
    for heroe in listaHeroes:
        print( heroe.get("nombre"), calcularPuntajeHeroe(heroe) )

heroe1 = creaHeroe("Link", 100, '20', 5)
heroe2 = creaHeroe("Samus", 150, '30', 2)
heroe3 = creaHeroe("Patuco", 1000, '1', 4)

misHeroes  = [ heroe1, heroe2, heroe3 ]

mejorHeroe = encontrarMejorHeroe(misHeroes)
print("el mejor heroe es...")
print(mejorHeroe)
