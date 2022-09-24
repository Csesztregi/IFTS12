#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     24/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
from random import *

n = randint(1,6)


def acertar (n1):
    n2=(int(input("escriba un numero del 1 al 6: ")))
    if n2==n:
        print ("¡correcto! lo adivinaste en",n1,"intentos")
    else:
        n1+=1
        acertar(n1)
acertar(1)



if __name__ == '__main__':
    main()
