# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:30:38 2021

@author: USUARIO
"""

# Programa que permite clasificar según el tipo de profesión

ingenieros = medicos = abogados = otros = 0 # Se inicializan contadores respectivos

nombre = input("Ingrese su nombre: ")
profesion = int(input(f"{nombre} ingrese su profesión: "))

if profesion == 1:
    ingenieros += 1
elif profesion == 2:
    medicos += 1
elif profesion == 3:
    abogados += 1
else:
    otros += 1
    
print (f"Ingenieros = {ingenieros} \nMedicos = {medicos}")
print (f"Abogados = {abogados} \nOtros = {otros}")
    