def encontrar_menor_mayor():
    numeros = []
    for i in range(3):
        while True:
            try:
                numero = int(input("Ingrese un número entero: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: ¡Debe ingresar un número entero!")
    
    menor = min(numeros)
    mayor = max(numeros)
    
    print("El número menor es:", menor)
    print("El número mayor es:", mayor)
encontrar_menor_mayor()
