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


    def cuenta_regresiva(n1):
        if n1==0:
            print ("¡Boom!")
        else:
            print (n1)
            n1-=1
            cuenta_regresiva(n1)
    cuenta_regresiva(6)

if __name__ == '__main__':
    main()