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
lista=[3,2,1]

def insercion(lista) :
    print("Método de ordenamiento inserción")
    for i in range(1, len(lista)+1):
        print("estoy en el for", lista)
        print(f"recorro desde {i} hasta {len(lista)+1}")
        k = i-1
        while (k > 0) and (lista[k] < lista[k-1]) :
            print("intercambio:")

            lista[k], lista[k-1] = lista[k-1], lista[k]

            k -= 1

            print("estoy en el while", lista)

insercion(lista)
print(lista)

