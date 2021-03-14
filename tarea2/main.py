from Entidades.Animales import Gato, Perro, Iguana

i = Iguana("buzusima", 4, 12)
# ojo! Podemos imprimir directamente la instancia i
# de la clase Iguana pq esa clase tiene un metodo
# llamado __str__
print(i)
print("La iguana " + i.nombre + " dice")
print(i.hablar())
print("La edad humana de " + i.nombre + " es " + str(i.edadHumana()))

g = Gato("NekoPerkin", 2, 2)
print(g)
print("El gato " + g.nombre + " dice")
print(g.hablar())
print("La edad humana de " + g.nombre + " es " + str(g.edadHumana()))

p = Iguana("Rosina", 5, 5)
print(p)
print("El perro " + p.nombre + " dice")
print(p.hablar())
print("La edad humana de " + p.nombre + " es " + str(p.edadHumana()))

#TAREA: encontrar por que rosina no habla bien!!
#TAREA: implementar los metodos edadHumana para Perro e Iguana