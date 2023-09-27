#Determinar si una palabra ingresada por teclado es una palíndromo. 
palabra = input("Ingrese una palabra: ")
if palabra == palabra[::-1]:
    print("es un palíndromo")
else:
    print("no es un palíndromo")
