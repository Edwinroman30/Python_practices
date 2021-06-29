#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

#1.	Almacenar en una variable el nombre de una persona y al final muestre en consola el mensaje: “Bienvenido [NOMBRE COMPLETO]”.

personName = "Juan Pepe"

print('Bienvenido a Python:, Sr.', personName)


#Crear un programa que permita cargar 5 numeros por teclado y los muestre.

lista = []

for i in range(5):
    lista.append(int(input("Inserte un numero:")))

i = 0

for i in range(5):
    print('Num => {}'.format(lista[i]))
