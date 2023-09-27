# Aritméticas
a = 5
b = 2
print(a + b)  # Suma: 7
print(a - b)  # Resta: 3
print(a * b)  # Multiplicación: 10
print(a / b)  # División: 2.5
print(a // b)  # División entera: 2
print(a % b)  # Módulo: 1
print(a ** b)  # Potencia: 25

# Comparación
x = 10
y = 5
print(x == y)  # Igual a: False
print(x != y)  # Diferente de: True
print(x > y)  # Mayor que: True
print(x >= y)  # Mayor o igual que: True
print(x < y)  # Menor que: False
print(x <= y)  # Menor o igual que: False

# Lógicas
p = True
q = False
print(p and q)  # Y lógico: False
print(p or q)  # O lógico: True
print(not p)  # No lógico: False

# Bit a bit
m = 0b1010  # Representa el número binario 10 en Python
n = 0b1100  # Representa el número binario 12 en Python
print(bin(m & n))  # Y bit a bit: 0b1000
print(bin(m | n))  # O bit a bit: 0b1110
print(bin(m ^ n))  # Xor bit a bit: 0b0110
print(bin(m << 1))  # Desplazamiento a la izquierda: 0b10100
print(bin(n >> 2))  # Desplazamiento a la derecha: 0b0011

# Asignación
x = 5
x += 3  # Asignación con suma
print(x)  # 8

y = 10
y //= 3  # Asignación con división entera
print(y)  # 3

z = 7
z **= 2  # Asignación con potencia
print(z)  # 49
bencina = True
encendido = True
edad = 19
#utiliza el operador and
if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no avanza")

#utiliza el operador or
if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no avanza")  

#utiliza el operador NOT junto and   
if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no avanza")

#utiliza el operador NOT junto or
if not bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no avanza")

#utiliza el operador NOT junto or y and
if not bencina or (encendido and edad > 18 ):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no avanza")
      