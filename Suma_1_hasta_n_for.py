# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:41:18 2021

@author: USUARIO
"""

n = int(input("Ingrese un número entero: "))
suma = 0

# Forma correcta
for i in range(1, n+1, 1):
    suma = suma + i
print("La suma de los números enteros de 1 hasta n con parámetros 1, n+1, 1 es:", suma) 

# Forma incorrecta
suma = 0
for i in range(1, n, 1):
    suma = suma + i
print("La suma de los números enteros de 1 hasta n con parámetros 1, n, 1 es:", suma)

# Forma correcta
suma = 0
for i in range(n+1):
    suma = suma + i
print("La suma de los números enteros de 1 hasta n con el paramétro n+1 es:", suma)
