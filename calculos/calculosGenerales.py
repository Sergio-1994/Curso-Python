
def sumar(num1, num2):
    print(num1 + num2)

def restar(num1, num2):
    return (num1 - num2)

def multiplicar(num1, num2):
    return (num1 * num2)

def dividir(num1, num2):
    if(num1 < 0 or num2 < 0):
        print('Oye no podemos dividir por cero!!')
    else:
        return (num1 / num2)

def potencia(base, exponente):
    print(f'El numero {base} elevado a {exponente} es igual a {base**exponente}')

def redondear(num):
    print(f'El numero redondeado es igual a {round(num)}')