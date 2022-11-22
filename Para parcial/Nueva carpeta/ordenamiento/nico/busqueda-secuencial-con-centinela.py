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

lista=["pedro","matias","tomas","hugo"]

def centinela(lista, buscado) :
# Metodo de busqueda secuencial con centinela
    posicion = -1
    i = 0

    while (i < len(lista)) and (posicion == -1) :
        if (lista[i] == buscado) :
            posicion = i

        i += 1

    return posicion


print(centinela(lista, "hugo"))