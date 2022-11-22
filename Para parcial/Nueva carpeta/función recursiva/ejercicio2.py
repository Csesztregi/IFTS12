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
    diccionarios= {}
    totales = {
        'stock': 0,
        'monto': 0
    }

    def pedirdatos(diccionarios):
        isbn = input("Ingrese un ISBN")
        if(isbn != "0"):

            libro = input("Ingrese el nombre del libro")
            stock = int(input("Ingrese el stock"))
            precio = int(input("Ingrese el precio del libro"))

            diccionario = {
                'isbn': isbn,
                'NombredelLibro': libro,
                'Stock': stock,
                'Precio': precio
            }

            totales['stock'] += stock
            totales['monto'] += precio * stock

            diccionarios[isbn] = diccionario
            pedirdatos(diccionarios)

        else:
            return

    pedirdatos(diccionarios)

    if (diccionarios != {}):
        print(diccionarios)
        print("La cantidad total de libros es ", totales['stock'])
        print("El monto total de los libros es ", totales['monto'])
        print("El valor promedio de los libros es ", totales['monto']/totales['stock'])

if __name__ == '__main__':
    main()
