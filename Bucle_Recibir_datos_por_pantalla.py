# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:35:32 2021

@author: USUARIO
"""

nombre = input("Ingrese un nombre: ")
while nombre != "":
    salario = int(input(f"{nombre} ingrese salario: "))
    aumento = 0.
    if salario < 1000:
        aumento = salario * 0.1
    nuevo_salario = salario + aumento
    print("Nombre", nombre, "\tsalario", salario, "\tAumento\t", aumento, "\tSalario nuevo\t", nuevo_salario)
    nombre = input("Ingrese un nombre: ")
    
print("Termine")