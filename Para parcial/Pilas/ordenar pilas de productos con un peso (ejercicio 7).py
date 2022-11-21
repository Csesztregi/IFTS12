#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fillory
#
# Created:     17/11/2022
# Copyright:   (c) Fillory 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

class nodoPila(object) :
    """Clase nodo pila"""
    nombre, peso, sig = None, None, None

class Pila(object) :
    """Clase Pila"""
    def __init__(self) :
        self.cima = None
        self.tamanio = 0

    def apilar(self, nombre, peso) :
        """Apila el elemento sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.nombre = nombre
        nodo.peso = peso
        nodo.sig = self.cima

        self.cima = nodo
        self.tamanio += 1

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x

    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def en_cima(self) :
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None :
            return self.cima.nombre, self.cima.peso
        else :
            return None

    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio

    def ordenpeso (self):
        pila2 = Pila()
        while(not pila1.pila_vacia()):
            nodo = self.desapilar()

            while (not pila2.pila_vacia() and  int(pila2.cima.peso) > int(nodo.peso)) :

                mayor = pila2.desapilar()
                print('DEBUG: Apilo mayor: ', mayor.peso)

                # Apilo la cima del mazo ordenado en la cima del mazo desordenado
                self.apilar(mayor.peso, mayor.nombre)

            # Apilo la carta en el mazo ordenado
            pila2.apilar(nodo.peso, nodo.nombre)
            print('DEBUG: apilar carta \n')

        # Pasar del mazo ordenado DESC al mazo vacío
        while (not pila2.pila_vacia()) :
            nodo = pila2.desapilar()
            self.apilar(nodo.peso, nodo.nombre)




producto = ["licuadora","pava","pastalinda","horno"]
pila1=Pila()
pila2=Pila()
pila1.apilar(3,10)
pila1.apilar(1,3)
pila1.apilar(0,1)
pila1.apilar(2,4)
print (pila1.en_cima())
pila1.ordenpeso()


while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print (producto[dato.nombre],dato.peso)





if __name__ == '__main__':
    main()
