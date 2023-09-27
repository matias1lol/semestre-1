def calcular_promedio_ponderado():
    lab1 = float(input("Ingrese la nota del Laboratorio 1: "))
    lab2 = float(input("Ingrese la nota del Laboratorio 2: "))
    lab3 = float(input("Ingrese la nota del Laboratorio 3: "))
    
    promedio_ponderado = lab1 * 0.3 + lab2 * 0.4 + lab3 * 0.3
    
    if promedio_ponderado < 4.0:
        print("El estudiante reprobó la asignatura.")
    elif promedio_ponderado >= 6.0:
        print("El estudiante aprobó la asignatura con distinción.")
    else:
        print("El estudiante aprobó la asignatura.")
calcular_promedio_ponderado()
