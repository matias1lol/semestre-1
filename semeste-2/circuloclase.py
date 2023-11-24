import math
class Circulo:
    def __init__(self, x):
        assert x > 0
        self.r = x
    def perimetro(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r ** 2
class Cuadrado:
    def __init__(self, x):
        assert x > 0
        self.a = x
    def perimetro(self):
        return 4 * self.a
    def area(self):
        return self.a ** 2
r = input("circulo o cuadrado?").lower()
if r == "circulo":
    c = Circulo(float(input("radio?")))
elif r == "cuadrado":
    c = Cuadrado(float(input("lado?")))
else:
    exit("debe ser circulo o cuadrado")
print("area=", c.area())
print("perimetro=", c.perimetro())
