# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:00:18 2021

@author: USUARIO
"""

# Programa para determinar si un número es primo o no
# Número primo = Divisible por si mismo y la unidad

x = int(input("Ingrese número entero: "))
i = 2
while i <= x**(.5) and x % i != 0:
    i += 1
if i > x**(.5):
    print(x,"es primo")
else:
    print(x, "NO es primo, es divisible por", i)