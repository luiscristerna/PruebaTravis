#Luis Manuel Cristerna Gallegos 05/09/2017
import unittest
from Calculadora import Calculadora
#P


class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()
	
	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(), 0)

	#Suma

	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 4)

	def test_sumar_3_mas_3_igual_6(self):
		self.calc.suma(3,3)
		self.assertEquals(self.calc.obtener_resultado(), 6)

	def test_sumar_menosuno_mas_uno_igual_uno(self):
		self.calc.suma(-1,2)
		self.assertEquals(self.calc.obtener_resultado(), 1)

	def test_suma_letraL_mas_2_igual_datosIncorrectos(self):
		self.calc.suma('l',2)
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	#Resta

	def test_restar_dos_menos_dos_igual_cero(self):
		self.calc.resta(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_restar_menostres_menos_dos_igual_menosuno(self):
		self.calc.resta(-3,2)
		self.assertEquals(self.calc.obtener_resultado(), -5)

	def test_restar_menosuno_menos_uno_igual_cero(self):
		self.calc.resta(-1,1)
		self.assertEquals(self.calc.obtener_resultado(), -2)

	def test_restar_letraL_menos_dos_igual_datosIncorrectos(self):
		self.calc.resta('l',2)
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')


	#Multiplicacion

	def test_multiplicar_dos_por_dos_igual_cuatro(self):
		self.calc.multiplicacion(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 4)	

	def test_multiplicar_cero_por_uno_igual_cero(self):
		self.calc.multiplicacion(0,1)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_multiplicar_menosuno_por_menosuno_igual_uno(self):
		self.calc.multiplicacion(-1,-1)
		self.assertEquals(self.calc.obtener_resultado(), 1)

		
	def test_multiplicar_letraA_por_dos_igual_dobleA(self):
		self.calc.multiplicacion('A',2)
		self.assertEquals(self.calc.obtener_resultado(), 'AA')

	#Division

	def test_dividir_dos_entre_dos_igual_uno(self):
		self.calc.division(2,2)
		self.assertEquals(self.calc.obtener_resultado(), 1)

	def test_dividir_cero_entre_uno_igual_cero(self):
		self.calc.division(0,1)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_dividir_uno_entre_cero_igual_nosentrecero(self):
		self.calc.division(1,0)
		self.assertEquals(self.calc.obtener_resultado(), 'No se puede divir entre cero')

	def test_dividir_letraL_entre_dos_igual_datosincorrectos(self):
		self.calc.division('L',2)
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')


	#Potencia

	def test_elevar_potencia_tres_a_tres_igual_27(self):
		self.calc.potencia(3,3)
		self.assertEquals(self.calc.obtener_resultado(), 27)	

	def test_elevar_potencia_dos_a_cero_igual_uno(self):
		self.calc.potencia(2,0)
		self.assertEquals(self.calc.obtener_resultado(), 'Numero elevado a la potencia cero es uno')

	def test_elevar_potencia_letraA_a_dos_igual_datosincorrectos(self):
		self.calc.potencia('A',2)
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')	

	def test_elevar_potencia_ocho_a_ocho_igual_unmillonseis(self):
		self.calc.potencia(8,8)
		self.assertEquals(self.calc.obtener_resultado(), 16777216)

	#Raiz

	def test_obtener_raiz_cuadrada_dos_igual_unopuntocuatro(self):
		self.calc.raiz(2)
		self.assertEquals(self.calc.obtener_resultado(), 1.4142135623730951)

	def test_obtener_raiz_cuadrada_menosuno_igual_nosepuede(self):
		self.calc.raiz(-1)
		self.assertEquals(self.calc.obtener_resultado(), 'Error')



if __name__ == '__main__': # pragma: no cover
	unittest.main()