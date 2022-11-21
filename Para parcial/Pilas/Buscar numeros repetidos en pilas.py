#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     01/11/2022
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
    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x
    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def ocurrencia(self, dato):
        contador=0

        while (not variable.pila_vacia()):
            if self.cima.info==dato:
                contador+=1
                variable.desapilar()


            else:
                variable.desapilar()


        print ("el numero",dato, "se repite", contador, "veces")



variable=Pila()
variable.apilar(25)
variable.apilar(2)
variable.apilar(33)
variable.apilar(2)
variable.apilar(33)
(variable.ocurrencia(33))
print(variable.tamanio)












if __name__ == '__main__':
    main()
