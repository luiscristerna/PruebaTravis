Feature: Calcular etapa de la vida de una persona
    Como usuario del sistema
    deseo saber en que etapa de la vida esta una persona
    para saber que personas utilizan mi aplicación

  Scenario: Calcular edad de 0 años
    Dado que ingreso la edad de "0" años
    cuando realizo la operación
    entonces su etapa de vida es "Ninguna, pues no existes"

  Scenario: Calcular edad de 8 años
    Dado que ingreso la edad de "8" años
    cuando realizo la operación
    entonces su etapa de vida es "Infancia"

  Scenario: Calcular edad de 17 años
    Dado que ingreso la edad de "17" años
    cuando realizo la operación
    entonces su etapa de vida es "Adolescencia"

  Scenario: Calcular edad de 34 años
    Dado que ingreso la edad de "34" años
    cuando realizo la operación
    entonces su etapa de vida es "Adultez"

  Scenario: Calcular edad de 80 años
    Dado que ingreso la edad de "80" años
    cuando realizo la operación
    entonces su etapa de vida es "Ancianidad"

  Scenario: Calcular edad de 140 años
    Dado que ingreso la edad de "140" años
    cuando realizo la operación
    entonces su etapa de vida es "Vete al panteon, no gastes oxigeno"


