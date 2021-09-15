# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:22:06 2021

@author: USUARIO
"""

# Programa que permite a través de un número entero determinar la sumatoria hasta ese valor


n = int(input("Ingrese un valor entero: "))
suma = 0
i = 1

while i <= n:
    suma = suma + i
    i = i + 1
print("La suma de los enteros desde 1 hasta", n, "es", suma)