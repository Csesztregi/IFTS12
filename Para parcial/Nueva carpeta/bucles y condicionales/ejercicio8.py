#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     04/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ejercicio8():
    lista = [17, 2, 3, 6, 99, 234, 5, 35, 67, 1]
    minimo = 100

    for i in lista:
        if i < minimo:
            minimo = i

    print("el mínimo es: ", minimo)

if __name__ == '__main__':
    ejercicio8()
