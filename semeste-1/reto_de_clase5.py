numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
if numero > 1:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
else:
    print("El número no es primo.")
if numero > 50:
    print("El número es mayor a 50.")
elif numero < 50:
    print("El número es menor a 50.")
else:
    print("El número es igual a 50.")
