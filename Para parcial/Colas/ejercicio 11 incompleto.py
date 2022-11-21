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
from datetime import time
class nodoCola(object) :
    """Clase nodo cola"""
    app, hora, mje, sig = None, None, None, None

class Cola(object) :
    """Clase Cola"""
    def __init__(self) :
        """Crea una cola vacía"""
        self.frente, self.final = None, None
        self.tamanio = 0

    def arribo(self, app, hora, mje) :
        """Arriba el elemento al final de la cola"""
        nodo = nodoCola()
        nodo.app = app
        nodo.hora = hora
        nodo.mje = mje

        if self.frente is None :
            self.frente = nodo
        else :
            self.final.sig = nodo

        self.final = nodo
        self.tamanio += 1

    def atencion(self) :
        """Atiende el elemento en el frente de la cola y lo devuelve"""
        dato = self.frente
        self.frente = self.frente.sig
        if self.frente is None :
            self.final = None

        self.tamanio -= 1
        return dato
##        return aplicaciones[dato.app], dato.hora, dato.mje

    def cola_vacia(self) :
        """Devuelve true si la cola está vacía"""
        return self.frente is None

    def en_frente(self) :
        """Devuelve el valor almacenado en el frente de la cola"""
        if self.frente is not None :
            return self.frente

    def tamanio(self) :
        """Devuelve el nro de elementos en la cola"""
        return self.tamanio

    def mover_al_final(self) :
        """Mueve el elemento del frente al final de la cola"""
        dato = self.atencion()
        self.arribo(dato.app,dato.hora,dato.mje)

        return dato

    def filtro (self,desde,hasta):
        dato = self.frente
        while (not self.cola_vacia()):

            if dato.hora < desde and dato.hora > hasta:
                cola2.arribo(dato.app,dato.hora,dato.mje)
                self.atencion()

            else:
                self.atencion()

    def delface (self):
        while (not self.cola_vacia()):
            dato = self.atencion()

            if dato.app == 0:
                print("eliminado")
                aux.arribo(dato.app,dato.hora,dato.mje)

            else:
                cola2.arribo(dato.app,dato.hora,dato.mje)
                aux.arribo(dato.app,dato.hora,dato.mje)
    def twit (self):
        for i in range (self.tamanio):
            dato = self.mover_al_final()
            if (dato.app == 1):
                print (dato.mje)








aplicaciones = ["Facebook","Twitter","Instagram"]
cola1 = Cola()
cola2 = Cola()
aux = Cola()
cola1.arribo(0,time(17,30),"tienes un mensaje")
cola1.arribo(2,time(11,30),"Carlos subio una historia")
cola1.arribo(0,time(14,30),"tienes una notificacion pendiente")
cola1.arribo(1,time(18,30),"Charly garcia se presentara en una conferencia de Python.....")
cola1.delface()
while (not cola2.cola_vacia()):
    dato = cola2.atencion()
    print(aplicaciones[dato.app],dato.hora,dato.mje)

aux.twit()

##dato = cola1.atencion()
##print(dato)




if __name__ == '__main__':
    main()
