#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

#7.	Almacene cuatro notas 90,95,77, 92 y las promedie.
# Al final debe decir su calificación en letras A, B,C,D ó F.

notas = [0,80,0,70]
aveg = 0
nota_final = 0

for x in notas:
    aveg += x

nota_final = aveg//len(notas)

if(nota_final >= 50 and nota_final < 60):
    print('Usted obtuvo una F')
elif(nota_final >= 60 and nota_final < 70):
    print('Usted obtuvo una D')
elif(nota_final >= 70 and nota_final < 80):
    print('Usted obtuvo una C')
elif(nota_final >= 80 and nota_final < 90):
      print('Usted obtuvo una B')
elif(nota_final >= 90 and nota_final < 100):
     print('Usted obtuvo una A')
else:
    print('Super F, :( lamentablemente debe poner mas empeño en esto HIJO.')
