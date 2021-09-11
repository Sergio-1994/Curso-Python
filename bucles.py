import math

"""
    Tipos de bucles en Python

    **********Bucle for***********

    Esta es la forma de imprimir un elemento de manera horizontal agragando la palabra end=""
        for iterador in "sergio":
            print('hola', end=" ")

    for i in "sergio@gmail.com":
    if (i=="@" or i == "."):
        contador += 1
    if contador == 2:
        print('El email es correcto', contador)
    else:
        print('El email no es correcto')

    range(): Recibe 3 parametros, valor inicial, valor final y de cuanto en cuanto va a realizar el conteo    

    for i in range(0, 15, 2):
        print(f"Valor de la variable {i}")


    valido = False

    email = input('Ingresa tu email\n')

    for i in range(len(email)):
        if (email[i] == "@"):
            valido = True

    if valido:
        print('El email es correcto')
    else:
        print('El email no es correcto')   

    *********Bucle While************

    i=1

    while (i<=10):
        print(f"ejecucion {i}")
        i=i+1
    print('finish')


    edad = int(input('Ingresa la edad\n'))

    while(edad < 0):
        print('La edad no puede ser negativa, torpe')
        edad = int(input('Ingresa la edad nuevamente\n'))

    print(f'Perfecto ya esta tienes {edad} años')


    print('Progama para calcular la raiz cuadrada de un numero')
    num = int(input('Ingresa un numero\n'))
    intentos = 0

    while(num < 0):
        print('No es posible hallar la raiz de un numero negativo')
        if (intentos == 2):
            print('Torpe no te lo dije antes!!! no se puede con un numero negativo, ya perdió')
            break
        num = int(input('Ingresa un numero\n'))
        if(num < 0):
            intentos += 1
    if(intentos < 2):
        solucion = math.sqrt(num)
        print(f'la raiz del numero es {solucion}')


"""

nombre = "Sergio"

for letra in nombre:
    if letra == "S":
        continue #Nos permite omitir esa vuelta de bucle, regresandolo nuevamente.
    print(letra)
