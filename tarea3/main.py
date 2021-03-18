from Animales.Gato import Gato
from Animales.Perro import Perro
from Animales.Iguana import Iguana
from Animales.Pato import Pato
from Animales.Patuco import Patuco

g = Gato("gato1", 1, 1)
p = Perro("dogi", 2, 2)
i = Iguana("canto", 3, 3)
g2 = Gato("nube", 1, 1)
pato = Pato("luz", 2, 2)
patuco = Patuco("patty", 2, 100)

veterinaria = [g, p, i, g2, pato, patuco]

suma = 0
for animal in veterinaria:
    print(animal)
    print("bañarme sale", animal.costoBaño())
    suma = suma + animal.cantidadPatas

print("la cantidad total de patas es", suma)
