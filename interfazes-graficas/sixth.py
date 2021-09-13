from tkinter import *
#Esta libreria nos permite crear modals para cargar archivos, para ver todos los metodos visita https://docs.python.org/3/library/dialog.html?highlight=tkinter#tkinter.filedialog.askopenfilename
from tkinter import filedialog

ventana = Tk()

def abrirFichero():
    #De este modo utilizamos los metodos para cargar los archivos
    fichero = filedialog.askopenfilename(title='Abrir', initialdir="/", filetype=(('Ficheros de excel', '*.xlsx'), ('Ficheros de texto','*.txt'), ('Todos los ficheros', '*.*')))
    print(fichero)

Button(ventana, text='Abrir fichero', command=abrirFichero).pack()


ventana.mainloop()