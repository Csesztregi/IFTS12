#
#
# Ejercicio 2
# Reemplazar todas las ocurrencias de un determinado elemento en una pila.
#
#

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

    def reemplazar(self, nroelegido, cambio):
        pdatosreemplazados=Pila()
        while (not self.pila_vacia()) :
            nro = self.desapilar()
            if (nro == nroelegido):
                nro = cambio
                pdatosreemplazados.apilar(nro)
            else:
                pdatosreemplazados.apilar(nro)

        while (not pdatosreemplazados.pila_vacia()):
            nro = pdatosreemplazados.desapilar()
            print(nro)


    def barrido(self):
        paux=Pila()
        while (not self.pila_vacia()):
            nro = self.desapilar()
            print(nro)
            paux.apilar(nro)
        while (not paux.pila_vacia()):
            nro = paux.desapilar()
            self.apilar(nro)


#Creo una pila pdatos
pdatos=Pila()

#Creo una lista de elementos
elementos=[1,5,3,8,7,4,6,3,7,3,2,4,5,3]

#Ingreso los elementos a la pila
for nro in elementos :
	pdatos.apilar(nro)

pdatos.barrido()

#Pido al usuario un numero a reemplazar
elegido = int(input('Ingrese un nro a reemplazar: '))
cambio= int(input('Ingrese un reemplazo'))

pdatos.reemplazar(elegido, cambio)

pdatos.barrido()


