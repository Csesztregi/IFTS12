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

def recortar(nro, liminf, limsup):
    if (nro < liminf):
        return liminf
    elif (nro > limsup):
        return limsup
    else:
        return nro

if __name__ == '__main__':
    recortar(50, 20, 80)
