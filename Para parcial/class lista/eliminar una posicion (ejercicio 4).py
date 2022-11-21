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
    posicion,info, sig = None, None, None

class Lista(object) :
    """Clase Lista enlazada simple"""
    def __init__(self) :
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

    def insertar(self,posicion, dato) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.info = dato
        nodo.posicion = posicion

        if (self.inicio is None) or (self.inicio.posicion > posicion) :
            nodo.sig = self.inicio
            self.inicio = nodo
        else :
            ant = self.inicio # anterior
            act = self.inicio.sig # actual

            while (act is not None and act.posicion < posicion) :
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

    def que_tamanio(self) :
        """Devuelve el número de elementos en la lista"""
        return self.tamanio

    def barrido(self) :
        """Realiza un barrido de la lista mostrando los valores"""
        aux = self.inicio

        while (aux is not None) :
            print(aux.info)
            aux = aux.sig

    def inserorden(self,posicion, dato) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.info = dato
        nodo.posicion = posicion

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



nros1 = [4,42,52,6,7]
nros2 = [4,2,6,2,2,7]
lista1 = Lista()
lista2 = Lista()

#agregar numeros a las 2 listas
for i in nros1:
    lista1.insertar(1,i)

for i in nros2:
    lista2.insertar(2,i)
##
###unir las dos listas en una
##aux = lista2.inicio
##for i in range (lista2.que_tamanio()):
##
##    lista1.insertar(aux.posicion,aux.info)
##    aux = aux.sig
##lista1.barrido()

#concatenar dos listas en una sola omitiendo los datos repetidos y
#manteniendo su orden;

cont = 0
aux = lista2.inicio
for i in range (lista2.que_tamanio()):
    if not lista1.buscar(aux.info):
        lista1.inserorden(1,aux.info)
        aux = aux.sig
    else:
        aux = aux.sig
        cont += 1

lista1.barrido()
print(f'habia un total de {cont} numeros repetidos')
# contar cuántos elementos repetidos hay entre dos listas;
print('\n')
aux2 = lista1.inicio
for i in range (lista1.que_tamanio()):
    lista1.eliminar(aux2.info)
    print(f'se elimino el numero {aux2.info}')
    aux2=aux2.sig

print(f'\nla lista tiene un total de {lista1.que_tamanio()} numeros')





