#El primer paso para serialzar es importar la libreria pickle
import pickle

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelera: {self.acelera}\nFrena: {self.frena}')

coche1 = Vehiculos('suzuki', 2021)
coche2 = Vehiculos('mazda', 2015)
coche3 = Vehiculos('nissan', 2021)

coches= [coche1, coche2, coche3]

fichero = open('los coches', 'wb')#Creamos el fichero en donde se va almacenar la info
pickle.dump(coches, fichero)#volcamos la info

fichero.close()
del(fichero)

abrirFichero= open('los coches', 'rb')#Abrimos el fichero
cargarFichero = pickle.load(abrirFichero)#Traemos la info del fichero
abrirFichero.close()

for coche in cargarFichero:
    print(coche.estado())