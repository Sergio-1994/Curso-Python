""" 
  La identación es Python es muy importante para el funcionamiento del programa

"""

""" notaAlumno = float(input('Ingrese el valor de la nota obtenida, please\n'))

def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Reprobado"
    return valoracion

print(evaluacion(notaAlumno)) """


""" print("Verificación de acceso")

edad = int(input('Ingre su edad, please\n'))

if (edad < 18):
    print('No pudes pasar')
elif (edad > 100):
    print('Edad incorrecta')
else:
    print('Puedes pasar') 
"""

salarioPresidente = float(input('Ingrese el salario del presidente\n'))
print('Salario presidente: ', salarioPresidente)

salarioDirector = float(input('Ingrese el salario del director\n'))
print('Salario director: ', salarioDirector)

salarioJefe = float(input('Ingrese el salario del jefe\n'))
print('Salario jefe: ', salarioJefe)

salarioAdministrativo = float(input('Ingrese el salario administrativo\n'))
print('Salario asministrativo: ', salarioAdministrativo)

if (salarioAdministrativo<salarioJefe<salarioDirector<salarioPresidente):
    print('Todo anda bien')
else:
    print('Algo anda mal')