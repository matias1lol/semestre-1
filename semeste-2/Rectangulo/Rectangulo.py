class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __gt__(self, otro):
        if self.x * self.y == otro.x * otro.y:
            return 0
        elif self.x * self.y > otro.x * otro.y:
            return 1
        else:
            return -1
    def dibujar(self, c):
        print(c * self.x)
        for i in range(self.y - 2):
            print(c + " " * (self.x - 2) + c)
        print(c * self.x)

