#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     02/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ejercicio3():
    arroba = "@"
    email = input("Por favor, ingrese un email")
    if (email.find(arroba) == -1):
        print("Usted NO ingreso un email")
    else:
        print("Usted ingresó un email")

if __name__ == '__main__':
    ejercicio3()
