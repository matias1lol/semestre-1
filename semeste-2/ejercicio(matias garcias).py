# Problema 1: funcion para recibe un nro. tentero numero de tres digitos y 
# entrege el mismo nro. PERO invertido.
# Ej:invierte nuemero (365) entrega 563
def invierteNumero(numero):

    centenas = numero // 100
    decenas = (numero // 10) % 10
    unidades = numero % 10
    numero_invertido = unidades * 100 + decenas * 10 + centenas
    return numero_invertido
# Problema 2: conversión de grados Fahrenheit a Celsius
def fahrenheitACelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
# Problema 3: conversión de dolares a pesos
def dolarAPesos(dolares):
    valor_cambio = 20.0 
    pesos = dolares * valor_cambio
    return pesos
# Problema 4: calculo del área de un triángulo
def areaTriangulo(base, altura):
    area = 0.5 * base * altura
    return area
num = 563
print("numero invertido:", invierteNumero(num))
temp_fahrenheit = 98.6
print("temperatura en celsius:", fahrenheitACelsius(temp_fahrenheit))
dolares = 50
print("valor en pesos:", dolarAPesos(dolares))
base_triangulo = 10
altura_triangulo = 8
print("area del triángulo:", areaTriangulo(base_triangulo, altura_triangulo))
