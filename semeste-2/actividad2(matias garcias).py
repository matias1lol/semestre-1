#frame:areaheron:(3 parametro)
#dec
#Ej:areaHeron(6,8,10) entrega 24
def areaHeron(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
print(areaHeron(6,8,10))
#areaHerobn debe respestar el nombre de las funciones de las enuadecuando
#ejemplo: areaheron(3,4,5) entrega 6
#se consistes entre el codigo y el proposito y el eje

