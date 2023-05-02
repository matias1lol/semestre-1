nombre = input("cual es tu nombre del estudiante:")
asignatura = input("cual es su asignatura:")
nota1 = float (input("inserte nota de laboratorio N1:"))
nota2 = float (input("inserte nota de laboratorio N2:"))
promedio = (nota1 * 0.3) +(nota2 *0.7)
dic = {
    "nombre_estudiante": nombre,
    "nombre_asignatura": asignatura,
    "nota_1": nota1,
    "nota_2": nota2,
    "promedio": round(promedio, 1)

}
print(dic)
