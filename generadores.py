""" Estructura de generadores que nos pemiten tener un control al momento de leer elementos a diferencia de las funciones extraen valores de una funcion y se almacenan en objetos iterables(que se pueden recorrer)"""

# Funcion tradicional
""" def numerosPares(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*2)
        num += 1
    return lista

print(numerosPares(15)) """

# Sintaxis del generador, este se ejecuta pausadamente con base a la llamada del generador

""" def numerosPares(limite):
    num = 1
    while num < limite:
        yield num*2 #yield me almacena el resultado de la función en un objeto
        num += 1
devuelvePares = numerosPares(10) #Este es el objero generador

print(next(devuelvePares))

print("Mas código")

print(next(devuelvePares))

print("Mas código")

print(next(devuelvePares))

print("Mas código") 


De esta manera larga de construir un for aninado en python

def devuelveCiudades(*ciudades): #El * indica que puede recibir n parametros y que los va a recibir en forma de tupla
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento #Aqui se almacena en un objero iterable el valor de cada subelemento
            

ciudadesDevueltas = devuelveCiudades('Colombia', 'Mexíco', 'Peru', 'Chile', 'Ecuador')

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))



"""



#Esta es la forma de trabajar con bucles anidados, funciona similar cuando leemos elementos de una matriz en java utilizando (yield from)

def devuelveCiudades(*ciudades): #El * indica que puede recibir n parametros y que los va a recibir en forma de tupla
    for elemento in ciudades:
            yield from elemento #Esta es una manera mas resumida que reemplaza el segundo 'for'

ciudadesDevueltas = devuelveCiudades('Colombia', 'Mexíco', 'Peru', 'Chile', 'Ecuador')

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))



