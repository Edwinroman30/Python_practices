#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

#1.	Crear un programa que solicite al usuario un número indeterminado de números 
# (mientras se tecleen números que no sean cero). Al salir el programa  debe dar en pantalla el total de números
#  ingresados y la suma de ellos. 


#Pedir un numero (QUE NO SEAN O)
#Al salir de debe decir:
    # total de numeros.
    # Suma de ellos.

suma_num = 0
counter= 0
num = 1

try:

    while (num != 0):
        num = float(input('Dígite un número: '))
        counter = counter + 1
        suma_num += num 

    print('La suma de los numeros es: {} y la cantidad de número ingresados es: {}'.format(round(suma_num),counter))
except:
    print('ERROR: Usted esta intentando de ingresar un caracter no valido ;)')
