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

def main():
    lista= []
    promedios=[]
    acumventa=[]

    def pedirdatos(lista):
        id = input("Ingrese ID de sucursal")
        if(id != "0"):
            nombre = input("Ingrese nombre de sucursal")
            ventas = int(input("Ingrese cantidad de ventas"))
            totalventa = int(input("Ingrese ventas total de la sucursal"))
            promedio = totalventa/ventas

            lista.append(id)
            lista.append(nombre)
            lista.append(ventas)
            lista.append(totalventa)
            promedios.append(promedio)
            acumventa.append(totalventa)
            pedirdatos(lista)
        else:
            return


    def imprimirdatos(lista):
        print("Su lista es", lista)

    pedirdatos(lista)

    if (lista != []):

        imprimirdatos(lista)
        print("Sus promedios son", promedios)
        contador = 0
        for i in acumventa:
            contador += i
        print("El total vendido por toda la cadena es", contador)

if __name__ == '__main__':
    main()
