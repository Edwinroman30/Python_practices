#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

#5.Convierte dólares a peso con la tasa del banco de reservas (18-01-2021).

taza = 57.00

cantidad_peso = int(input('Introduzca la cantidad a convertir en dolar:'))

peso_dominicano = cantidad_peso * taza

print('Conversión en pesos Dominicanos son: {0}'.format(peso_dominicano))