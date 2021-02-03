#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

"""
2.	Crear un programa que presente un menú con las siguientes opciones 
o	Convertir grados a Celsius a Fahrenheit 
o	Convertir dólar a pesos.
o	Convertir metros a pies.
o	Salir 
Cada vez que finalice una de estas acciones debe regresar al menú. El programa  solo finalizará cuando el
usuario elija la opción salir. 

"""

print('Bienvenido al programa 002: \n 1)Convertir grados a Celsius a Fahrenheit. \n 2)Convertir dólar a pesos. \n 3)Convertir metros a pies. \n 4)SALIR')
option = int(input('\n Program:\> '))


if(option == 1):
    print('Something one')
elif(option == 2):
     print('Something two')
elif(option == 3):
     print('Something two')
elif(option == 4):
     print('Something two')
else:
     print('Su selección esta fuera de RANGO'.upper())