#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Fillory
#
# Created:     16/11/2022
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
    def ocurrencia (self,pila,aux,reemplazo):
        lista=[]
        while (not pila.pila_vacia()):
            dato = pila.desapilar()

            if (dato not in lista):
                aux.apilar(dato)
                lista.append(dato)
            else:
                aux.apilar(reemplazo)

pdatos = Pila()
aux = Pila()
pdatos.apilar(2)
pdatos.apilar(5)
pdatos.apilar(2)
pdatos.apilar(7)
pdatos.apilar(7)
pdatos.apilar(25)
pdatos.apilar(25)
pdatos.ocurrencia(pdatos,aux,9)
while (not aux.pila_vacia()):
    dato = aux.desapilar()
    print (dato)



if __name__ == '__main__':
    main()
