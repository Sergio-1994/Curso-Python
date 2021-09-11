#El modulo io es el cual nor permite trabajar con archivos externos
from io import open



# archivoTexto = open("archivo.txt", "w") => esta es la foma de abrir o crear un archivo nuevo open() como primer parametro recibe el nombre del archivo que vamos a crear y el segundo parametro es en el cual le indicamos de que forma vamos a abrir o crear ese archivo, en este caso asignamos w=write por que vamos a escribir en ese archivo

# frase = "Que maravilla ome"

# archivoTexto.write(frase)

# archivoTexto.close()

# archivoTexto = open("archivo.txt", "r")

# texto = archivoTexto.read()

# archivoTexto.close()

# print(texto)


#Esta instruccion nos permite abrir el archivo en modo lectura r equivale a read
# archivoTexto = open("archivo.txt", "r")

# #readlines() este metodo lee el archivo linea a linea y almacena la info en una lista
# lineasTexto = archivoTexto.readlines()

# archivoTexto.close()

# print(lineasTexto)

#Esta es la forma de agregar texto a nuestro archivo con la letra a=append 
# archivoTexto = open("archivo.txt", "a")
# Agregamos el texto nuevo
# archivoTexto.write("Agregando texto nuevo")
# Cerramos el archivo
# archivoTexto.close()
# seek(posicion) es un metodo que nos pemite modificar la posicion del putero o cursor en un archivo
# read(posicion) nos permite indecarle hasta donde va imprimir la información
# archivoTexto = open('archivo.txt', 'r')
# print(archivoTexto.read())
# archivoTexto.seek(14)
# print(archivoTexto.read())
# redline() nos permite ubicarnos al final de la última linea
# archivoTexto = open('archivo.txt', 'r+') r+ nos pemite habilitar dos acciones tanto de lectura como de escritura
#archivoTexto.seek(len(archivoTexto.read())/2) # de esta manera podemos ubicar el cursor en la mitad del texto
#readlines() nos permite traer la información en forma de lista
#writelines(lista) este metodo nos permite escribir texto y recibe como paramtro una lista

archivoTexto = open('archivo.txt', 'r+')

listaTexto = archivoTexto.readlines()

listaTexto[0] = 'Esta linea fue agregada desde fuera del texto'

archivoTexto.seek(0)

archivoTexto.writelines(listaTexto)

archivoTexto.close()

