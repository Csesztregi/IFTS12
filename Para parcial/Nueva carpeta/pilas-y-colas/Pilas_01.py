# Ejercicio 1
# Determinar el número de ocurrencias de un determinado elemento en una pila.

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

pdatos = Pila()
elementos = [5,7,6,8,2,4,3,4,9,4,2,4,9,6,1,3,4,9,4,1,3,8,7,6,1,4,3,5,5,6,8,4,5,4,6]

# ingreso los elementos a la pila
for nro in elementos :
	pdatos.apilar(nro)

# solicito al usuario que ingrese un nro
dato = int(input('Ingrese un nro a contabilizar: '))

contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while (not pdatos.pila_vacia()) :
    nro = pdatos.desapilar()
    contador[nro] += 1

print('Se encontraron ', contador[dato], ' ocurrencias del nro ', dato)
