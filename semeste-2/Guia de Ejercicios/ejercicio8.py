def determinar_estacion():
    mes = input("Ingrese un mes (en minúsculas): ")
    
    if mes == "diciembre" or mes == "enero" or mes == "febrero":
        estacion = "verano"
    elif mes == "marzo" or mes == "abril" or mes == "mayo":
        estacion = "otoño"
    elif mes == "junio" or mes == "julio" or mes == "agosto":
        estacion = "invierno"
    elif mes == "septiembre" or mes == "octubre" or mes == "noviembre":
        estacion = "primavera"
    else:
        estacion = "mes no válido"
    
    print("La estación correspondiente al mes", mes, "es:", estacion)
determinar_estacion()
