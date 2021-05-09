listas = ['Edwin',18,'202010233@itla.edu.do',1,True]

print(listas[2:-1])

listas.append('Something wild')
listas.insert(1,'Does not exist')

#print(listas.pop(1))
print(listas)

#listas.remove('1')

"""if(1 in listas):
    print('Python is dangerous')
else:
    print('Python may causes some problems but give it a chance')"""

nombre = ['Edwin','Braily','George']
edad = [18,16,23]

#Recorrer multiples LISTA O ARRAYS A LA VEZ
for n,e in zip(nombre,edad):
    print('Su nombre es {} y su edad es de {}'.format(n,e))

for n in reversed(nombre):
    print(n)
