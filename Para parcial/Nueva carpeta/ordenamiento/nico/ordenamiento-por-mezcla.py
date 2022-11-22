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
izquierda=[1,3,2]
derecha=[5,6,7]


def merge(izquierda, derecha) :
 #Funcion para mezclar listas ya ordenadas
    lista_mezclada = []

    while (len(izquierda) > 0) and (len(derecha) > 0) :

        if (izquierda[0] < derecha[0]) :
            lista_mezclada.append(izquierda.pop(0))

        else :
            lista_mezclada.append(derecha.pop(0))

    if (len(izquierda) > 0) :
        lista_mezclada += izquierda

    if (len(derecha) > 0) :
        lista_mezclada += derecha

    return lista_mezclada

lista= merge(izquierda,derecha)
print(lista)

