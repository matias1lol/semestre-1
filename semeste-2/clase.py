class Auto:  # Abstracción de los objetos autos
    def __init__(self, bencina):
        self.bencina = bencina
        print("Este auto tiene", bencina, "litros de bencina")

    def arrancar(self):
        if self.bencina > 0:
            return "Arranca"
        else:
            return "No arranca"

    def conducir(self):
        if self.bencina > 0:
            self.bencina -= 1
            return "Quedan", self.bencina, "litros"
        else:
            return "No se mueve"
auto_mio = Auto(3)      
print(auto_mio.bencina)
print(auto_mio.arrancar())
print(auto_mio.conducir())