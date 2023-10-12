import circulo

radio = float(input("Introduce el radio del círculo: "))
area = circulo.area(radio)
perimetro = circulo.perimetro(radio)

print(f"El área del círculo es {area:.2f}")
print(f"El perímetro del círculo es {perimetro:.2f}")