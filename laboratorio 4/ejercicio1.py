trabajadores = [["juan",[7000000, 650000]],["maria",[681000, 710000, 590000]],["pedro",[590000, 635000, 705000]]]
def calcular_sueldo(lista_sueldos):
    total_sueldos = sum(lista_sueldos)
    promedio = total_sueldos / len(lista_sueldos)
    return round(promedio, 2)
def sueldo_mas_alto(lista_sueldos):
    sueldo_maximo = max(lista_sueldos)
    return sueldo_maximo
def impuestos(sueldo):
    retencion = sueldo * 0.1225
    return retencion
for trabajador in trabajadores:
    nombre = trabajador[0]
    sueldos = trabajador[1]

    promedio = calcular_sueldo(sueldos)
    sueldo_maximo = sueldo_mas_alto(sueldos)

    print(f"Promedio de sueldo de {nombre}: {promedio}")
    print(f"Sueldo más alto de {nombre}: {sueldo_maximo}")
