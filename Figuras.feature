Feature: Calcular el área de una figura geometrica
  Como profesor de primaria
  deseo saber el área de una figura geometrica especifica
  para verificar los resultados de mis alumnos

  Scenario: Calcular área del circulo
    Dado que ingreso el radio de "2" Centímetros
    cuando realizo la operación
    entonces el área del círculo es de "12.5664" Centímetros

  Scenario: Calcular área del circulo
    Dado que ingreso el radio de "16" Centímetros
    cuando realizo la operación
    entonces el área del círculo es de "804.2496" Centímetros

  Scenario: Calcular área del trianguulo
    Dado que ingreso la base de "4" Centímetros y la altura de "4" Centímetros
    cuando realizo la operación
    entonces el área del triangulo es de "8" Centímetros

  Scenario: Calcular área del trianguulo
    Dado que ingreso la base de "12" Centímetros y la altura de "5" Centímetros
    cuando realizo la operación
    entonces el área del triangulo es de "30" Centímetros

  Scenario: Calcular área del cuadrado
    Dado que ingreso el lado de "5" Centímetros
    cuando realizo la operación
    entonces el área del cuadrado es de "25" Centímetros

  Scenario: Calcular área del cuadrado
    Dado que ingreso el lado de "10" Centímetros
    cuando realizo la operación
    entonces el área del cuadrado es de "100" Centímetros

  Scenario: Calcular área del trapecio
    Dado que ingreso la altura de "5" Centímetros, la base1 de "5" Centímetros y la base2 de "5" Centímetros
    cuando realizo la operación
    entonces el área del trapecio es de "25" Centímetros

  Scenario: Calcular área del trapecio
    Dado que ingreso la altura de "10" Centímetros, la base1 de "17" Centímetros y la base2 de "12" Centímetros
    cuando realizo la operación
    entonces el área del trapecio es de "140" Centímetros