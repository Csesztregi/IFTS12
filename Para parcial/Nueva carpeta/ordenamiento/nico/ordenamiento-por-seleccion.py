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
lista=[4,3,2,1]

def seleccion(lista) :
#Método de ordenamiento selección
     for i in range(0, len(lista)-1) :
        print(f"PRIMER FOR:recorro desde {i} en rango de 0 a {len(lista)-1}")
        minimo = i
        print(f"el minimo es {lista[minimo]}")
        for j in range(i+1, len(lista)) :
            print(f"SEGUNDO FOR: para {j} desde {i+1} hasta {len(lista)}")
            if (lista[j] < lista[minimo]) :
                print(f"comparacion: {lista[j]}<{lista[minimo]}")
                minimo = j
                print(f"ahora minimo es {lista[minimo]}")

        lista[i], lista[minimo] = lista[minimo], lista[i]
        print("intercambio:")
        print(lista)

print(lista)
seleccion(lista)
print(lista)

