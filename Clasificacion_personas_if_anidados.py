# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:42:39 2021

@author: USUARIO
"""

nombre = input("Ingrese el nombre: ")
genero = int(input("Ingrese el género, 0 para mujer 1 para hombre "))
estatura = int(input("Ingrese estatura: "))
peso = int(input("Ingrese el peso: "))

if estatura > 180:
    if peso > 70:
        if genero == 0:
            print("Reina de belleza")
        else:
            print("Cantautor")
    else:
        print("Árbitro de fútbol")
else:
    print("Jugador de parqués")
    
print("Sujeto clasificado")