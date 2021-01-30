'''Crear un programa que calcule el descuento a un empleado. si su salario es mayor a 20K el impuesto es de 18%, 
si es mayor 10K el impuesto es 12%, menor de 10K no paga impuesto. Mostrar en pantalla cual es el salario neto a 
cobrar.
'''

#sueldo
sueldo_bruto = float(input('Dígite su sueldo: '))
sueldo_neto = 0
descuento = 0

if(sueldo_bruto >= 20000):
        descuento = sueldo_bruto * 0.18
        sueldo_neto = sueldo_bruto - descuento
else:
    if(sueldo_bruto >= 10000):
        descuento = sueldo_bruto * 0.12
        sueldo_neto = sueldo_bruto - descuento
    else:
         print('Felicidades Usted no paga impuestos :)')
         sueldo_neto = sueldo_bruto


print('Su salario Bruto es: ',round(sueldo_bruto,2))
print('Su salario neto es: ', sueldo_neto)
print('El impuestos aplicado fue de: ',descuento)