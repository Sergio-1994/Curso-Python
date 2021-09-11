class Computador():

    def __init__(self, marca, color, precio):
        self.marca = marca
        self.color = color
        self.precio = precio

    def use(self):
        print('Use me only on tables')
    
    def getInfo(self):
        print(f'Marca: {self.marca}\nEl color: {self.color}\nEl precio: {self.precio}')



class Portatil(Computador):

    def __init__(self,memoria, cpu, marca, color, precio):
        super().__init__(marca, color, precio)
        self.memoria = memoria
        self.cpu = cpu

    def use(self):
        print('Use me wherever you want')

    def getInfo(self):
        super().getInfo()
        print(f'Memoria: {self.memoria}\nCpu: {self.cpu}')
           

    

def polimorfismo(obj):
    obj.use()

asus = Portatil(16, 9, 'asus', 'silver gray ', 2500000)




