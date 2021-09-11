"""
  Progrmacion orienda a objetos Conceptos::
  Clases: Una clase es una plantilla que se utiliza para crear objetos que comparten un mismo comportamiento, estado e identidad.
  Objetos: Es una entidad provista de métodos o mensajes a los cuales responde (comportamiento); atributos con valores concretos (estado); y propiedades (identidad)
  Métodos: Es el algoritmo asociado a un objeto que indica la capacidad de lo que éste puede hacer.
"""


class Coche():

    # Esta es la forma de crear el metodo constructor en una clase

    def __init__(self):
        # Para encapsular una variable o metodos se anteponen dos guines bajos self.__variable
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    # Metodo para arrancar

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo = self.__preoperacional()

        if (self.__enMarcha and chequeo):
            return 'El coche esta en marcha'
        elif(self.__enMarcha and chequeo == False):
            return 'Algo anda mal en el coche, no podemos arrancar'
        else:
            return 'El coche esta detenido'

    # Metodo para saber el estado del coche
    def estado(self):
        print(f'El coche tiene {self.__ruedas} ruedas\nUn ancho de {self.__anchoChasis}\nUn largo de {self.__largoChasis}')

    # Metodo para hacer el analisis preoperacional
    def __preoperacional(self):
        print('Realizando el chequeo interno')

        self.gasolina = False
        self.aceite = True
        self.liquidoFreno = True
        self.refrigerante = True

        if(self.gasolina == True and self.aceite == True and self.liquidoFreno == True and self.refrigerante == True):
            return True
        else:
            return False


""" Instancias de la clase Coche """

nissan = Coche()

print(nissan.arrancar(True), '\n')

nissan.estado()


print('***********Un coche mas************\n')

renault = Coche()

print(renault.arrancar(False))

renault.estado()
