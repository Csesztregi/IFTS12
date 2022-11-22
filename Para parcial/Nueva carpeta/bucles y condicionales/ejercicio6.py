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

def ejercicio6():
    lista = [20, 30, 12, 35, 6, 7, 67, 80, 77]
    contador = 0
    acum = 0


    for i in lista:
        contador += 1
        acum += i
        promedio = acum / contador
    print("el promedio es: ", promedio)

if __name__ == '__main__':
    ejercicio6()
