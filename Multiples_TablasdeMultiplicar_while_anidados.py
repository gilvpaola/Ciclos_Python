# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:31:00 2021

@author: USUARIO
"""

# Programa para generar multiples tablas de multiplicar según n

n = int(input("Ingrese número entero: "))

x = 1

while x <= n:
    i = 1
    while i <= 10:
        r = x * i
        print(x, "*", i, "=", r)
        i = i + 1
    x = x + 1
    print("")