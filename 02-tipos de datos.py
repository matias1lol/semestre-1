# datos de tipo numerico
edad = 18
peso = 96
estatura= 1.71
print(f"mi peso es de {peso}")
# operaciones aritmeticas basicas
imc = peso / (estatura**2)
print("Mi imc es de:",imc," \n")
print(type(imc))
print("Mi imc es de: {:.2f}".format(imc),"\n")
# datos de tipo cadena de caracteres
asignatura = "Programacion"
carrera = "Ingenieria civil en informatica"
print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)
print("la cantidad de caracteres de la palabra", asignatura, "es de",len(asignatura))
#valores booleanos
ampolleta = False
interruptor = True
print(ampolleta,interruptor)
print("la variable ampolleta es de tipo:",type(interruptor),"\n")
#podemos transformar cualquier valor a un booleano
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
#datos de tipo list
#inicializando lista de 2 maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia",nueva_lista)
print("esta es una lista vacia",otra_lista)
print(type(otra_lista))
#declarando tres listas diferentes
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]
#¿ Se puede realizar una lista de datos compuestos?
data = ["Osorno", {"UV": "nivel bajo", "Temp C": 15}, (-40.5725, -73.1323)]
listamixta = ["felipe",100, True]
print("lista de candena de caracteres:", estudiantes)
print("lista de numeros:",num)
print("lsita de elemento:", lenguaje)
print("esto igual es una lista mixta:", listamixta)
print(len(listamixta))
print(estudiantes.count("pepe"))
print(num.count(5000))
lenguaje = ["javascript"]
print("nuevo valor del arregla de un elemento",lenguaje)
print(estudiantes[0])
print(estudiantes[1])
print("posicion -2", estudiantes[-2])