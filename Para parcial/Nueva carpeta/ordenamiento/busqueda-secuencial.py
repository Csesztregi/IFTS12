#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Daniela
#
# Created:     10/10/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
lista=[1,50,23,100,33]

def secuencial(lista, buscado) :
#Metodo de busqueda secuencial
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i] == buscado) :
            posicion = i

    return posicion

print(secuencial(lista, 23))
