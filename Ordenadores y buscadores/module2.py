#-------------------------------------------------------------------------------
# Name:        module2
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
    import time
    tiempo_inicio= time.time()
    lista=[12,2,44,1123,5435,6,3,23,24,5436,358,6845,634,6547,45643,654]
    def orden (lista):
        control=True
        contador=0
        while (contador<len(lista)-1) and control:
            control=False
            for j in range(0,len(lista)-1):
                if (lista[j] < lista[j+1]):
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]
                    control=True
            contador+=1
    tiempo_fin=time.time()
    tiempo= tiempo_fin - tiempo_inicio

    def buscar (lista, buscado):
        posicion=-1
        for i in range (0,len(lista)):
            if (lista[i] == buscado):
                posicion=i+1
        return posicion

    def imp (lista, buscado):
        for i in range (0,len(lista)):
            if (lista[i] == buscado):
                break
            else:
                print (lista[i])





    orden(lista)
    print (lista)
    print (f"el tiempo fue de",tiempo,"segundos")
    print (f"la posicion de su numero es:",(buscar(lista,5436)))
    print (imp(lista, 654))


if __name__ == '__main__':
    main()
