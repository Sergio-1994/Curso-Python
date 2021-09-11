""" 
    PRINCICIO DE SUSTITUCION, ES CLAVE PARA COMPRENDER LA HERENCIA 

    (ES SIEMPRE UN/A)
    
"""

class Persona():

    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def descripcion(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}\nDirección: {self.direccion}')



class Empleado(Persona):

    def __init__(self, salario, antigüedad, nombre, edad, direccion):
        #Esta es la forma de utilizar el metodo super() para heredar metodos constructores de otras clases
        super().__init__(nombre, edad, direccion)
        self.salario = salario
        self.antigüedad = antigüedad

    
    def descripcion(self):
        #De esta manera también podemos heredar metodos de otras clases
        super().descripcion()
        print(f'Salario: {self.salario}\nAntigüedad: {self.antigüedad}')





pepe = Empleado(18000, 2, 'Pepe', 13, 'Colombia')
pepe.descripcion()
