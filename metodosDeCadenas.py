nombre = 'Sergio esta estudiando'

print(nombre.upper()) #Conveinte la cadena en mayuscula
print(nombre.lower()) #Conveinte la cadena en minuscula
print(nombre.capitalize()) #Conveinte la primera letra en mayuscula
print(nombre.count('e')) #Cuenta cuantas veces esta el caracter
print(nombre.find('r')) #Nos imprime la posicion en la cual esta el caracter
print(nombre.isdigit()) #Nos imprime validar si el dato es un digito, devuelve false o true

age = input('Ingrese su edad\n')

while(age.isdigit() == False):
    print(f'Idiota para ti esto {age} es una edad, corrige eso')

    age = input('Ingrese su edad\n')

if (int(age) > 18):
    print('Puedes pasar')
else:
    print('No puedes pasar bb')
