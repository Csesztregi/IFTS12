def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i] == buscado) :
            posicion = i

    return posicion

def binaria(lista, buscado) :
    """ Metodo de busqueda binaria """
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1

    while (primero <= ultimo) and (posicion == -1) :
        medio = (primero + ultimo) // 2

        if (lista[medio] == buscado) :
            posicion = medio
        else :
            if (buscado < lista[medio]) :
                ultimo = medio - 1
            else :
                primero = medio + 1

    return posicion


def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def seleccion(lista) :
    """Método de ordenamiento selección"""
    for i in range(0, len(lista)-1) :
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j] < lista[minimo]) :
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

def insercion(lista) :
    """Método de ordenamiento inserción"""
    for i in range(1, len(lista)+1) :
        k = i-1
        while (k > 0) and (lista[k] < lista[k-1]) :
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1

def quicksort(lista, primero, ultimo) :
    """Metodo de ordenamiento quicksort"""
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo

    while (izquierda < derecha) :
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
            izquierda += 1

        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
            derecha -= 1

        if (izquierda < derecha) :
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    if (lista[pivote] < lista[izquierda]) :
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    if (primero < izquierda) :
        quicksort(lista, primero, izquierda-1)

    if (ultimo > izquierda) :
        quicksort(lista, izquierda+1, ultimo)


def mergesort(lista) :
    """Metodo de ordenamiento mergesort"""
    if (len(lista) <= 1) :
        return lista
    else :
        medio = len(lista) // 2
        izquierda = []

        for i in range(0, medio) :
            izquierda.append(lista[i])

        derecha = []

        for i in range(medio, len(lista)) :
            derecha.append(lista[i])

        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)

        if (izquierda[medio-1] <= derecha[0]) :
            izquierda += derecha

            return izquierda

        resultado = merge(izquierda, derecha)

        return resultado

def merge(izquierda, derecha) :
    """Funcion para mezclar listas"""
    lista_mezclada = []

    while (len(izquierda) > 0) and (len(derecha) > 0) :
        if (izquierda[0] < derecha[0]) :
            lista_mezclada.append(izquierda.pop(0))
        else :
            lista_mezclada.append(derecha.pop(0))

    if (len(izquierda) > 0) :
        lista_mezclada += izquierda

    if (len(derecha) > 0) :
        lista_mezclada += derecha

    return lista_mezclada
