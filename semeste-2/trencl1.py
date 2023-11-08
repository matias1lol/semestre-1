#Sin el uso de OO, programe el diálogo indicado en el siguiente ejemplo:
#Suma y mayor de fracciones a/b y c/d
# Solicitar los valores de a, b, c y d
print("Suma y mayor de fracciones a/b y c/d")
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))
d = int(input("d? "))
numerador_suma = a * d + c * b
denominador_suma = b * d
print("suma =", numerador_suma, "/", denominador_suma)
if a * d > c * b:
    print("mayor =", a, "/", b)
else:
    print("mayor =", c, "/", d)
