temperaturas_minimas = {9, 5, 2, 7, 6, 1}
temperaturas_maximas = {12, 14, 11, 10, 15, 9}
if 9 in temperaturas_minimas and 9 in temperaturas_maximas:
    print("La temperatura 9°C está en ambos sets.")
else:
    print("La temperatura 9°C no está en ambos sets.")
if 6 in temperaturas_minimas or 6 in temperaturas_maximas or 17 in temperaturas_minimas or 17 in temperaturas_maximas:
    print("temperaturas 6°C o 17°C está en alguno de los sets.")
else:
    print("Las temperaturas 6°C y 17°C no están en ninguno de los sets.")
temperaturas_minimas = {temp ** 4 for temp in temperaturas_minimas}
temperaturas_maximas = {temp ** 4 for temp in temperaturas_maximas}
print("Temperaturas mínimas es a 4:", temperaturas_minimas)
print("Temperaturas máximas es a 4:", temperaturas_maximas)
temperaturas_unidas = temperaturas_minimas.union(temperaturas_maximas)
print("Set unido de temperaturas:", temperaturas_unidas)
