Feature: Raiz de un numero
	Como usuario de la calculadora
	deseo realizar la raiz de un numero
	para obtener el resultado preciso

    Scenario: Raiz de 1
		Dado el numero "1"
		cuando realizo la operación
		entonces obtengo el resultado de la raiz que es "1"

    Scenario: Raiz de 4
		Dado el numero "4"
		cuando realizo la operación
		entonces obtengo el resultado de la raiz que es "2"

    Scenario: Raiz de 9
		Dado el numero "9"
		cuando realizo la operación
		entonces obtengo el resultado de la raiz que es "3"
