# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:12:38 2021

@author: USUARIO
"""

x = int(input("Ingrese un número entero: "))

if x % 2 == 0:
    print(x, "NO es primo, es número par")
    exit(0) #Termina ejecución del programa, no ejecuta más
i = 2
for i in range(3, int(x**(.5)) + 1,2):
    if x % i == 0:
        print("x, NO es primo, es divisible por", i)
        break
if x % i != 0:
    print(x, "Es primo")