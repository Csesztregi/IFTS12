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

#ordenamiento por seleccion

lista=[1,2,60,40,3]

def seleccion(lista) :

    for i in range(0, len(lista)-1) :
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j] < lista[minimo]) :
                minimo = j
                lista[i], lista[minimo] = lista[minimo], lista[i]

seleccion(lista)
print(lista)

def seleccion_mayor(lista):

    for i in range(0, len(lista)-1):
        maximo = i
        for j in range(i+1, len(lista)):
            if(lista[j] > lista[maximo]):
                maximo = j
                lista[i], lista[maximo] = lista[maximo], lista[i]

seleccion_mayor(lista)
print(lista)