""" 
    Crea un programa que pida introducir una dirección de email por teclado. El programa
    debe imprimir en consola si la dirección de email es correcta o no en función de si esta
    tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
    ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
    o al final, la dirección también será errónea,

"""
sw = False

while(sw == False):

    email = input('Ingrese su direccion de email, por favor\n').lower()

    if(email.count('@') > 0 and email.count('@') < 2 and email.rfind('@') != len(email)-1):
        print('El email es correcto')
        sw = True
    elif(email.count('@') > 1):
        print('El email no puede tener más de una @')
    elif(email.count('@') < 1):
        print('El email no puede estar sin una @')
    elif(email.find('@') == 0):
        print('El @ no puede esta el inicio')
    elif(email.rfind('@')):
        print('El @ no puede estar al final')
