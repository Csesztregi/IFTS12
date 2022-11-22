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

n1= (int (input("ingrese un numero impar: ")))
while n1 % 2 == 0:
    n1= (int (input("ingrese un numero impar: ")))
print ("numero impar correcto")