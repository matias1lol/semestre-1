def obtener_palabras(frase):
    palabras = frase.split()
    longitud_palabras = {}
    for palabra in palabras:
        longitud_palabras[palabra] = len(palabra)
    return longitud_palabras
frase = input("Ingresa una frase: ")
resultado = obtener_palabras(frase)
print(resultado)
print(type(resultado))
