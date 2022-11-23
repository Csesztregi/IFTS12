from tkinter import * #importar libreria

raiz = Tk() #declarar la variable
raiz.title("ventanita del amor") #titulo de ventana
raiz.resizable (True,True) #tamanio de ventana
raiz.iconbitmap("microbe.ico") #cambiar la imagen de la ventana principal
raiz.config(bg="black") #color de fondo

#Frame y pack() es para definir el ancho y la altura de la ventana
miframe = Frame(raiz, width=500, height=400)
miframe.pack()

#escribir dentro del cuadro y definir donde aparecera el texto, color, fuente y tamanio

milabel = Label(miframe, text="Holaaaaa",fg = "red",font = ("Comic San MS", 18))
milabel.place(x=200, y=200)

#cuadro para ingresar texto

cuadro=Entry(miframe)
cuadro.place(x=110, y=10)
label = Label(miframe, text="Nombre:",fg = "black",font = ("Comic San MS", 9))
label.place(x=50, y=10)



raiz.mainloop() #abrir la ventana

#si guardo con extension .pyw puedo abrir el programa sin la consola.
