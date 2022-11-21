from datetime import date

class parcial(object) :
    """Clase Parcial"""
    materia, nota, fecha = None, None, None

    def __init__(self, materia, nota, fecha) :
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

class nodoLista(object) :
    """Clase nodo lista"""
    nombre,apellido,legajo,parciales, sig = None, None, None, [], None

class Lista(object) :
    """Clase Lista enlazada simple"""
    def __init__(self) :
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

    def insertar(self, nombre,apellido,legajo,parciales) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.nombre = nombre
        nodo.apellido = apellido
        nodo.legajo = legajo
        nodo.parciales = parciales

        if (self.inicio is None) or (self.inicio.apellido > apellido) :
            nodo.sig = self.inicio
            self.inicio = nodo
        else :
            ant = self.inicio # anterior
            act = self.inicio.sig # actual

            while (act is not None and act.apellido < apellido) :
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

    def tamanio(self) :
        """Devuelve el número de elementos en la lista"""
        return self.tamanio

    def barrido(self) :
        """Realiza un barrido de la lista mostrando los valores"""
        aux = self.inicio

        while (aux is not None) :
            print (aux.apellido,aux.nombre,aux.legajo)
            aux = aux.sig

    def buscar_anio(self, anio_a) :
        aux = self.inicio

        while (aux is not None) :

            for parcial in aux.parciales :
                anio_b = parcial.fecha.year

                if (anio_a == anio_b) :
                    print(aux.apellido, aux.nombre, aux.legajo)
                    print(parcial.fecha, parcial.materia, parcial.nota)


            aux = aux.sig

    def insertara(self, nombre,apellido,legajo,parciales) :
        """Inserta el dato a la lista"""
        nodo = nodoLista()
        nodo.nombre = nombre
        nodo.apellido = apellido
        nodo.legajo = legajo
        nodo.parciales = parciales

        if (self.inicio is None) or (self.inicio.apellido > apellido) :
            nodo.sig = self.inicio
            self.inicio = nodo
        else :
            ant = self.inicio # anterior
            act = self.inicio.sig # actual

            while (act is not None and act.apellido < apellido) :
                ant = ant.sig
                act = act.sig

            nodo.sig = act
            ant.sig = nodo

        self.tamanio += 1



    def promedio (self):
        aux = self.inicio
        while (aux is not None):
            cant = 0
            nota = 0
            for i in aux.parciales:
                cant+=1
                nota+= i.nota
            if ((nota/cant)>8):
                print("el promedio de",aux.nombre,"es de:",nota/cant)
            aux=aux.sig

    def conl(self):
        aux = self.inicio
        while (aux is not None):
            for i in aux.apellido[0]:
                if i == "L":
                    print (aux.apellido,aux.nombre,aux.legajo)



            aux = aux.sig

    def promediotodos (self):
        aux = self.inicio
        while (aux is not None):
            cant = 0
            nota = 0
            for i in aux.parciales:
                cant+=1
                nota+= i.nota
            print("el promedio de",aux.nombre,"es de:",nota/cant)
            aux=aux.sig


lista1 = Lista()
lista1.insertara('Mariano', 'LPérez', 1, [parcial("filosofia", 1, date(2020, 12, 3)), parcial("sociologia", 1, date(2020, 11, 5)), parcial("matematicas",1, date(2022, 9, 22))])
lista1.insertara('Gisela', 'Montserrat', 2, [parcial("sociales", 9, date(2025, 12, 3)), parcial("pedagogia", 8, date(2024, 11, 5)), parcial("base de datos",9, date(2022, 9, 22))])
lista1.insertara('Amanda', 'Arepa', 3, [parcial("sociales", 5, date(2025, 12, 3)), parcial("pedagogia", 8, date(2024, 11, 5)), parcial("base de datos",7, date(2022, 9, 22))])

print("alumnos ordenados alfabeticamente por apellido")
lista1.barrido()
print("\n")
lista1.promedio()
print("\nLos alumnos que su apellido empiezan con L son:")
lista1.conl()
print("\nPromedios: ")
lista1.promediotodos()



