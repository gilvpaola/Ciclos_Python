# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:50:52 2021

@author: USUARIO
"""

# Programa para determinar el costo del tiquete de una aerolinea según edad
# del pasajero, ciudad de origen y ciudad de destino

nombre = input("Ingrese su nombre: ")
origen = int(input(f"{nombre} ingrese su ciudad de origen: "))
destino = int(input(f"{nombre} ingrese su ciudad de destino: "))
edad = int(input(f"{nombre} ingrese su edad: "))

if origen == 5 or destino == 5:
    costo_tiquete = 980000
else:
    if origen == 1:
        if destino == 2:
            costo_tiquete = 200000
            if edad < 60:
                costo_tiquete = 210000
        elif destino == 3:
            costo_tiquete = 250000 - .1 * edad * 1000
        elif destino == 4:
            costo_tiquete = 300000 + edad * 1000
        elif origen == 2:
            if destino == 1:
                if edad > 80:
                    costo_tiquete = 0
                else:
                    costo_tiquete = 200000
            elif destino == 3:
                costo_tiquete = 200000
                if edad < 60:
                    diferencia = 60 - edad
                    if diferencia > 20:
                        sobrecosto = 20000
                    else:
                        sobrecosto = diferencia * 1000
                    costo_tiquete = 200000 + sobrecosto
            elif destino == 4:
                costo_tiquete = 400000
                if edad > 60:
                    costo_tiquete = 400000 + 0.05 * 10000
        elif origen == 3:
            if destino == 1:
                costo_tiquete = 350000
            elif destino == 2:
                costo_tiquete = 280000
                if edad < 60:
                    costo_tiquete = 300000
            elif destino == 4:
                costo_tiquete = 190000
                if edad < 60:
                    costo_tiquete = 200000
        elif origen == 4:
            if destino == 1:
                costo_tiquete = 500000
                if edad < 10:
                    costo_tiquete = 250000
            elif destino == 2:
                costo_tiquete = 210000
                if edad < 30:
                    costo_tiquete = 240000
            elif destino == 3:
                costo_tiquete = 350000
                if edad > 60:
                    costo_tiquete = 350000 + (edad - 60) * 10000
                    
print(nombre, "El costo de su tiquete es: ", costo_tiquete)
                
                
 