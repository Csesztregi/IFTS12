#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     16/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#implementar una función que calcule la suma de todos los numeros enteros comprendidos entre 0 y un numero entero positivo dado

def main():
    pass
    lista=[]

    def calculo_suma(numero):
        for i in range(numero+1):
            lista.append(i)
        print("La lista de numeros es ", lista)
        suma = 0
        for i in lista:
            suma += i
        print("La suma de esos numeros es ", suma)

    calculo_suma(int(input("Escribe un numero para hacer el cálculo")))


if __name__ == '__main__':
    main()
