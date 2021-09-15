# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:05:41 2021

@author: USUARIO
"""

# Programa para mostrar todos los primos desde 3 hasta un entero n

n = int(input("Ingrese número entero: "))

x = 3
while x <= n:
    i = 2
    while i <= x**(.5) and x % i != 0:
        i += 1
    if i > x**(.5):
        print(x, "es primo")
    x = x + 2