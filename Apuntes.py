"""INTRODUCCION A PYTHON """

#La funcion print es la primera que aprendemos ya que la utilizamos para imprimir nuestro primer "hola mundo"

#Primeras funciones para la introduccion

print("Hola Mundo") #La función print() en Python se utiliza para mostrar información en la consola).


#-----------------------------------------------

mensaje = "Hola Mundo"  #definimos una variable 

print(mensaje)


#Entrada de datos

mensaje = input("Ingrese su nombre: ") #la funcion input en Python se utiliza para obtener datos de entrada del usuario. Cuando se llama a input(), el programa se detiene y espera a que el usuario escriba algo en la consola 


"""01-VARIABLES Y DATOS"""




#Variable: una variable en Python es un contenedor que se utiliza para almacenar datos o valores


#Python es dinamico y permite modificar las variables


variable = "Hola Mundo" #Ejemplo de variable 


""" 
-----------------NUMEROS EN PYTHON------------------------

En python utilizamos los operadores los operadores ( +, -, *, /, %, (2**potencia),)

EJEMPLO CON * MULTIPLICACION 

>>> num = 10
>>> num
>>> 10
>>>
>>> num * 2
>>> 20

------------------TIPOS DE DATOS NUMERICOS -------------------

Enteros (int): Representan números enteros positivos o negativos, sin decimales.
EJ:

entero = 42

Números flotante (float): Representan números reales con parte decimal.

flotante = 3.14

Números complejos (complex): Representan números complejos, con una parte real y una imaginaria.

complejo = 1 + 2j



FUNCION "type" nos indica que tipo de datos contiene la variable

>>> num = 10
>>> num
>>> 10
>>> type(num)
 <class 'float'>

"""

#Ahora almacenaremos los datos que se ingresan con input en una variable

mensaje = input("Ingrese un texto: ")      #------>Esta es nuestra primera aplicacion en consola con una variable, un input y un print.
print(mensaje)


#Conversion de tipos 

n1 = input("Ingrese el primer numero: ")
n2 = input("Ingrese el segundo numero: ")


""" en esta aplicacion los datos de las variables se asigga el tipo 'str' y
    no suma los datos sino que los juntara

    EJ:

     n1 = input("Ingrese el primer numero: ")
     n2 = input("Ingrese el segundo numero: ")

     suma = n1 + n2 

     print("la suma es: ", suma)

     Ingrese el primer numero: 5
     Ingrese el segundo numero: 5
     la suma es:  55   #-----> EL RESULTADO NO ES DE UNA SUMA

"""

#Convertir Variable de str a int;


n1 = int(n1)     #-------> asignamos la funcion int (de tipo entero) para convertir los datos de la variable de str a int
n2 = int(n2)

suma = n1 + n2 
print("la suma es: ", suma)


"""
AHORA SI NOS RESULVE LA OPERACION Y NOS DEVUELVE EL TIPO DE DATO CORRECTO: 

Ingrese un texto: suma 
suma 
Ingrese el primer numero: 5
Ingrese el segundo numero: 5
la suma es:  10  -------------> RESULTADO DE LA OPERACION 

"""

#02-OPERADORES LOGICOS Y CONDICIONALES 


"""
En Python, los tipos de datos booleanos (bool) representan valores lógicos y solo pueden tener
uno de dos valores posibles: True o False. Estos valores se utilizan para realizar operaciones lógicas
y de comparación, y son fundamentales para el control de flujo en los programas,
como en las estructuras condicionales (if, elif, else) y los bucles (while, for).

"""