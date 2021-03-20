# Un taller de reparación de dispositivos moviles
# necesita un programa para manejar su inventario
# cuando un dispositivo ingresa a la tienda se debe registrar
# el nombre del dueño, su teléfono y la fecha en que se ingresó.
# además de esto se debe registrar si el dispositivo viene con la pantalla rota (sí o no)
# se reciben dos tipos de dispositivos: iOS y Android.
# los dispositivos iOS se dividen en iphones e ipads
# los dispositivos Android se dividen en celulares y tablets
# para esta tarea los iphones tendrán pantallas de 6 pulgadas, los ipads de 12
# en cambio en android los celulares tendrán pantallas de 7 pulgadas y los tablets de 10
# el costo de reparación de los dispositivos es de $15.000
# si viene con la pantalla quebrada se agregarán $1.000 pesos por cada pulgada de la pantalla
# como bien saben, en apple son unos ladrones desalmados, así es que todo dispositivos iOS
# tiene un recargo de 50% en su reparación

# Ejemplo1: costo de reparación de un celular android con pantalla rota será
# Base: $15.000
# Pantalla: 7 pulgadas * $1.000 = $7.000
# total: $22.000

# Ejemplo2: costo de reparación de un ipad con pantalla rota será
# Base: $15.000
# Pantalla: 12 pulgadas * $1000 = $12.000
# total (sin recargo apple): $27.000
# total: $27.000 + 13.500 = $40.500 (eso te pasa por cuico)

from .TallerMovil import TallerMovil

t = TallerMovil()