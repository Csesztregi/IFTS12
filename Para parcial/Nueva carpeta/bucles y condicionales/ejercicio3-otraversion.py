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

def main():
    mail = input('Ingrese su mail: ')
    mail2 = mail.replace("@", "Q")
    if(mail != mail2):
        print('El mail es correcto')
    else:
        print('El mail no es correcto')

if __name__ == '__main__':
    main()
