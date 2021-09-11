""" 
    Las tuplas son listas inmutables, es decir que no se puede modificar mas rapidas en ejecución a comparación de las listas 

    miLista = list(tuplaNom): El metodo list permite convertir una tupla en una lista
    tuplaNom = tuple(miLista): El metodo tuple nos permite convertir una lista en una tupla
    print("Sergio" in miTupla): Validamos que el elemento si este en la tupla
    tuplaNom.count(elemento): Nos permite saber cuantas veces esta el elemento en la tupla
    len(tuplaNom): Nos permite saber la cantidad de elementos que contiene la tupla
    tuplaSingle =("Sergio",): Esta en la forma de crear una tupla unitaria
    index(elemento): Nos devuelve el indice del elemento en la tupla
    miTupla = tuple(miLista): Nos permite convertir una lista en una tupla

    
    Este tipo de tupla se conoce como empaquetado de tupla la cual no lleva parentesis
    tuplaEmpaquetada = "Sergio", 77 , 78, "Liborina"

    Esta es la forma de realizar un desempaquetado de tupla
    tuplaEmpaquetada = ("Sergio", 10 , 1, 1994)
    nombre, dia, mes, year = tuplaEmpaquetada

    print(nombre)
    print(dia)
    print(mes)
    print(year)




"""

tuplaSingle =("Sergio",)

tuplaEmpaquetada = ("Sergio", 10 , 1, 1994)
nombre, dia, mes, year = tuplaEmpaquetada

miLista = ["Sergio", 10, 1, 1994, 1]
tuplaNom = tuple(miLista)

print(len(tuplaSingle))
print(nombre)
print(dia)
print(mes)
print(year)
