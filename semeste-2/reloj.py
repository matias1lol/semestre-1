class ParDeNumeros:
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0
    def getValor(self):
        return self.valor
    def setValor(self, nuevoValor):
        if(nuevoValor >= 0) and (nuevoValor < self.limite):
            self.valor = nuevoValor
    def toString(self):
        if self.valor < 10:
            return "0" + str(self.valor)
        else:
            return str(self.valor)
    def aumentar(self):
        self.valor = (self.valor + 1) % self.limite
class Reloj:
    def __init__(self, horas=0, minutos=0):
        self.horas = ParDeNumeros(24)
        self.minutos = ParDeNumeros(60)
        self.setReloj(horas, minutos)
    def tic(self):
        self.minutos.aumentar()
        if self.minutos.getValor() == 0:
            self.horas.aumentar()
        self.actualizarPantalla()
    def setReloj(self, hora, minuto):
        self.horas.setValor(hora)
        self.minutos.setValor(minuto)
        self.actualizarPantalla()
    def getHora(self):
        return self.pantalla
    def actualizarPantalla(self):
        self.pantalla = self.horas.toString() + ":" + self.minutos.toString()
class TestReloj:
    def __init__(self):
        self.reloj = Reloj(12, 30)
    def test_tic(self):
        print("Hora antes de tic: ", self.reloj.getHora())
        self.reloj.tic()
        print("Hora después de tic: ", self.reloj.getHora())
    def test_setReloj(self):
        print("Hora antes de setReloj: ", self.reloj.getHora())
        self.reloj.setReloj(10, 45)
        print("Hora después de setReloj: ", self.reloj.getHora())
test = TestReloj()
test.test_tic()
test.test_setReloj()
