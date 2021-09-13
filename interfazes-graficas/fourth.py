from tkinter import *
#libreria para trabajar con modals
from tkinter import messagebox

ventana = Tk()
photo= PhotoImage(file='images/logo.png')
Label(ventana, image=photo).pack()

#Funciones 

def modals():
    #Este metodo nos permite crear los modales
    messagebox.showinfo('Procesador de Sergio', 'Procesador de textos 2021 version 01')

def avisoLicencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GNU')

def cerrarApp():
    valor= messagebox.askokcancel("Salir", '¿Deseas salir de la aplicación?')
    if(valor==True):
        ventana.destroy()

def cerrarDoc():
    valor= messagebox.askretrycancel('Reintentar', 'No es posible cerrar doc bloqueado')
    if(valor==False):
        ventana.destroy()

#De esta manera creamos una barra de menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu, height=300)

#De este modo asociamos las opciones que apareceran en el menú correspondiente
archivo_menu = Menu(barra_menu, tearoff=0)
#De este modo agregamos submenus al elemento de la barra de menú
archivo_menu.add_command(label='Nuevo')
archivo_menu.add_command(label='Guardar')
archivo_menu.add_command(label='Guardar como')
#Metodo para crear una linea de separación
archivo_menu.add_separator()
archivo_menu.add_command(label='Cerrar', command=cerrarDoc)
archivo_menu.add_command(label='Salir', command= cerrarApp)


archivo_edicion = Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label='Copiar')
archivo_edicion.add_command(label='Cortar')
archivo_edicion.add_command(label='Pegar')

archivo_herramientas = Menu(barra_menu, tearoff=0)

archivo_ayuda = Menu(barra_menu, tearoff=0)
archivo_ayuda.add_command(label='Licencia', command=avisoLicencia)
archivo_ayuda.add_command(label='Acerca de', command=modals)

#De este modo añadimos ya el elemento a la barra del menú
barra_menu.add_cascade(label='Archivo', menu=archivo_menu)
barra_menu.add_cascade(label='Edicion', menu=archivo_edicion)
barra_menu.add_cascade(label='Herramientas', menu=archivo_herramientas)
barra_menu.add_cascade(label='Ayuda', menu=archivo_ayuda)


ventana.mainloop()