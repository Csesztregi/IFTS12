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
lista=[5,6,90, 12]

def quicksort(lista, primero, ultimo) :
 #Metodo de ordenamiento quicksort""
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo

    while (izquierda < derecha) :
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
            izquierda += 1

    while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
        derecha -= 1

    if (izquierda < derecha) :
        lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    if (lista[pivote] < lista[izquierda]) :
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    if (primero < izquierda) :
        quicksort(lista, primero, izquierda-1)

    if (ultimo > izquierda) :
        quicksort(lista, izquierda+1, ultimo)

quicksort(lista,0,3)
print(lista)