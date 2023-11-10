#Hecho Por Matias Garcia Gonzalez y Jeremias Maichil 
class Pokemon:
    def __init__(self, nombre, tipo, altura, peso, sexo):
        self.nombre = nombre
        self.tipo = tipo
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
        self.ps_base = 0
        self.ataque = 0
        self.defensa = 0
        self.velocidad = 0
    def setPS_base(self, ps_base):
        self.ps_base = ps_base
    def setAtaque(self, ataque):
        self.ataque = ataque
    def setDefensa(self, defensa):
        self.defensa = defensa
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    def esMejorQue(self, otro_pokemon):
        promedio_self = (self.ps_base + self.ataque + self.defensa + self.velocidad) / 4
        promedio_otro = (otro_pokemon.ps_base + otro_pokemon.ataque + otro_pokemon.defensa + otro_pokemon.velocidad) / 4
        return promedio_self > promedio_otro
pika = Pokemon("Pikachu", "eléctrico", 0.4, 6.0, "h")
charma = Pokemon("Charmander", "fuego", 0.6, 8.5, "m")
pika.setPS_base(3)
pika.setAtaque(13)
pika.setDefensa(10)
pika.setVelocidad(15)
print(pika.esMejorQue(charma))
