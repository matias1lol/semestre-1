import statistics

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
numeros.pop()
numeros.insert(0, 2)
numeros = list(set(numeros))
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
print("Lista después de eliminar el último elemento:", numeros)
print("Media de la lista:", media)
print("Mediana de la lista:", mediana)
