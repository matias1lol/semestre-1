print("###1-DECLARACIONES DE FUNCIONES###")
def mi_primera_funcion():
    print("Esta es mi primera función")

mi_primera_funcion()

print("###2-DECLARACIONES DE FUNCIONES###")
def concatenar(lista1, lista2):
    return lista1 + lista2

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(concatenar(lista1, lista2))

print("###3-DECLARACIONES DE FUNCIONES###")
def multiplicacion(num1, num2):
    return num1 * num2

print(multiplicacion(50, 50))

print("###4-DECLARACIONES DE FUNCIONES###")
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
