#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     07/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    lista = [7,14,20,30,2,13,15,19]
    def separar(l1):
        par = []
        inpar = []
        for i in l1:
            if i % 2 == 0:
                par.append (i)
            else:
                inpar.append (i)
        return par, inpar

    print (separar(lista))









if __name__ == '__main__':
    main()
