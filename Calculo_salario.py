# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:35:32 2021

@author: USUARIO
"""

tsa = 0
tau = 0
tns = 0
contador = 0
contAu = 0
nombre = input("Ingrese nombre: ")
while nombre != "":
    salario = int(input(f"{nombre} ingrese salario: "))
    tsa = tsa + salario
    contador = contador + 1
    aumento = 0
    if salario < 1000:
        aumento = salario * 0.1
        tau = tau + aumento
        contAu = contAu + 1
    nuevo_salario = salario + aumento
    tns = tns + nuevo_salario
    print("Nombre", nombre, "\tsalario", salario, "\tAumento\t", aumento, "\tNuevo salario\t", nuevo_salario)
    nombre = input("Ingrese nombre: ")
psa = tsa / contador
pau = tau / contador
pns = tns / contador
print("Total empleados", contador, "\tTotal con aumento > cero", contAu)
print("Total salarios anteriores\t", tsa, "\tPromedio\t", psa)
print("Total aumentos           \t", tau, "\tPromedio\t", pau)
print("Total nuevos salarios    \t", tns, "\tPromedio\t", pns)


    