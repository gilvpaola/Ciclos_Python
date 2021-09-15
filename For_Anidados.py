# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:25:11 2021

@author: USUARIO
"""

# Programa para generar secuencias con ciclo anidados

n = int(input("Ingrese un número entero: "))

for i in range(1, n+1):
    for j in range (1, i+1):
        print(i, end="")
    print("")
print("")

for i in range(1, n+1):
    for j in range (1, i+1):
        print(j, end="")
    print("")
print("")

# Genera que se impriman inversamente

for i in range(n, 0, -1):
    for j in range (1, i+1):
        print(i, end="")
    print("")
print("")

for i in range(n, 0, -1):
    for j in range (i, 0, -1):
        print(j, end="")
    print("")
print("")