#don sandro viaja frecuenteme desde susr a valdiavia.
#el camino entro el punto A el punto c tiene una distancia de 40 km, el trayecto de B a C de 25 km. y de A a B de 22 km.
#don sandro va a comprar un vehiculo y esta buscando que minimice sus costos en los trayectos de A a C de forma directa (AC) y de A a C pero pasando por B (ABC)
#para esto debe buscar un vehiculo de rendimiento (ej:15km/L)tal que logre este objetivo para cada uno de estos trayectos. dicho esto, se pide econtrar una relacion del costo en funcion del rendimiento y el precio de la bencina.

#1)use la receta de diseño de funciones para definirla funcion de nombre litro que calcule la cantidad la cantidad  de bencina en funcion de la distancia recorrido y el rendimiento del vehiculo.
#2)utilice la receta de diseño de funciones para definir la funcion de nombre costo_bencina que calcule el costo de la bencina en funcion su precio y litros llenados al estanque.
#3)revuelve el problema ultizando lo solicitado en a y b. no es necesrio que haya resuelto alguno de los apartados anteriores (a y/0 b).

#1) definicion de la funcion litros
def litros(distancia, rendimiento):
    return distancia / rendimiento

#2) definicion de la funcion costo_bencina
def costo_bencina(precio, litros):
    return precio * litros

# 3) responder el problema
def costo_viaje(distancia, rendimiento, precio_bencina):
    
    litros_necesarios = litros(distancia, rendimiento)

    costo = costo_bencina(precio_bencina, litros_necesarios)
    return costo

distancia_AC = 40  # km
distancia_ABC = 22 + 25  # km
rendimiento = 15  # km/L
precio_bencina = 1000  # precio por litro

costo_AC = costo_viaje(distancia_AC, rendimiento, precio_bencina)
costo_ABC = costo_viaje(distancia_ABC, rendimiento, precio_bencina)

print(f"El costo del viaje de A a C directamente es: ${costo_AC}")
print(f"El costo del viaje de A a C pasando por B es: ${costo_ABC}")
