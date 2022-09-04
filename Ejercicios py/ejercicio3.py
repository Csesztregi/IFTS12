#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     03/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
valido=False

mail=input("ingrese su mail: ")

for i in range(len(mail)):
    if mail[i]=="@":
        valido=True
if valido:
    print ("email correcto")
else:
    print("email incorrecto")





if __name__ == '__main__':
    main()
