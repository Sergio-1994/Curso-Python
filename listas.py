""" 
    1. Estructura de datos que nos permiten almacenar gran cantidad de valores, son similares a los arrays en otros lenguajes.
    2. En Python las listas pueden guardar diferente tipo de valores, lo que no ocurre en otros lenguajes.
    3. Se pueden expandir dinámicamente añadiendo nuevos elementos.

    Metodos de las listas:
        append(valor): Este metodo nos permite agregar un elemento al final de la lista
        insert(posicion, valor a agregar): Este metodo permite insertar un elemento indicado la posición en la cual queremos insertalo
        extend([valor1], [valor2]...): Este metodo permite añadir varios elementos a la lista y lo hará al final
        index(elemento): Nos devuelve el indice del elemento en la lista
        remove(elemento): Nos permite eliminar el elemento que le pasemos de una lista
        pop(): Nos permite eliminar el ultimo elemento de la lista
        sort(): Nos permite ordenar la lista

        Nota: En Python es posible sumar o unir listas y multiplicar, ejemplo:

        listas = lista1 + lista2
        lista = [1,2,3,4,5] * 3

        print('elemento a bucar', in nombre de la lista): Ejemplo
        print(77 in listaNom) si el valor existe devuelve true de lo contrario false
    
    Nomenclaturas    
        print(listaNom[:]): Nos permite imprimir todos los elementos de la lista
        print(listaNom[1:3]): Nos permite imprimir los elementos de la lista por trosos 
"""

#Sintaxis de las listas


listaNom = ['Sergio', 'Maria', 'Diego', 'Ninfa', 1]
listaNom[4] = listaNom[4] + 5
print(listaNom)

