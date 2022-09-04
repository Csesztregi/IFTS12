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

def ejercicio2():
    numero1= (int (input("Por favor, ingrese un número")))
    numero2= (int(input("Por favor, ingrese otro número")))
    print("sumar, restar o multiplicar")
    opcion = input("Por favor ingrese una opción")
    while opcion != "sumar" is not opcion != "restar" is not opcion is not "multiplicar":
          opcion = input("Opción incorrecta. Por favor ingrese una opción")
    if (opcion == "sumar"):
        print(numero1+numero2)
    elif(opcion == "restar"):
        print(numero1-numero2)
    else:
        print(numero1*numero2)
    print("Operación finalizada")
if __name__ == '__main__':
    ejercicio2()
