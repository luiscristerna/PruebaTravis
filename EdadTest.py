#Luis Manuel Cristerna Gallegos 05/09/2017
import unittest
from Edad import Edad

class EdadTest(unittest.TestCase):

	def setUp(self):
		self.edad = Edad()


	def test_obtener_edad_cero_igual_no_existes(self):
		self.edad.calcular_edad(0)
		self.assertEquals(self.edad.obtener_edad(), 'Ninguna, pues no existes')

	def test_obtener_edad_diez_igual_eres_nino(self):
		self.edad.calcular_edad(10)
		self.assertEquals(self.edad.obtener_edad(), 'Infancia')

	def test_obtener_edad_17_igual_eres_adolescente(self):
		self.edad.calcular_edad(17)
		self.assertEquals(self.edad.obtener_edad(), 'Adolescencia')

	def test_obtener_edad_32_igual_eres_adulto(self):
		self.edad.calcular_edad(32)
		self.assertEquals(self.edad.obtener_edad(), 'Adultez')

	def test_obtener_edad_70_igual_eres_adulto_mayor(self):
		self.edad.calcular_edad(70)
		self.assertEquals(self.edad.obtener_edad(), 'Ancianidad')
	
	def test_obtener_edad_120_igual_eres_mummra(self):
		self.edad.calcular_edad(120)
		self.assertEquals(self.edad.obtener_edad(), 'Vete al panteon, no gastes oxigeno')		
		
	def test_obtener_edad_muchos_igual_datos_incorrectos(self):
		self.edad.calcular_edad('L')
		self.assertEquals(self.edad.obtener_edad(), 'Datos Incorrectos')


if __name__ == '__main__':
	unittest.main()