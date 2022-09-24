#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     22/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    lista = [[23,45,63],[72,81,91],[56,64,37],[34,75,26]]

    def recorrer (lista):
        if len(lista) == 0:
            print("listo")
        else:
            print(lista[0])
            recorrer(lista[1:])
    recorrer(lista)



if __name__ == '__main__':
    main()
