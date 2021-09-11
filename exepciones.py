import math

""" def divide(num1, num2):
    try:
        return f'Result of the division is = {num1 / num2}'
    except ZeroDivisionError:
        print('Cannot divide by zero')


while True:

    try:
        num1 = int(input('Enter the firts number, please\n'))
        num2 = int(input('Enter the second number, please\n'))
        break
    except ValueError:
        print('Enter a value valid, try again')

operation = int(input('Enter the operation\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n'))

if(operation == 4):
    print(divide(num1, num2))


print('The program continue its execution...') """

# AN EXAMPLE MORE

""" def divide():
    try:
        num1 = int(input('Enter the firts number, please\n'))
        num2 = int(input('Enter the second number, please\n'))

        print (f'Result of the division is = {num1 / num2}')
    except ValueError:
        print('The value entered is incorrect')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    finally:
        print('calculation finished')

#Calling the function
divide() """


# Function to calculate an age using (raise) that allows creating your own exceptions
# def getAge(age):
#     if age < 0:
#         raise mipro('There is no negative age')
#     if age < 20:
#         print('You are very young')
#     elif age < 40:
#         print('You are young')
#     elif age < 65:
#         print('You are adult')
#     elif age < 100:
#         print('beware')

# getAge(-18)

# An example more

def getSqueareRoot(num):
    if num < 0:
        raise ValueError('Number cannot be negative')#This is the way to create your own exceptions
    else:
        return math.sqrt(num)


num = int(input('Enter a number, please\n'))
try:
    print(getSqueareRoot(num))
except ValueError as negativeNumber:
    print(negativeNumber)

print('Program finished...')
