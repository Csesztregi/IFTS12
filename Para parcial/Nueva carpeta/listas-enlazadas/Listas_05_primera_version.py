##    Ejercicio 5 Implementar los algoritmos necesarios para resolver las siguientes tareas:
##    a). concatenar dos listas, una atrás de la otra;
##    b). concatenar dos listas en una sola omitiendo los datos repetidos y
##    manteniendo su orden;
##    c). contar cuántos elementos repetidos hay entre dos listas;
##    d). eliminar todos los nodos de una lista de a uno a la vez mostrando su
##    contenido.


class nodoLista(object) :
    """Clase nodo lista"""
    info, sig, valor  = None, None, None

class Lista(object) :
    """Clase Lista enlazada simple"""
    def __init__(self) :
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

    def insertar(self, posicion, valor) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.info = posicion
        nodo.valor=valor

        if (self.inicio is None) or (self.inicio.info > posicion) :
            nodo.sig = self.inicio
            self.inicio = nodo
        else :
            ant = self.inicio # anterior
            act = self.inicio.sig # actual

            while (act is not None and act.info < posicion) :
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

        return nodo.valor

    def buscar(self, buscado) :
        """Devuelve la dirección del elemento buscado"""
        aux = self.inicio
        resultado=0
        while (aux is not None):
            if (aux.valor == buscado) :
                resultado+=1
            aux = aux.sig

        return resultado

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
            print(aux.valor)
            aux = aux.sig


    def insertar_sin_repetir(self, lista, posicion):
        nodo = self.inicio
        while (nodo is not None) :
            elemento=lista.eliminar(posicion)
            if (self.buscar(elemento) == 0):
                self.insertar(posicion,elemento)
            nodo = nodo.sig


##    a). concatenar dos listas, una atrás de la otra;
unalista=Lista()
otralista=Lista()

nros=[2,4,8,0,2,4,6,8,0]

for nro in nros:
    unalista.insertar(1, nro)

masnros=[3,5,7,9,1,3,5,7]

for nro in masnros:
    otralista.insertar(2, nro)


granlista=Lista()


# Quitar todos los elementos de la primer lista
nodo = unalista.inicio

while (nodo is not None) :
    elemento=unalista.eliminar(1)
    granlista.insertar(1,elemento)
    nodo = nodo.sig


#Quitar todos los elementos de la segunda lista
nodo = otralista.inicio

while (nodo is not None) :
    elemento=otralista.eliminar(2)
    granlista.insertar(2,elemento)
    nodo = nodo.sig



##    b). concatenar dos listas en una sola omitiendo los datos repetidos y
##    manteniendo su orden;



nros=[1,5,7,7,9,4,8,20,2,4,6,8,0]

for nro in nros:
    unalista.insertar(1, nro)

masnros=[3,5,7,9,7,8,1,3,5,7]

for nro in masnros:
    otralista.insertar(2, nro)

otragranlista=Lista()

unaprueba=Lista()



##Insertar los elementos de la primer lista

nodo = unalista.inicio
while (nodo is not None) :
    elemento=unalista.eliminar(1)
    if (otragranlista.buscar(elemento) == 0):
        otragranlista.insertar(1,elemento)
    nodo = nodo.sig


##Insertar los elementos de la segunda lista

nodo = otralista.inicio
while (nodo is not None) :
    elemento=otralista.eliminar(2)
    if (otragranlista.buscar(elemento) == 0):
        otragranlista.insertar(2,elemento)
    nodo = nodo.sig


otragranlista.barrido()


##    c). contar cuántos elementos repetidos hay entre dos listas;

lista1=Lista()
lista2=Lista()
lista3=Lista()
nros=[1,3,3,5]

for nro in nros:
    lista1.insertar(1,nro)

nros2=[2,5,5,5]

for nro in nros2:
    lista2.insertar(2,nro)


# Quitar todos los elementos de la primer lista
nodo = lista1.inicio

while (nodo is not None) :
    elemento=lista1.eliminar(1)
    lista3.insertar(1,elemento)
    nodo = nodo.sig


#Quitar todos los elementos de la segunda lista
nodo = lista2.inicio

while (nodo is not None) :
    elemento=lista2.eliminar(2)
    lista3.insertar(2,elemento)
    nodo = nodo.sig

print('Lista ultimo ejercicio')


print('Elementos repetidos entre dos listas')
lista4=Lista()
nodo = lista3.inicio
repetidos=0

while (nodo is not None) :
    elemento=lista3.eliminar(2)
    lista4.insertar(2,elemento)
    if (lista4.buscar(elemento) > 0):
        repetidos+=1
    nodo = nodo.sig

print(f'Los repetidos entre las dos listas son: {repetidos}')


##    d). eliminar todos los nodos de una lista de a uno a la vez mostrando su
##    contenido.

lista4.barrido()
