Feature: Division de dos numeros
	Como usuario de la calculadora
	deseo realizar la division de dos numeros
	para obtener el resultado preciso

	Scenario: Division de 2 entre 2
		Dado que divido los numeros "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado de la division que es "1"

	Scenario: Division de 0 entre 9
		Dado que divido los numeros "0" y "9"
		cuando realizo la operación
	    entonces obtengo el resultado de la division que es "0"

    Scenario: Division de 9 entre 3
		Dado que divido los numeros "9" y "3"
		cuando realizo la operación
		entonces obtengo el resultado de la division que es "3"