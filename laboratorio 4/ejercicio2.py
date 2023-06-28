a = [10, 80, 15, 30, 20]
b = [20, 45, 80, 20, 10]
c = [20, 35, 60, 90, 20]
# A
def funcion_valores():
    lista1 = set(a)
    lista2 = set(b)
    lista3 = set(c)
    comun = lista1.intersection(lista2, lista3)
    print(comun)
# B
def funcion_concatenar():
    concatenar = a + b + c
    print(concatenar)
# C
def determinar_valor():
    lista1 = set(a)
    lista2 = set(b)
    lista3 = set(c)
    comun = lista1 & lista2 & lista3
    print(comun)
# D
def ordenar_fun():
    descendente = [a, b, c]
    descendente.sort(reverse=True)
    print("Orden descendente:", descendente)
# E
def fun_remplazar():
    descendente1 = [a, b, c]
    descendente1.sort(reverse=False)
    descendente1[0] = [100]
    print(descendente1)

funcion_valores()
funcion_concatenar()
determinar_valor()
ordenar_fun()
fun_remplazar()
