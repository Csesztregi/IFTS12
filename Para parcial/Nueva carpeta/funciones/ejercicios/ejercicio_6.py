#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     13/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
lista = [12, 4, 28, 90, 7, 21, 51, 27, 30, 8, 5]

def separar():
    pares = []
    impares = []
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares


if __name__ == '__main__':
    separar()
