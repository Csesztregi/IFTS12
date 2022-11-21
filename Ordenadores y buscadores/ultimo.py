#-------------------------------------------------------------------------------
# Name:        module5
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
sucursales=[ "Almagro", "Belgrano", "Caballito", "Palermo", "Villa Crespo" ]
datos={
    "registros": []
}

def pedirdatos (datos):
    nro = int(input("Ingrese Nro. de registro: "))
    while (nro != 0):
        sucursal = 2
        producto = 3
        ventas = 20

        guardar= {
            "nro":nro,
            "sucursal":sucursal,
            "producto":producto,
            "ventas":ventas
        }
        datos["registros"].append(guardar)
        nro = int(input("Ingrese Nro. de registro: "))

def ventas (datos):
    for i in (datos["registros"]):
        if (i['producto'] == 3):
            print (f'la sucursal:',(sucursales[i['sucursal']]),'tuvo',{i['ventas']},' ventas de el principito')

pedirdatos(datos)
print (datos["registros"])
print(ventas(datos))


if __name__ == '__main__':
    main()
