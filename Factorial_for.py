# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:52:02 2021

@author: USUARIO
"""

# Programa para calcular el factorial de un número n

n = int(input("Ingrese un número entero: "))
factorial = 1

# Forma correcta
for i in range(1, n+1, 1):
    factorial = factorial * i
print("El factorial de n con parámetros 1, n+1, 1 es:", factorial)

# Forma incorrecta
factorial = 1
for i in range(1, n, 1):
    factorial = factorial * i
print("El factorial de n con parámetros 1, n, 1 es:", factorial)

# Forma incorrecta = siempre da 0 porque i inicio en 0
factorial = 1
for i in range(n+1):
    factorial = factorial * i
print("El factorial de n con parámetro n+1 es:", factorial)
