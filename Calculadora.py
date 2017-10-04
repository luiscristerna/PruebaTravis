# Luis Manuel Cristerna Gallegos 05/09/2017
# Implementando CI con travis
#prueba 3
import math


class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = num1 + num2
        except:
            self.resultado = "Datos Incorrectos"

    def resta(self, num1, num2):
        try:
            self.resultado = num1 - num2
        except:
            self.resultado = "Datos Incorrectos"

    def multiplicacion(self, num1, num2):
<<<<<<< HEAD
        self.resultado = num1 * num2
=======
        try:
            self.resultado = num1 * num2
        except:
            self.resultado = "Datos Incorrectos"
>>>>>>> b14a3e20acba4e119ddf9efe1b06cdd1783f5acc

    def division(self, num1, num2):
        try:
            if(num2 == 0):
                self.resultado = 'No se puede divir entre cero'
            else:
                self.resultado = num1 / num2
        except:
            self.resultado = 'Datos Incorrectos'

    def potencia(self, num1, num2):
        try:
            if(num2 == 0):
                self.resultado = 'Numero elevado a la potencia cero es uno'
            else:
                self.resultado = num1 ** num2
        except:
            self.resultado = 'Datos Incorrectos'

    def raiz(self, num1):
<<<<<<< HEAD
        if(num1 < 0):
            self.resultado = 'Error'
        else:
            self.resultado = math.sqrt(num1)

=======
        try:
            if(num1 < 0):
                self.resultado = 'Error'
            else:
                self.resultado = math.sqrt(num1)
        except:
            self.resultado = 'Datos incorrectos'
>>>>>>> b14a3e20acba4e119ddf9efe1b06cdd1783f5acc
