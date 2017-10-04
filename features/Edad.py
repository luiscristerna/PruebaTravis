#Luis Manuel Cristerna Gallegos 05/09/2017
class Edad():

	def __init__(self):
		self.edad = 0

	def obtener_edad(self):
		return self.edad

	def calcular_edad(self, num1):
		try:
			if(num1 < 1):
				self.edad = 'Ninguna, pues no existes'
			elif(num1 > 0 and num1 < 13):
			 	self.edad = 'Infancia'
			elif(num1 > 12 and num1 < 18):
				self.edad = 'Adolescencia'
			elif(num1 > 17 and num1 < 65):
				self.edad = 'Adultez'
			elif(num1 > 65 and num1 < 119):
				self.edad = 'Ancianidad'
			elif(num1 > 119 and num1 < 200):
				self.edad = 'Vete al panteon, no gastes oxigeno'
			else:
				self.edad = 'Datos Incorrectos'
		except:
				self.edad = 'Datos Incorrectos'