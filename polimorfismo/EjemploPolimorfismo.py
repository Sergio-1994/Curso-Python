class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas')



class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas')


class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')



""" 
    Esta es la forma de utilizar el polimorfismo 

    def nombre del metodo(objeto o instancia):
    objeto.nombre del metodo que deseo llamar()

    instancia = Clase()
    metodo(instancia)

"""
def polimorfismo(objeto):
    objeto.desplazamiento()

miVehiculo = Coche()
polimorfismo(miVehiculo)