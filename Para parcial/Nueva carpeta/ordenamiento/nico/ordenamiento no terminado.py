#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     03/10/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import random
    import time
    inicio = time.time()
    pass
    lista= [random.randint(0, 100) for i in range(5000)]

    def ordenar (lista):


        for i in range (0, len(lista)):
            for j in range (0, len(lista)-1):
                if (lista[j] > lista[j+1]):
                    lista[j] , lista[j+1] = lista[j+1] , lista[j]

            i+=1

    ordenar(lista)

    final = time.time()

    print("burbuja")
    print("tiempo: ", final - inicio)



    #--------------------------------------------------------------------------------------------------------------

    inicio2 = time.time()
    lista2= [random.randint(0, 100) for i in range(5000)]
    def burbuja_mejorado(lista) :

        i = 0
        control = True
        while (i <= len(lista2)-2) and control :
            control = False
            for j in range(0, len(lista2)-1) :
                if (lista2[j] > lista2[j+1]) :
                    lista2[j], lista2[j+1] = lista2[j+1], lista2[j]
                    control = True
            i += 1
    burbuja_mejorado(lista2)

    final2 = time.time()
    mejor4=final2 - inicio2
    print("Burbuja mejorada")
    print(f"tiempo: ", final2 - inicio2)
    #--------------------------------------------------------------------------------------------------------------

    inicio3 = time.time()
    lista3= [random.randint(0, 100) for i in range(5000)]
    def seleccion(lista) :

        for i in range(0, len(lista)-1) :
            minimo = i
            for j in range(i+1, len(lista)) :
                if (lista[j] < lista[minimo]) :
                    minimo = j

            lista[i], lista[minimo] = lista[minimo], lista[i]


    seleccion(lista3)

    final3 = time.time()
    mejor3=final3 - inicio3
    print("por seleccion")
    print(f"tiempo: ", final3 - inicio3)

    #--------------------------------------------------------------------------------------------------------------
    inicio4 = time.time()
    lista4= [random.randint(0, 100) for i in range(50)]
    def insercion(lista) :

        for i in range(1, len(lista)+1) :
            k = i-1
            while (k > 0) and (lista[k] > lista[k-1]) :
                lista[k], lista[k-1] = lista[k-1], lista[k]
                k -= 1
    insercion(lista4)
    final4 = time.time()
    mejor2= final4 - inicio4
    print("insercion")
    print(f"tiempo: ", final4 - inicio4)
    #--------------------------------------------------------------------------------------------------------------
    inicio5 = time.time()
    listass= [random.randint(0, 100) for i in range(500)]
    def quicksort(lista, primero, ultimo) :

        izquierda = primero
        derecha = ultimo - 1
        pivote = ultimo

        while (izquierda < derecha) :
            while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
                izquierda += 1

            while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
                derecha -= 1

            if (izquierda < derecha) :
                lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

        if (lista[pivote] < lista[izquierda]) :
            lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

        if (primero < izquierda) :
            quicksort(lista, primero, izquierda-1)

        if (ultimo > izquierda) :
            quicksort(lista, izquierda+1, ultimo)

    quicksort(listass,0,-1)
    print ("\n")
    final5 = time.time()
    print("ordenamiento rapido")
    print(f"tiempo: ", final5 - inicio5)
    mejor1=final5-inicio5

    #encontrar el numero mas alto
    if mejor1>mejor2 and mejor1>mejor3 and mejor1>mejor4:
        print (f"quicksort es el mas rapido, tarda",mejor1)
    if mejor2>mejor1 and mejor2>mejor3 and mejor2>mejor4:
        print (f"quicksort es el mas rapido, tarda",mejor2)
    if mejor3>mejor2 and mejor3>mejor1 and mejor3>mejor4:
        print (f"quicksort es el mas rapido, tarda",mejor3)
    if mejor4>mejor2 and mejor4>mejor3 and mejor4>mejor1:
        print (f"quicksort es el mas rapido, tarda",mejor4)



    #--------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
