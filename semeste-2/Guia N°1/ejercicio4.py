impar = 1
cubo = 1
print(f"{impar}³ = {cubo}")
for i in range(2, 5):
    suma_impares = 0
    
    for j in range(i):
        suma_impares += impar
        impar += 2
    cubo += suma_impares ** 3 
    print(f"{suma_impares}³ = {cubo}")
