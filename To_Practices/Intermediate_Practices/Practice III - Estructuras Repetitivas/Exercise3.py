#Crear un programa que muestre los primeros 10 n�meros pares a partir del producto de (10 x 10).


i = 1
counter = 0

while i in range((10*10)):
    if((i % 2) == 0):
        print(i)
        counter = counter + 1
    if counter == 10:
        break
    i= i + 1

#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233