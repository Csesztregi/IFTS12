#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     14/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    def recortar(nro, liminf, limsup):
        if (nro < liminf):
            return liminf
        elif (nro > limsup):
            return limsup
        else:
            return nro
    print (recortar(35, 20, 80))




if __name__ == '__main__':
    main()
