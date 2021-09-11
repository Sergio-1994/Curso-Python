
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


class Furgonetas(Vehiculos):
        
    def cargar(self, cargar):
        self.cargado = cargar

        if(self.cargar):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'






class Motos(Vehiculos):
    
    stun = ""

    def picando(self):
        self.stun = 'Picando la dt'
    
    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelera: {self.acelera}\nFrena: {self.frena}\nEsta {self.stun}')


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando= True




miMoto = Motos('YAMAHA', 2021)

miMoto.arrancar()
miMoto.picando()
miMoto.estado()


print()

miFurgoneta = Furgonetas('nissan', 2020)

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.cargar(True))


class BicicletaElectrica(VElectricos,Vehiculos):
    
    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nFrena: {self.frena}\n Cargando Energia: {self.cargando}')






print()

miBici = BicicletaElectrica('ws', 2021)
miBici.arrancar()
miBici.cargarEnergia()
miBici.estado()



       







