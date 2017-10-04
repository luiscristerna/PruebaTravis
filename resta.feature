Feature: Resta de dos numeros
	Como usuario de la calculadora
	deseo realizar la resta de dos numeros
	para obtener el resultado preciso

	Scenario: Resta de 2 menos 2
		Dado que resto los numeros "2" y "2"
		cuando realizo la operación
		entonces obtengo el resultado de la resta que es "0"

	Scenario: Resta de 7 menos 5
		Dado que resto los numeros "7" y "5"
		cuando realizo la operación
		entonces obtengo el resultado de la resta que es "2"

	Scenario: Resta de 1000 menos 100
		Dado que resto los numeros "1000" y "100"
		cuando realizo la operación
		entonces obtengo el resultado de la resta que es "900"