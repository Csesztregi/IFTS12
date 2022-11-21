#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      gmoya
#
# Created:     01/11/2022
# Copyright:   (c) gmoya 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class nodoLista(object) :
    """Clase nodo lista"""
    info, sig = None, None

class Lista(object) :
    """Clase Lista enlazada simple"""
    def __init__(self) :
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

    def insertar(self, dato) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.info = dato

        if (self.inicio is None) or (self.inicio.info > dato) :
            nodo.sig = self.inicio
            self.inicio = nodo
        else :
            ant = self.inicio # anterior
            act = self.inicio.sig # actual

            while (act is not None and act.info < dato) :
                ant = ant.sig
                act = act.sig

            nodo.sig = act
            ant.sig = nodo

        self.tamanio += 1

    def eliminar(self, clave) :
        """Elimina un elemento de la lista y lo devuelve si lo encuentra"""
        dato = None

        if (self.inicio.info == clave) :
            dato = self.inicio.info
            self.inicio = self.inicio.sig
            self.tamanio -= 1
        else :
            ant = self.inicio
            act = self.inicio.sig

            while (act is not None and act.info != clave) :
                ant = ant.sig
                act = act.sig

            if (act is not None) :
                dato = act.info
                ant.sig = act.sig
                self.tamanio -= 1

        return dato

    def buscar(self, buscado) :
        """Devuelve la dirección del elemento buscado"""
        aux = self.inicio

        while (aux is not None and aux.info != buscado) :
            aux = aux.sig

        return aux

    def lista_vacia(self) :
        """Devuelve true si la lista está vacía"""
        return self.inicio is None

    def tamanio(self) :
        """Devuelve el número de elementos en la lista"""
        return self.tamanio

    def barrido(self) :
        """Realiza un barrido de la lista mostrando los valores"""
        aux = self.inicio

        while (aux is not None) :
            print(aux.info)
            aux = aux.sig


agrego=Lista()
par=Lista()
impar=Lista()

nros=[1,2,3,4,5,6,7,8,9,6,5,4,3,2]

for nros in nros:
    agrego.insertar(nros)

nodo= agrego.inicio
while (nodo is not None):

    if (nodo.info % 2 == 0):
        par.insertar(nodo.info)
    else:
        impar.insertar(nodo.info)
    nodo = nodo.sig

par.barrido()
print ('\n')
impar.barrido()
