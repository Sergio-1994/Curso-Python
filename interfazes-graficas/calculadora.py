from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('300x400')
miFrame = Frame(ventana)
miFrame.pack()

operacion = ""
resultado = 0

#-------Pantalla fila 1-----------------
numIngresado = StringVar()

pantalla= Entry(miFrame, textvariable=numIngresado)
#pantalla.insert(0, 0)
pantalla.grid(row=1, column=1, padx=3, pady=10, columnspan=4)
pantalla.config(bg='black', fg='#03f943', justify='right')

#-------Pulsaciones teclado--------------------------------
def btnPulsado(num):
    global operacion
    if(operacion !=""):
        numIngresado.set(num)
        operacion=""
    else:
        numIngresado.set(numIngresado.get()+num)

def btnClean():
    global resultado
    resultado=0
    numIngresado.set("")

#------------SUMA-----------------------------------
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion = "suma"
    numIngresado.set(resultado)

#------------RESTA----------------------------------
def resta(num):
    global operacion
    global resultado
    resultado -= int(num)
    operacion = "resta"
    numIngresado.set(resultado)
#------------MULTIPLICACIÓN----------------------------------
def multiplicacion(num):
    global operacion
    global resultado
    resultado*=int(num)
    operacion = "multiplicacion"
    numIngresado.set(resultado)

#--------------El Resultado-----------------------

def elResultado():
    global resultado
    global operacion
    numIngresado.set(resultado+int(numIngresado.get()))

    resultado=0
    



#-------Fila numero 2--------------------------------
btn7= Button(miFrame, text='%', width=3)
btn7.grid(row=2, column=1)
btn8= Button(miFrame, text='CE', width=3, command= lambda:btnClean())
btn8.grid(row=2, column=2)
btn9= Button(miFrame, text='C', width=3, command= lambda:btnClean())
btn9.grid(row=2, column=3)
btnDiv= Button(miFrame, text='DEL', width=3)
btnDiv.grid(row=2, column=4)



#-------Fila numero 3------------------
btn7= Button(miFrame, text='7', width=3, command= lambda:btnPulsado('7'))
btn7.grid(row=3, column=1)
btn8= Button(miFrame, text='8', width=3, command= lambda:btnPulsado('8'))
btn8.grid(row=3, column=2)
btn9= Button(miFrame, text='9', width=3, command= lambda:btnPulsado('9'))
btn9.grid(row=3, column=3)
btnDiv= Button(miFrame, text='/', width=3)
btnDiv.grid(row=3, column=4)

#-------Fila numero 4------------------
btn4= Button(miFrame, text='4', width=3, command= lambda:btnPulsado('4'))
btn4.grid(row=4, column=1)
btn5= Button(miFrame, text='5', width=3, command= lambda:btnPulsado('5'))
btn5.grid(row=4, column=2)
btn6= Button(miFrame, text='6', width=3, command= lambda:btnPulsado('6'))
btn6.grid(row=4, column=3)
btnMul= Button(miFrame, text='x', width=3, command= lambda:multiplicacion(numIngresado.get()))
btnMul.grid(row=4, column=4)

#-------Fila numero 5------------------
btn1= Button(miFrame, text='1', width=3, command= lambda:btnPulsado('1'))
btn1.grid(row=5, column=1)
btn2= Button(miFrame, text='2', width=3, command= lambda:btnPulsado('2'))
btn2.grid(row=5, column=2)
btn3= Button(miFrame, text='3', width=3, command= lambda:btnPulsado('3'))
btn3.grid(row=5, column=3)
btnRes= Button(miFrame, text='-', width=3, command= lambda:resta(numIngresado.get()))
btnRes.grid(row=5, column=4)

#-------Fila numero 6------------------
btn0= Button(miFrame, text='0', width=3, command= lambda:btnPulsado('0'))
btn0.grid(row=6, column=1)
btnComa= Button(miFrame, text=',', width=3, command= lambda:btnPulsado(','))
btnComa.grid(row=6, column=2)
btnIgual= Button(miFrame, text='=', width=3, command= lambda:elResultado())
btnIgual.grid(row=6, column=3)
btnSuma= Button(miFrame, text='+', width=3, command= lambda:suma(numIngresado.get()))
btnSuma.grid(row=6, column=4)


#Bucle para mostrar la ventana
ventana.mainloop()