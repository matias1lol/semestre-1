def estudiantes_en_comun():
    grupo1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
    grupo2 = {"Marcos", "Nicolás", "Diego", "Matias"}
    
    estudiantes_comunes = grupo1.intersection(grupo2)
    
    if len(estudiantes_comunes) > 0:
        print("Los siguientes estudiantes están en ambos grupos:")
        for estudiante in estudiantes_comunes:
            print(estudiante)
    else:
        print("No hay estudiantes en común entre los grupos.")
estudiantes_en_comun()
