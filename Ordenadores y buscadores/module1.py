#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     05/10/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


datos = {
        "libros": [ "Don Quijote", "Historia de dos ciudades", "El Señor de los Anillos", "Harry Potter y la piedra filosofal", "El principito" ],
        "sucursales": [ "Almagro", "Belgrano", "Caballito", "Palermo", "Villa Crespo" ],
        "total": 0,
        "registros": []
    }
principito=5

def solicitarDatos(datos) :
    nro_registro = int(input("Ingrese Nro. de registro: "))

    while (nro_registro != 0) :
        nro_sucursal = int(input("Ingrese Nro. de sucursal: "))
        nro_producto = int(input("Ingrese Nro. de producto: "))
        ventas = int(input("Ingrese cantidad de ventas: "))

        registro = {
            "nro_registro": nro_registro,
            "nro_sucursal": nro_sucursal,
            "nro_producto": nro_producto,
            "ventas": ventas
        }

        datos['total'] += registro['ventas']
        datos['registros'].append(registro)

        nro_registro = int(input("Ingrese Nro. de registro: "))
    print('\n')

solicitarDatos(datos)
print (datos["registros"])
print (datos["registros"])







if __name__ == '__main__':
    main()
