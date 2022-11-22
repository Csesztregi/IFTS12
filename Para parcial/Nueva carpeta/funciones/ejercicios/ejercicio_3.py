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

def relacion(numero1, numero2):
    if (numero1 > numero2):
        return 1
    elif (numero1 < numero2):
        return -1
    else:
        0

if __name__ == '__main__':
    relacion(1,2)
