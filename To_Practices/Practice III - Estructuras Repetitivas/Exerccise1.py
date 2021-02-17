#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

#Crear un programa que pida n�meros positivos al usuario, y vaya calculando la suma de todos ellos 
#(terminar� cuando se teclea un n�mero negativo o cero).


num = float(input('Ingrese un número: '))
counter = 0

while num > 0:
    counter += num
    num = float(input('Ingrese un número: '))
    

print('El total de los números es: {}'.format(counter))