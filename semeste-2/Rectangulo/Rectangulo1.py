from Rectangulo import Rectangulo
class Rectangulo1(Rectangulo):
    def rotar(self):
        return Rectangulo1(self.y, self.x)
    def pintar(self, c):
        for i in range(self.y):
            print(c * self.x)
rectangulos = []
while True:
    ancho = int(input("Ancho? "))
    alto = int(input("Alto? "))
    if ancho == 0 and alto == 0:
        break
    r = Rectangulo(ancho, alto)
    rectangulos.append(r)
    r.dibujar("*")
mas_grande = None
area_maxima = 0
for r in rectangulos:
    area = r.x * r.y
    if area > area_maxima:
        area_maxima = area
        mas_grande = r
if mas_grande is not None:
    rotado = mas_grande.rotar()
    rotado.pintar("*")
