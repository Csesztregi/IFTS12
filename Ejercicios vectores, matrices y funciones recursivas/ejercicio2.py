#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     20/09/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

    diccionarios={}
    totales={
        'stock':0,
        'monto':0}

    def pedirdatos(diccionarios):
        ISBN=input("Ingrese ISBN: ")
        if (ISBN != "0"):
            nombre=input("Coloque el nombre del libro: ")
            stock=int(input("coloque el stock: "))
            precio=int(input('coloque el precio'))

            diccionario= {'ISBN': ISBN, 'NombreLibro': nombre, 'stock':stock, 'precio': precio,}

            totales['stock'] += stock
            totales['monto'] += precio * stock

            diccionarios[ISBN] = diccionario
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
