#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Fillory
#
# Created:     04/10/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
    personajes=["lisa","homero","moe","milhouse","flanders","skinner","barney","burns", "march"]
    def burbuja(lista) :

        i = 0
        control = True
        while (i <= len(lista)-2) and control :
            control = False
            for j in range(0, len(lista)-1) :
                if (lista[j] > lista[j+1]) :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    control = True
            i += 1

    def buscar (lista,buscado):
        posicion=-1
        for i in range (0, len(lista)):
            if (lista[i]==buscado):
                posicion=i
        return posicion

    def otro (lista):
        for i in lista:
            if i > "lisa":
                print (i)
    def l (lista):
        for i in lista:
            for j in (i):
                if j == "m":
                    print (f"empieza con m: ",i)
                else:
                    break





    burbuja(personajes)
    print (personajes)
    print ("\n")
    print(f"la posicion es: ",(buscar(personajes,"lisa")))
    print ("\n")
    print (otro(personajes))
    print ("\n")
    print(l(personajes))
if __name__ == '__main__':
    main()
