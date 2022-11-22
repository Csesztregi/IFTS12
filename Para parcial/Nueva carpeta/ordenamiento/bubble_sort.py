lista = [5, 1, 78, 99, 35, 67, 90, 23, 11, 100]

def bubbleSort(array):
    length = len(array)-1
    print(length)

    for i in range(0, length): #realiza las pasadas al algoritmo
        for j in range(0, length): #realiza las comparaciones
            if lista[j] > lista[j+1]:
                aux = lista[j]
                array[j]=array[j+1]
                array[j+1]= aux

    return lista
print("Antes de ordenar:", lista)
bubbleSort(lista)
print("Después de ordenar", bubbleSort(lista))