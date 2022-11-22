# Ejercicio 3
# Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como
# estructura extra.

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

    def barrido(self):
        paux=Pila()
        while (not self.pila_vacia()):
            nro = self.desapilar()
            paux.apilar(nro)
        while (not paux.pila_vacia()):
            nro = paux.desapilar()
            print(nro)
            self.apilar(nro)

    def invertir(self):
        paux=Pila()
        while (not self.pila_vacia()):
            nro = self.desapilar()
            print(nro)
            paux.apilar(nro)
        return paux

pdatos=Pila()

elementos=[2,4,5,6,8,7,9,3,1,0,3,9,5,8,2,7,5]

for nro in elementos:
    pdatos.apilar(nro)

print("Pila barrida")
pdatos.barrido()
print("Pila invertida")
pilainvertida=pdatos.invertir()
pilainvertida.barrido()

