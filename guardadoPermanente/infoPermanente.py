import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print(f'Se ha creado una persona nueva con el nombre de {self.nombre}')

    def __str__(self):
        return "{}{}{}".format(self.nombre, self.genero, self.edad)


class listaPersonas:

    personas = []

    def __init__(self):

        #Agregamos informacion binaria de esta forma
        listaDePersonas = open('ficheroPersonas', 'ab+')
        #Desplazamos el cursor al principio es decir la posicion 0 esto para en un futuro poder leer la info
        listaDePersonas.seek(0) #Metodo para desplazar el cursor a la posicion que le pasemos en este caso 0x1
        #Realizamos el volcado o carga de la informacion que va a ser almacenada en la lista
        try:
            self.personas = pickle.load(listaDePersonas)
            print('Se cargaron {} personas del fichero externo'.format(len(self.personas)))
        except:
            print('El fichero está vacío')
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    #Metodo para agregar personas a la lista
    def addPersonas(self, persona):
        self.personas.append(persona)
        self.savePersonas()
    #Metodo para imprimir la lista de personas
    def listarPersonas(self):
        for p in self.personas:
            print(p)
    #Metodo para guardar personas en un fichero externo
    def savePersonas(self):
        listaPersonas = open('ficheroPersonas', 'wb')
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del(listaPersonas)
    #Metodo para mostrar el fichero externo
    def showInfo(self):
        print('La informacion de la lista es la siguiente')
        for p in self.personas:
            print(p)




miLista = listaPersonas()
p1 = Persona('Diego ', 'Hombre ', 13)
miLista.addPersonas(p1)
p1 = Persona('Ana ', 'Mujer ', 30)
miLista.addPersonas(p1)
p1 = Persona('Diego ', 'Hombre ', 13)
miLista.addPersonas(p1)
miLista.showInfo()