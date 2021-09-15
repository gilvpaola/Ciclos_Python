# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:52:09 2021

@author: USUARIO
"""

# Programa que lee tres números enteros y los escribe ordenados
# ascendentemente.

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
c = int(input("Ingrese el tercer número enter: "))

# Primera forma: Pregunta compuesta
# NOTA: No escribe nada si se tienen dos datos iguales

if a < b and b < c:
    print("a", a, "b", b, "c", c)
if a < c and c < b:
    print("a", a, "c", c, "b", b)
if b < a and a < c:
    print("b", b, "a", a, "c", c)
if b < c and c < a:
    print("b", b, "c", c, "a", a)
if c < a and a < b:
    print("c", c, "a", a, "b", b)
if c < b and b < a:
    print("c", c, "b", b, "a", a)
    
print("Terminó la primera forma")
    
# Segunda forma: Pregunta compuesta con < o =

if a <= b and b <= c:
    print("a", a, "b", b, "c", c)
else:
    if a <= c and c <= b:
        print("a", a, "c", c, "b", b)
    else:
        if b <= a and a <= c:
            print("b", b, "a", a, "c", c)
        else:
            if b <= c and c <= a:
                print("b", b, "c", c, "a", a)
            else:
                if c < a and a < b:
                    print("c", c, "a", a, "b", b)
                else:
                    print("c", c, "b", b, "a", a)

print("Terminó la segunda forma")

# Tercera forma: If anidados

if a < b:
    if b < c:
        print("a", a, "b", b, "c", c)
    else:
        if a < c:
            print("a", a, "c", c, "b", b)
        else:
            print("c", c, "a", a, "b", b)
else:
    if a < c:
        print("b", b, "a", a, "c", c)
    else:
        if b < c:
            print("b", b, "c", c, "a", a)
        else:
            print("c", c, "b", b, "a", a)
        
            
print("Terminó la tercera forma")        
        
            
            
            
        
        
                
                
                

    

