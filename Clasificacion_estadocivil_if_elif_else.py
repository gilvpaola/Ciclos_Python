# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:41:52 2021

@author: USUARIO
"""

nombre = input("Ingrese su nombre: ")
estado_civil = int(input(f"{nombre} ingrese su estado civil: "))

if estado_civil == 1:
    print(nombre, "es Soltero")
elif estado_civil == 2:
    print(nombre, "es Casado")
elif estado_civil == 3:
    print(nombre, "es Separado")
elif estado_civil == 4:
    print(nombre, "es Viudo")
elif estado_civil == 5:
    print(nombre, "esta en Unión libre")
else:
    print("Estado civil inválido")
    
