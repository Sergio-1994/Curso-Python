from tkinter import *

ventana = Tk()#Creamos la ventana
ventana.geometry('800x600')#Le damos un tamaño del
ventana.title('Hello from Python')#Damos un titulo
ventana.config(bg='green')#Le damos un color de fondo
ventana.config(relief='sunken')#Borde
ventana.config(bd='10',pady=100)#tamaño de borde

#Nota los elementos que creemos dentro de la ventana es necesarios enpaquetarlos con el metodo pack() para poderlos mostrar

#Creamos un frame
miFrame = Frame(ventana, width='400', height='500', padx=15, pady=15)#Recordemos pasar como parametro la ventana que creamos anteriormente para que el frame se muestre con base a ella
#miFrame.config(bg='orange')
miFrame.pack()#Empaquetamos el frame

myName = StringVar()#De esta manera asignamos una cadena de caracteres a la variable

#Creamos un input o cuadro de texto
#De nuevo pasamos al constructor de los input el Frame al cual va a pertenecer
inputName = Entry(miFrame, textvariable=myName)#Asociamos la variable myName al input
inputName.grid(row=0, column=1, padx=5, pady=5)#De esta manera podemos crear un grid en python para ubicar los elementos

inputLastName = Entry(miFrame)
inputLastName.grid(row=1, column=1, padx=5, pady=5)

inputAge = Entry(miFrame)
inputAge.grid(row=2, column=1, padx=5, pady=5)

inputUser = Entry(miFrame)
inputUser.grid(row=3, column=1, padx=5, pady=5)

inputPass = Entry(miFrame)
inputPass.grid(row=4, column=1, padx=5, pady=5)
inputPass.config(show='*')#De esta forma ocultamos la contraseña en una interfaz

#De esta manera creamos el textarea
inputComment = Text(miFrame, width=15, height=5)
inputComment.grid(row=5, column=1, padx=5, pady=5)
#De este modo damos un scroll vertical al textarea
scrollVertical = Scrollbar(miFrame, command=inputComment.yview)
scrollVertical.grid(row=5, column=2, sticky='nsew')

inputComment.config(yscrollcommand=scrollVertical.set)

#Creamos un label
labelName = Label(miFrame, text='Nombre:')
labelName.grid(row=0, column=0, sticky='nw', padx=5, pady=5)

labelLastName = Label(miFrame, text='Last Name:')
labelLastName.grid(row=1, column=0, sticky='nw', padx=5, pady=5)

labelAge = Label(miFrame, text='Age:')
labelAge.grid(row=2, column=0, sticky='nw', padx=5, pady=5)

labelUser = Label(miFrame, text='User:')
labelUser.grid(row=3, column=0, sticky='nw', padx=5, pady=5)

labelPass = Label(miFrame, text='Password:')
labelPass.grid(row=4, column=0, sticky='nw', padx=5, pady=5)


#Creamos una textarea o caja de texto
labelComment = Label(miFrame, text='Comment:')
labelComment.grid(row=5, column=0, sticky='nw', padx=5, pady=5)

def codigoButton():
    myName.set('Sergio')


#Creamos un button 
buttonEnviar = Button(ventana, text='Enviar', command=codigoButton)#Al dar click llamamos asociamos la funcion codigoButton con el atributo command
buttonEnviar.pack()






ventana.mainloop()#Ejecutamos el metodo que contiene un bucle el cual nos muestra la ventana