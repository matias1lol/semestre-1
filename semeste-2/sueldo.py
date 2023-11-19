def sueldo(horas):
 return 5000*horas
print("$",sueldo(40))
# areaTrianguloRectangulo: numero numero -> numero
# Calcula el area de triangulo rectangulo donde uno de
# sus lados es lado1 y el otro es lado2
def areaTrianguloRectangulo(lado1, lado2):
 return lado1 * lado2 / 2
assert areaTrianguloRectangulo(3, 4) == 6
print("el area es: ", areaTrianguloRectangulo(3,4))