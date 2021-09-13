from tkinter import *

ventana = Tk()
ventana.title('Examples')
#Recordemos la forma de poner una foto en una interfaz
foto= PhotoImage(file='images/logo.png')
Label(ventana, image=foto).pack()

var_option = IntVar()
check_python = IntVar()
check_java = IntVar()
check_node = IntVar()

def imprime():
    if(var_option.get() == 1):
        etiqueta.config(text="Has elegino masculino")
    else:
        etiqueta.config(text="Has elegino femenino")


def opcionesLenguajes():
    opcionElegida = ""
    if(check_python.get() == 1):
        opcionElegida +="Python"
    if(check_java.get() ==1):
        opcionElegida +="Java"
    if(check_node.get() == 1):
        opcionElegida +="Node"

    text_final.config(text=opcionElegida)

#Al momento de utilizar Radiobutton es necesario asignar una variable y un valor para poder trabajar con ellos
Label(ventana, text="Género").pack()
Radiobutton(ventana, text='Masculino', variable=var_option, value=1, command=lambda:imprime()).pack()
Radiobutton(ventana, text='Femenino', variable=var_option, value=2, command=lambda:imprime()).pack()

etiqueta = Label(ventana)
etiqueta.pack()

#Checkbutton
Label(ventana, text="Lenguajes de programación").pack()
Checkbutton(ventana, text='Python', variable=check_python, onvalue=1, command=lambda:opcionesLenguajes()).pack()
Checkbutton(ventana, text='Java', variable=check_java, onvalue=1, command=lambda:opcionesLenguajes()).pack()
Checkbutton(ventana, text='Node', variable=check_node, onvalue=1, command=lambda:opcionesLenguajes()).pack()

#label para mostrar el sms final
text_final = Label(ventana)
text_final.pack()


ventana.mainloop()