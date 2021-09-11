""" 

    Estructura de datos fundamental en Python (Los diccionarios) 
    
    Sintaxis de un diccionario
        Almacenan los datos a traves de una clave:valor
        miDiccionario = {"Alemania":"Berlín", "Francia":"París", "España":"Madrid"}

    Operaciones
        Agregar elementos al diccionario
        miDiccionario["Colombia"] = "Bogotá" 

        Editar elementos al diccionario, se hace reescribiendo el elemento
        miDiccionario["Colombia"] = "Bogotá" 

        Eliminar utilizando la palabra del y seguido el nombre del diccionario con su respectivo elemento
        del miDiccionario["Alemania"]  

    Metodos 
        print(miDiccionario.keys) Nos imprime todas las claves
        print(miDiccionario.values) Nos imprime todas los valores
        print(len(miDiccionario)) Nos imprime la cantidad de elementos del dicionario

"""

miDiccionario = {"Alemania":"Berlín", 77:"Sergio", "España":"Madrid"}
miDiccionario["Colombia"] = ["Bogotá"]
print(miDiccionario)
miDiccionario["Colombia"] = "Bogotá"
print(miDiccionario)
del miDiccionario["Alemania"]
print(len(miDiccionario))

