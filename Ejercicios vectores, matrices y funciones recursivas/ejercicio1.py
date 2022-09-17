#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     15/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    lista= []
    promedios=[]
    acuventa=[]

    def pedirdatos(lista):
        ID= input ("ingrese ID del local: ")
        lista.append(ID)
        if (ID != "0"):
            nombre= input ("ingrese nombre del local: ")
            lista.append(nombre)
            ventas= int(input("ingrese la cantidad de ventas: "))
            lista.append(ventas)
            totventas= int(input("ingrese la cantidad total de ventas en pesos: "))
            acuventa.append(totventas)
            lista.append(totventas)
            promedio= totventas/ventas
            promedios.append(promedio)
            pedirdatos(lista)

        else:
            print (f"los datos ingresados son: ", lista)
            print (f"El promedio de las ventas son: ", promedios)
            print (f"El total de ventas de las sucursales son: ", acuventa)
    pedirdatos(lista)










if __name__ == '__main__':
    main()
