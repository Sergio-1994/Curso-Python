class Persona():

    
    def __init__(self, name, lastName, age, sex):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.sex = sex
        

    def  getInfo(self):
        print(f'Hola {self.name} {self.lastName} veo que eres {self.sex} y tienes {self.age} años')

    def queTanMayorEres(self):
        if(self.age > 18):
            print('El tiempo ya no riende')
        elif(self.age > 30):
            print('Pongase las pilas')
        elif(self.age > 40):
            print('Ya debes estar realizado')
        elif(self.age > 60):
            print('Relagese')
        else:
            print('Eres muy joven hijo')

i = 0

while(i !=2):

    op= int(input('***BIENVENIDO***\nCuentanos que deseas hacer\n1.Ingresar datos\n2.Salir\n'))

    if(op == 1):    
        name = input('Ingrese su nombre, por favor\n')
        lastName = input('Ingrese su apellido, por favor\n')
        age = int(input('Ingrese su edad, por favor\n'))
        sex = input('Ingrese su sexo, por favor\n')
            
        sergio = Persona(name, lastName, age, sex)
        sergio.getInfo()
        sergio.queTanMayorEres()
    else:
        i=2
        print('Programa finalizado...')

        
