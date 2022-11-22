#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     10/10/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
cien=100
cienmil=100000
unmillon=1000000
diezmillones=10000000
import random #importa una librería random
import time #importa una librería de tiempo
timeinicial=time.time()


for i in range(cien):
    aux=random.randint(0,100)
    elementosaleatorios.append(aux)

print(f"La lista sin ordenar es: {elementosaleatorios}")



def ordenamiento_burbuja(lista) :
#Método de ordenamiento burbuja mejorado
    i = 0
    control = True

    while (i <= len(lista)-2) and control :
        control = False
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
                i += 1


ordenamiento_burbuja(elementosaleatorios)
print(f"La lista ordenada es: {elementosaleatorios}")

timefinal=time.time()

print(f"El tiempo inicial fue {timeinicial}, el tiempo final fue {timefinal}")
print("El algoritmo tardó:", timefinal-timeinicial, "en ordenar los")