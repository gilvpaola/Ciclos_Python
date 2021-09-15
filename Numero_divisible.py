# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:04:07 2021

@author: USUARIO
"""

# Programa para determinar si un número entero es divisible por otro
# número entero

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

if a % b == 0:
    print(a, "es divisible por", b)
else:
    print(a, "no es divisible por", b)
print("Fin del programa")
    