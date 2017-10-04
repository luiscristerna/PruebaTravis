# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora
from Edad import Edad
from Figuras import Figuras

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

#Suma
@step(u'Dado que sumo los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Resta
@step(u'Dado que resto los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))
@step(u'entonces obtengo el resultado de la resta que es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Multiplicacion
@step(u'Dado que multiplico los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicaion(int(num1), int(num2))
@step(u'entonces obtengo el resultado de la multiplicacion que es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Division
@step(u'Dado que divido los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))
@step(u'entonces obtengo el resultado de la division que es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Potencia
@step(u'Dado la potencia del numero "([^"]*)" a la "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))
@step(u'entonces obtengo el resultado de la potencia que es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.cal.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Potencia
@step(u'Dado el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(int(num1))
@step(u'entonces obtengo el resultado de la raiz que es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.cal.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Edades
@step(u'Dado que ingreso la edad de "([^"]*)" años')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.ed = Edad()
    world.ed.calcular_edad(int(num1))
@step(u'entonces su etapa de vida es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.ed.obtener_edad()
	assert esperado == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Figuras

#Circulo
@step(u'Dado que ingreso el radio de "([^"]*)" Centímetros')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.fig = Figuras()
    world.fig.obtener_area_circulo(int(num1))
@step(u'entonces el área del círculo es de "([^"]*)" Centímetros')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.fig.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Triangulo
@step(u'Dado que ingreso la base de "([^"]*)" Centímetros y la altura de "([^"]*)" Centímetros')
def dado_que_ingreso_el_numero_group1_group2(step, num1, num2):
    world.fig = Figuras()
    world.fig.obtener_area_triangulo(int(num1),int(num2))
@step(u'entonces el área del triangulo es de "([^"]*)" Centímetros')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.fig.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Cuadrado
@step(u'Dado que ingreso el lado de "([^"]*)" Centímetros')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.fig = Figuras()
    world.fig.obtener_area_cuadrado(int(num1))
@step(u'entonces el área del cuadrado es de "([^"]*)" Centímetros')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.fig.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Trapecio
@step(u'Dado que ingreso la altura de "([^"]*)" Centímetros, la base1 de "([^"]*)" Centímetros y la base2 de "([^"]*)" Centímetros')
def dado_que_ingreso_el_numero_group1_group2_group3(step, num1, num2, num3):
    world.fig = Figuras()
    world.fig.obtener_area_trapecio(int(num1),int(num2),int(num3))
@step(u'entonces el área del trapecio es de "([^"]*)" Centímetros')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = float(world.fig.obtener_resultado())
	assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)
