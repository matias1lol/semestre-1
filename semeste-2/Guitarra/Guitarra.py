class Guitarra:
    def __init__(self):
        self.iCuerda = 0 
        self.iEspacio = 0  
    def setDedo(self, posCuerda, posEspacio):
        if type(posCuerda) == int and 1 <= posCuerda <= 6:
            if type(posEspacio) == int and 0 <= posEspacio <= 9:
                self.iCuerda = posCuerda
                self.iEspacio = posEspacio
                return True
        return False
    def getNota(self):
        notas = [
            ["Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si", "Do", "Reb"], # Cuerda 1
            ["Si", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab"], # Cuerda 2
            ["Sol", "Lab", "La", "Sib", "Si", "Do", "Reb", "Re", "Mib", "Mi"], # Cuerda 3
            ["Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"], # Cuerda 4
            ["La", "Sib", "Si", "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb"], # Cuerda 5
            ["Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si", "Do", "Reb"]  # Cuerda 6
        ]
        if self.iCuerda == 0 or self.iEspacio == 0:
            return "Ninguna"
        else:
            return notas[self.iCuerda - 1][self.iEspacio - 1]
