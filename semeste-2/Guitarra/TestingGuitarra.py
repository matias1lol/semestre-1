from Guitarra import Guitarra

guit = Guitarra()
print(guit.getNota()) # Ninguna
print(guit.setDedo(1, 3)) # True
print(guit.getNota()) # Solb
print(guit.setDedo(2, 5)) # True
print(guit.getNota()) # Mib
print(guit.setDedo(3, 7)) # True
print(guit.getNota()) # Reb
print(guit.setDedo(4, 4)) # True
print(guit.getNota()) # Fa
print(guit.setDedo(5, 8)) # True
print(guit.getNota()) # Mi
print(guit.setDedo(6, 2)) # True
print(guit.getNota()) # Fa
print(guit.setDedo(0, 0)) # True
print(guit.getNota()) # Fa
print(guit.setDedo(7, 2)) # False
print(guit.getNota()) # Fa
print(guit.setDedo(3, 10)) # False
print(guit.getNota()) # Fa
print(guit.setDedo("a", 4)) # False
print(guit.getNota()) # Fa
print(guit.setDedo(2, "b")) # False
print(guit.getNota()) # Fa
