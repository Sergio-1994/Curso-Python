#Esta es la biblioteca 'pickle' que nos permitira serializar
import pickle 


# names = ['Wilson', 'Ninfa', 'Edwin', 'Deisy', 'Sergio', 'Valentina', 'Diego']

# ficheroBinario = open('listaNombres', 'wb') #wb en este caso nos permitira escribir binarios write binari

#Esta es la forma de ingresar la informacion que queremos volcar, dump() es el metodo que nos pemite hacer el volcado y recibe dos parametros el primero es la informacion que queremos guardar y el segundo es el nombre del fichero en el cual lo vamos a guardar
# pickle.dump(names, ficheroBinario)

#Cerramos el archivo
# ficheroBinario.close()

#Eliminamos el archivo en caso de quererlo 
# del(ficheroBinario)

#luego de crear el archivo binario vamos a intentar leerlo 

Nombres = open('listaNombres', 'rb') # rb read binari nos permitira los permisos para leer info binaria
lista = pickle.load(Nombres) # el metodo load() nos permitira traer o cagar esa info que estaba en forma binaria
print(lista)