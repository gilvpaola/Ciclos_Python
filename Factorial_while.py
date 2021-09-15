# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:32:04 2021

@author: USUARIO
"""

n = int(input("Ingrese un valor entero: "))
factorial = 1
i = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print("El factorial de", n, "es", factorial)
