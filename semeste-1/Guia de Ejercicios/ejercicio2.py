def comparar_palabras():
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    
    if len(palabra1) > len(palabra2):
        print("La palabra", palabra1, "tiene más caracteres que", palabra2)
        print("La palabra", palabra2, "tiene menos caracteres que", palabra1)
    elif len(palabra2) > len(palabra1):
        print("La palabra", palabra2, "tiene más caracteres que", palabra1)
        print("La palabra", palabra1, "tiene menos caracteres que", palabra2)
    else:
        print("Ambas palabras tienen la misma cantidad de caracteres.")
comparar_palabras()
