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
lista= ["a","b","c","d"]

def burbuja(lista) :
#Método de ordenamiento burbuja
    for i in range(0, len(lista)-1) :
        print("el i del primer for vale", i, "y el valor es", lista[i])
        print("primer for")
        for j in range(0, len(lista)-i-1) :
            print(j)
            print("comparación:", lista[j], ">", lista[j+1])
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)

print(lista)

burbuja(lista)

print(lista)