#Crear un programa que muestre las letras de la Z (may�scula) a la A (may�scula, descendiendo).

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
i = len(abecedario) - 1

while(i > 0):
    print(abecedario[i].upper())
    i= i - 1
    
print(abecedario[0].upper())
#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233