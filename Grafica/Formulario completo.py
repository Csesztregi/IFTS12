from tkinter import *

ventana = Tk()

miframe = Frame (ventana, width = 1200, height = 600)

miframe.pack()
#tocar boton enviar y se pone el nombre que elijas 1/4
name = StringVar()
#crear cuadro
cuadro = Entry(miframe,textvariable = name ) #tocar boton enviar y se pone el nombre que elijas 2/4 (desde textvariable a = name)
cuadro.grid(row = 0, column = 1)
nombre = Label(miframe,text = "Nombre")
nombre.grid(row = 0, column = 0, sticky="w", padx = 10, pady= 10)

#crear cuadro
cuadro = Entry(miframe)
cuadro.grid(row = 1, column = 1)
nombre = Label(miframe,text = "Apellido")
nombre.grid(row = 1, column = 0, sticky="w", padx = 10, pady= 10)

#crear cuadro
cuadro = Entry(miframe)
cuadro.grid(row = 2, column = 1)
cuadro.config(show = "*")
nombre = Label(miframe,text = "DNI")
nombre.grid(row = 2, column = 0, sticky="w", padx = 10, pady= 10)

#crear cuadro de texto
comentarios = Text(miframe,width = 25, height = 5)
comentarios.grid (row = 3, column = 1)
nombre=Label(miframe, text = "Comentarios")
nombre.grid(row = 3, column = 0, sticky="w", padx = 10, pady= 10)

#ponerle barra de desplazamiento al cuadro de texto
scrollvert = Scrollbar(miframe, command= comentarios.yview)
scrollvert.grid(row = 3, column = 2, sticky = "nsew")
comentarios.config(yscrollcommand=scrollvert.set)
#tocar boton enviar y se pone el nombre que elijas 3/4
def codigoboton ():
    name.set("Nicolas")
#tocar boton enviar y se pone el nombre que elijas 4/4
boton=Button(ventana, text="Enviar",command = codigoboton)
boton.pack()

ventana.mainloop()