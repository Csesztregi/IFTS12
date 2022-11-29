##        Armar una función que se llame maximoMinimoVendido(datos)
##        y reciba un parámetro datos que serán un diccionario.
##
##        Al invocarla deberá hacer realizar una búsqueda sobre el
##        producto más vendido y el producto menos vendido.
##
##        Finalmente deberá imprimir exactamente:
##
##        Mínimo: {VENTAS} ventas de {NOMBRE_PRODUCTO} en {NOMBRE_CONCESIONARIA}
##        Máximo: {VENTAS} ventas de {NOMBRE_PRODUCTO} en {NOMBRE_CONCESIONARIA}


datos = {
        "autos": ["FIAT Cronos", "Peugeot 208", "Toyota Hilux", "Volkswagen Amarok", "Chevrolet Cruze"],
        "concesionarias": ["Valmotors FIAT", "Kansai Toyota", "Le Meridien Peugeot", "San Jorge", "Dietrich"],
        "registros": [
            {'nro_registro': 1, 'nro_concesionaria': 2, 'nro_producto': 3, 'ventas': 14543},
            {'nro_registro': 2, 'nro_concesionaria': 4, 'nro_producto': 5, 'ventas': 10605},
            {'nro_registro': 3, 'nro_concesionaria': 1, 'nro_producto': 1, 'ventas': 25580},
            {'nro_registro': 4, 'nro_concesionaria': 5, 'nro_producto': 4, 'ventas': 12525},
            {'nro_registro': 5, 'nro_concesionaria': 3, 'nro_producto': 2, 'ventas': 15282}
        ]
    }



def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i] == buscado) :
            posicion = i

    return posicion

def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]


def maximoMinimoVendido(datos):
    maximo= datos["registros"][0]
    minimo= datos["registros"][0]
    for i in datos["registros"]:
        if i["ventas"]> maximo["ventas"]:
            maximo = i
        if i["ventas"]< minimo["ventas"]:
            minimo = i
    print(maximo["ventas"],"ventas de",datos["autos"][maximo["nro_producto"]-1],"en",datos["concesionarias"][maximo["nro_concesionaria"]-1])

    print(minimo["ventas"],"ventas de",datos["autos"][minimo["nro_producto"]-1],"en",datos["concesionarias"][minimo["nro_concesionaria"]-1])



maximoMinimoVendido(datos)