#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     02/11/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


class nodoPila(object) :
    """Clase nodo pila"""
    info, sig = None, None

class Pila(object) :
    """Clase Pila"""
    def __init__(self) :
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato) :
        """Apila el elemento sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima

        self.cima = nodo
        self.tamanio += 1

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x

    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def en_cima(self) :
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None :
            return self.cima.info
        else :
            return None

    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio
vocal=Pila()
consonante=Pila()
caracter=Pila()
contblanco=0
variable = ("1papelito 23 papeleo un papelon35, de la gran flauta1.1")
for i in (variable):
    if (i == "a" or i == "e" or i == "i" or i == "u" or i == "o"):
        vocal.apilar(i)
    elif (i == "c" or i == "d" or i == "f" or i == "g" or i == "h"or i == "j"or i == "k"or i == "l"or i == "m"or i == "n"or i == "p"or i == "q"or i == "r"or i == "s"or i == "t"or i == "x"or i == "y"or i == "z"):
        consonante.apilar(i)
    else:
        caracter.apilar(i)
for i in (variable):
    if (i == " "):
        contblanco+=1
total=(consonante.tamanio + caracter.tamanio + vocal.tamanio)
cont=0
sustituto=Pila()

while (not caracter.pila_vacia()):

    if (caracter.en_cima()) == "1" or (caracter.en_cima()) =="2" or (caracter.en_cima()) =="3" or (caracter.en_cima()) == "4" or (caracter.en_cima()) == "5" or (caracter.en_cima()) == "6"or (caracter.en_cima()) == ""or (caracter.en_cima()) == "7"or (caracter.en_cima()) == "8"or (caracter.en_cima()) == "9":
        cont+=1
    sustituto.apilar(caracter.en_cima)
    caracter.desapilar()
while (not sustituto.pila_vacia()):
    caracter.apilar(sustituto.en_cima)
    sustituto.desapilar()

print("hay un total de",consonante.tamanio,"consonantes","un total de",vocal.tamanio,"vocales","y un total de",caracter.tamanio,"caracteres")
print("hay un total de",contblanco,"espacios en blanco")
print ("El porcentale de vocales es de", vocal.tamanio * 100 / total, "%")
print("la cantidad de numeros totales es de", cont)


if __name__ == '__main__':
    main()
