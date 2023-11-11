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
lucario = Pokemon("lucario", "lucha", 1.2, 54.0, "m")
Charizard = Pokemon("Charizard", "fuego", 1.7, 90.5, "m")
lucario.setPS_base(5)
lucario.setAtaque(7)
lucario.setDefensa(5)
lucario.setVelocidad(6)
Charizard.setPS_base(5)
Charizard.setAtaque(5)
Charizard.setDefensa(5)
Charizard.setVelocidad(6)
print(lucario.esMejorQue(Charizard))
