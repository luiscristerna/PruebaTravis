Feature: Potencia de dos numeros
	Como usuario de la calculadora
	deseo realizar la potencia de dos numeros
	para obtener el resultado preciso

	Scenario: Potencia de 3 a la 3
		Dado la potencia del numero "3" a la "3"
		cuando realizo la operación
		entonces obtengo el resultado de la potencia que es "27"

    Scenario: Potencia de 10 a la 3
		Dado la potencia del numero "10" a la "3"
		cuando realizo la operación
		entonces obtengo el resultado de la potencia que es "1000"

    Scenario: Potencia de 65 a la 3
		Dado la potencia del numero "65" a la "3"
		cuando realizo la operación
		entonces obtengo el resultado de la potencia que es "274625"