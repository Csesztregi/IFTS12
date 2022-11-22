import random #importa una librería random
import time

listadecienmil=[]

for i in range(5000):
    aux=random.randint(0,100)
    listadecienmil.append(aux)


tiempoinicialBurbuja=time.time()

def burbuja_mejorado(lista) :
 #Método de ordenamiento burbuja mejorado
    i = 0
    control = True
    while (i <= len(lista)-2) and control :
        control = False
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
    i += 1


burbuja_mejorado(listadecienmil)

tiempofinal=time.time()


print(f"El tiempo inicial fue {tiempoinicialBurbuja}, el tiempo final fue {tiempofinal}, la diferencia entre uno y otro es: ", tiempofinal-tiempoinicialBurbuja)

tiempoburbuja=tiempofinal-tiempoinicialBurbuja
