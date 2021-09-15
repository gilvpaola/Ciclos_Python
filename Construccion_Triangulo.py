# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:40:08 2021

@author: USUARIO
"""

# Programa que permite ingresar tres números enteros y determina
# si con ellos se puede construir un triángulo o no

a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
c = int(input("Ingrese el tercer número entero: "))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print(a, b, "y", c, "pueden formar un triángulo")
        else:
            print(a, b, "y", c, "no pueden formar un triángulo")
            
print("Fin triángulo con tres if")

if a + b > c and a + c > b and b + c > a:
    print(a, b, "y", c, "pueden formar un triángulo")
else:
    print(a, b, "y", c, "no pueden formar un triángulo")

print("Fin if sencillo")
    