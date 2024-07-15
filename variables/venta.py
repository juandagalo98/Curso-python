
"""
Práctica 02: Calcular precio de venta

Enunciado: dado el valor de venta de 
productos, hallar el IGV (18%) y el 
precio de venta.

Análisis: para la solución de este problema,
se requiere que el usuario ingrese el valor de 
venta del producto y el sistema realice el 
cálculo respectivo para hallar el IGV y el 
precio de venta, para esto use la siguiente 
expresión.

igv = vv * 0.18

pv = vv + igv
"""


#MENSAJE DE LA APLICACION 
print("----Calculadora de venta.----")


#ENTRADA DE DATOS
vv = float(input("ingrese el valor de venta: "))

#OPERACIONES
igv = vv * 0.18
pv = vv + igv

#SALIDA DE DATOS

print('='*29)
print("-----FACTURA DE VENTA-----")
print("El valor de venta es:", vv)
print("El igv es: ", igv)
print("El precio de venta es: ", pv)
print('='*29)


