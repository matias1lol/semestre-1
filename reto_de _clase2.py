nombres = []
pesos = []
estaturas = []
edades = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del paciente {i+1}: ")
    nombres.append(nombre)
    peso = float(input(f"Ingrese el peso del paciente {i+1} en kg: "))
    pesos.append(peso)
    estatura = float(input(f"Ingrese la estatura del paciente {i+1} en metros: "))
    estaturas.append(estatura)
    while True:
        try:
            edad = int(input(f"Ingrese la edad del paciente {i+1}: "))
            if edad < 0 or edad > 120:
                print("Error: la edad debe estar entre 0 y 120 años")
            else:
                edades.append(edad)
                break
        except ValueError:
            print("Error: la edad debe ser un número entero")
pacientes = []
for i in range(3):
    paciente = (nombres[i], pesos[i], estaturas[i], edades[i])
    pacientes.append(paciente)
for i, paciente in enumerate(pacientes):
    print(f"Paciente {i+1}:")
    print(f"Nombre: {paciente[0]}")
    print(f"Peso: {paciente[1]} kg")
    print(f"Estatura: {paciente[2]} m")
    print(f"Edad: {paciente[3]} años")
