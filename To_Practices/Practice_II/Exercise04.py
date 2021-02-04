#Studen: Edwin Alberto Roman Seberino.
#Enrollment: 2020-10233

"""
4.	Realizar un programa que reciba por teclado el sueldo de un empleado y le  aplique los cálculos de ISR 
(ver tabla DGII), ARS, y AFP (investigar porcentajes).
"""


#AFP = Administradora de Fonfo de Pensiones. (2.87%)
#ARS = Administradora de Riesgos de Salud. / SFS = Seguro Familiar Social.  (3,04%.)
#ISR = Impuesto Sobre la Renta.


ARS = 0
AFP = 0
ISR = 0

pagoMensualIRS = 0

#Las deducciones de AFP y ARS:

sueldoEmpleado = float(input('Dígite su sueldo: '))

ARS = sueldoEmpleado * 0.0304
AFP = sueldoEmpleado * 0.0287


sueldoEmpleado = sueldoEmpleado - (ARS+AFP)

if ((sueldoEmpleado*12) < 416220.00):
    print('Usted esta exento del pago ISR')
elif((sueldoEmpleado*12) >= 416220.01 and (sueldoEmpleado*12) <= 624329.00):
    
    pagoMensualIRS = (sueldoEmpleado*12) - 416220.01
    pagoMensualIRS = pagoMensualIRS * 0.15
    pagoMensualIRS = pagoMensualIRS / 12
    sueldoEmpleado = sueldoEmpleado - pagoMensualIRS
    
elif((sueldoEmpleado*12) >= 624329.01 and (sueldoEmpleado*12) <= 867123.00):
    
    pagoMensualIRS = (sueldoEmpleado*12) - 624329.01
    pagoMensualIRS = pagoMensualIRS * 0.20
    pagoMensualIRS = pagoMensualIRS + 31216.00
    pagoMensualIRS = pagoMensualIRS / 12
    sueldoEmpleado = sueldoEmpleado - pagoMensualIRS

elif((sueldoEmpleado*12) >= 867123.01):
    
    pagoMensualIRS = (sueldoEmpleado*12) - 867123.01
    pagoMensualIRS = pagoMensualIRS * 0.25
    pagoMensualIRS = pagoMensualIRS + 79776
    pagoMensualIRS = pagoMensualIRS / 12
    sueldoEmpleado = sueldoEmpleado - pagoMensualIRS

else:
    print('ERRO: Usted a ingresado un monto menor de 0.')

print('Descuento por ARS (Administradora de Riesgos de Salud): {}'.format(round(ARS,2)))
print('Descuento por AFP Administradora de Fonfo de Pensiones: {}'.format(round(AFP,2)))
print('Descuento por ISR (Impuesto Sobre la Renta) : {}'.format(round(pagoMensualIRS,2)))

print('Sueldo Neto mensual: {}'.format(round(sueldoEmpleado,2)))
