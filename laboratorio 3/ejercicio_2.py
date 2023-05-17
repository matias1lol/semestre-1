a = [21, 8, 15, 3, 12]
b = [10, 9, 12, 15, 18]
c = [2, 3, 8, 9, 12]
concatenada = a + b + c
print("lista concatenada:", concatenada)
concatenada.insert(-1, 20)
print("lista con el número 20:", concatenada)
concatenada.sort(reverse=True)
print("lista ordenada de forma descendente:", concatenada)
concatenada.append([4, 5, 6])
print("lista con la lista [4, 5, 6] insertada:", concatenada)
suma_total = (concatenada)
print("suma total de los números:", suma_total)
promedio = suma_total / len(concatenada)
print("promedio de la lista:", promedio)
