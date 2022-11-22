lista=["z", "y", "x", "w"]

print(lista)
def coctel(lista) :
    izquierda = 0
    derecha = len(lista) - 1
    control = True

    print("entro en el while")
    while (izquierda < derecha) and control :
        print(f"cuando izquierda vale {izquierda} es menor que derecha que vale {derecha} y control sea {control}")
        control = False
        print(f"control pasa a ser {control}")
    print("entro en el for")
    for i in range(izquierda, derecha) :
        print(f"ordeno de izquierda a derecha {i}, desde {izquierda} a {derecha}")
        if (lista[i] > lista[i+1]) :
            print(f"{lista[i]}>{lista[i+1]}")
            control = True
            print("control=true")
            lista[i], lista[i+1] = lista[i+1], lista[i]
            print(f"intercambio valores y ahora {lista[i]} está antes que", lista[i+1])
            print(lista)
    derecha -= 1
    print(f"ahora derecha vale {derecha}")

    print("sali del primer bucle")

    for j in range(derecha, izquierda, -1) :
        print("esta es la lista que tengo:", lista)
        print(f"para {j} en rango de{derecha} a {izquierda}, de atrás para adelante")
        if (lista[j] < lista[j-1]) :
            print(f"{lista[j]} es menor que", lista[j-1])
            control = True
            lista[j], lista[j-1] = lista[j-1], lista[j]
            print(f"intercambio {lista[j-1]} por {lista[j]}")
            print(lista)
    izquierda += 1
    print(f"ahora izquierda vale {izquierda}")
    print("salí del segundo bucle")


coctel(lista)
print(lista)