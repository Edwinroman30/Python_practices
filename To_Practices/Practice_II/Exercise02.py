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
option = int(input('\n Program:> '))
valueToConvert = 0

def Cel_Fahr():
    Gcelsius = float(input('Introduzca los grados Celsius: ')) 
    Gfahrenheit = (Gcelsius * (9/5) + 32)
    print('Grados Fahrenheit: {0}'.format(Gfahrenheit))

def Dollar_Peso():
    Dollar = float(input('Ingrese su cantidad de dolar: '))
    Peso = Dollar * 56.90
    print('Pesos Dominicanos: {}'.format(round(Peso,2)))

def Meter_feet():
    Meter = float(input('Ingrese la cantidad en metro: '))
    Feet = Meter * 3.281
    print('Cantidad a pie: {}'.format(round(Feet,2)))


if(option == 1):
   Cel_Fahr()
elif(option == 2):
    Dollar_Peso()
elif(option == 3):
    Meter_feet()
elif(option == 4):
     print('Se ha denido la ejecución del programa.')
else:
     print('Su selección esta fuera de RANGO'.upper())