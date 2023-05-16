nombres = ["Juan", "Ana", "Pedro", "María", "José"]
edades = [28, 35, 42, 23, 31]
trabajadores = {}
for i in range(len(nombres)):
    trabajadores[nombres[i]] = edades[i]
print(trabajadores)
