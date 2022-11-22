#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     07/10/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
lista=[1,20,60,30, 40, 2]

def burbuja_mejorado(lista) :
#Método de ordenamiento burbuja mejorado"""
    i = 0
    control = True
    while (i <= len(lista)-2) and control :
        control = False
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
                i += 1


burbuja_mejorado(lista)
print(lista)