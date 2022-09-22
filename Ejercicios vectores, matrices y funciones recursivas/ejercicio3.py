#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Fillory
#
# Created:     21/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
    lista=[]
    def suma(numero):
        for i in range(numero+1):
            lista.append(i)
        suum=0
        for i in lista:
            suum += i
        print (suum)
    suma(2)





if __name__ == '__main__':
    main()
