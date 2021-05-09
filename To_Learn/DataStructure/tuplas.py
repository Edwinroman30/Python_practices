#Son inmutables

numbers = (1,23,23)
lista = []

for i in numbers:
    lista.append(i*2)

print(lista)
print(numbers)

#SOlo se pueden colocar o destructurar las cantidades de variables como de indices o len que tenga la tupla.
a,b,c = numbers
print(a+b)
