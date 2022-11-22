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

def ejercicio7():
    lista = [100, 14, 15, 70, -1, 46, 23, 99]
    maximo = 0

    for i in lista:
        if i > maximo:
            maximo = i
    print(maximo)

if __name__ == '__main__':
    ejercicio7()
