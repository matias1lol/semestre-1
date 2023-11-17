# ATRIBUTOS:
# dia: int
# mes: int
# anio: int

class Fecha:

	def __init__(self, x):
		(dia,mes,anio)=x.split("/")
		(self.dia,self.mes,self.anio)=(int(dia), int(mes), int(anio))

	def __str__(self):
			return str(self.dia)+"/"+str(self.mes)+"/"+str(self.anio)


	def __sub__(self,x):
		pass

	def siguiente(self):
		nueva = Fecha(str(self))
		nueva.dia += 1
		if nueva.dia > Fecha.dias_mes(nueva.mes, nueva.anio):
			nueva.dia = 1
			nueva.mes += 1
			if nueva.mes > 12:
				nueva.mes = 1
				nueva.anio += 1
		return nueva

	@staticmethod
	def dias_mes(mes, anio):
		dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if mes == 2 and Fecha.bisiesto(anio):
			return 29
		return dias[mes - 1]

	@staticmethod
	def bisiesto(anio):
		return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
	
f = Fecha("01/05/2013")
print(f)
g = f.siguiente()
print(g)
