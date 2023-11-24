class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    def saldo(self):
        return self.saldo
    def numero(self):
        return self.numero
    def __str__(self):
        return f"cuenta={self.numero}, saldo={self.saldo}"
    def compareTo(self, d):
        if self.saldo == d.saldo:
            return 0
        elif self.saldo < d.saldo:
            return -1
        else:
            return 1
    def depositar(self, monto):
        self.saldo += monto
    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False
class Cuenta1(Cuenta):
    def girar(self, monto):
        self.saldo -= monto
        return True
c = Cuenta("123", 1000)
print(c)

resultado = c.girar(2000)
print(resultado)
print(c)

c.depositar(500)
print(c)

resultado = c.girar(1000)
print(resultado)
print(c)

c1 = Cuenta1("456", 1000)
print(c1)

resultado = c1.girar(2000)
print(resultado)
print(c1)
