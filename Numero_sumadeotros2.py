# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:18:56 2021

@author: USUARIO
"""

# Programa para leer tres números enteros y determinar si el tercero
# es la suma de los dos primeros

a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
c = int(input("Ingrese el tercer número entero: "))

if a + b == c:
    print(c, "es la suma de", a, "con", b)
else:
    if a + c == b:
        print(b, "es la suma de", a, "con", c)
    else:
        if b + c == a:
            print(a, "es la suma de", b, "con", c)
        else:
            print(a,",", b, "y", c, "no cumplen la condición")
print("El programa finalizo")       
