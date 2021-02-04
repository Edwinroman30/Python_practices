#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

"""
3.	Hacer un programa que genere las tablas de multiplicar de los números  múltiplos de 5 que hay entre 1 y 500.
"""

i=0

for i in range(500):
    i= i + 1
    if((i%5) == 0):
        print(i)
