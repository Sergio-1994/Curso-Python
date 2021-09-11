#Libreria tkinter para trabajar con interfaces graficas
from tkinter import *

#Creando ventanas

raiz = Tk()#Clase que contiene los metodos para crear ventanas
raiz.title('Ventana de pruebas')#Metodo para crear titulos
#raiz.resizable(False, True)#Metodo para restringir ampliar la ventana, recibe 2 parametros que devuelven true o false el primero para width y el segundo para height
raiz.geometry('300x300')#Metodo para modificar el ancho y alto de la ventana
#raiz.iconbitmap('ruta')#metodo para cambiar el icono de la ventana
raiz.config(bg='green')#Metodo para modificar la apariencia de la ventana
raiz.config(bd='20')
raiz.config(relief='sunken')
raiz.config(cursor='hand2')

#Creando Frames con tkinter

miFrame = Frame()
#miFrame.pack(fill='both', expand='true')#A la hora de crear Frame es necesario empaquetarlo con el metodo pack y ademas este metodo recibe parametros geometricos
miFrame.pack()
miFrame.config(bg='white', width='200', height='300')
miFrame.config(bd='35', cursor='pirate')#Nos pone bordes a la ventana y un cursor del tipo que queramos, en fin para trasterar mas con esto visita la documenación https://docs.python.org/3/library/tkinter.html
miFrame.config(relief='ridge')


#Creando los labels
miLabel = Label(raiz, text='Que maravilla ome', fg='red').place(x='100', y='100')#Esta es una manera mas abreviada






raiz.mainloop()#Bucle que muestra la ventana