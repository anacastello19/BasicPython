# Ejercicio 1 :Imprime «Hola Mundo» si a es mayor a b.
# Rellena el código que falta. ¡Adelante!

# a = 50
# b = 10

# # Si a es mayor a b…

# if a > b:
#     print("Hello World")
# else:
#     print('A no es mayor que b')


# Ejercicio 2: Determinar si alguien es menor de edad o no.
# Pide al usuario la edad por pantalla e imprime por pantalla si puede acceder a nuestra fiesta nocturna.

# edad = int(input('Que edad tienes?? '))

# if edad >= 18:
#  print("Puedes acceder a la fiesta")
# else:
#     print('Tu acceso queda denegado por ser menor de edad')


# Ejercicio 3: Haz una calculadora básica que permita realizar
# el cálculo de la hipotenusa de un triángulo,
# vigilando que ningún cateto debe ser menor o igual a cero.
# Si se diera el caso, imprimir «Error» por pantalla.
"""
    Formula de una hipotenusa de un triangulo a²+b²= c² 
a=int(input('Cateto a: escribe el numero: '))
b= int(input("Cateto b: escribe el numero: "))
# c= int(input("Hipotenusa: escribe el numero"))

if (a > 0 and b > 0):
    resp= (a**2) + (b**2) 
    print(f'El resultado es: {resp}' )
else:
    print('Error') 

"""
"""
Ejercicio 4
Haz una calculadora básica pida al usuario dos valores, a y b.

Según la opción que desean, realizar la operación:

"""
consigna = """
                Si operación es 1 entonces debemos ver el resultado de a + b"
                Si operación es 2 entonces debemos ver el resultado de a * b
                Si operación es 3 entonces debemos ver el resultado de a - b
                Si operación es 4 entonces debemos ver el resultado de a / b
                5 si deseas para la calculadora

print(consigna)

operacion = int(input("Que operacion desea realizar? "))

a = int(input("Ingrese en a un numero: "))
b = int(input("Ingrese en b un numero: "))
operacion1= a+b
operacion2 = a * b
operacion3 = a - b
operacion4 = a / b
if operacion == 1:
    print(operacion1)
elif operacion == 2:
    print(operacion2)
elif operacion == 3:
    print(operacion3)
elif operacion == 4:
    print(operacion4)
else: 
    print('Ese numero no tiene operacion por el momento!')
    
"""

"""
Ejercicio 5
Imaginemos que en nuestra tienda hay un carné por puntos y que alguien debe pagar el precio_final_de_compra. 
Si tienes menos de 100 puntos realizaremos un descuento del 10%. 
Si es mayor a 100 y menor a 150 aplicamos un 12%. 
Si tienes 150 un 15% y sino, el resto de los casos de más de 150, un 20%. 
¡Crea la variable puntos y juega con ella!


carnetPuntos= int(input("Buen dia! Cuantos puntos tiene su carnet? "))

compra=100

if carnetPuntos<100:
    descuento= compra-(compra * 0.10)
elif carnetPuntos>100 and carnetPuntos<150:
    descuento = compra-(compra * 0.12)
elif carnetPuntos>150:
    descuento = compra-(compra * 0.20)
else:
    print('Error')
    

print(f"Con ese puntaje su compra le queda en {descuento}")
"""
"""
Ejercicio 6

Calcula sabiendo el valor de una factura cuanto será el precio final 
para el cliente, sabiendo que…

Por norma general, el IVA aplicado es de un 21%. Sin embargo, 
en restaurantes es el 10%.

Calcular el precio final según IVA aplicado. Pista: 
Pide al usuario que tipo de factura es.

"""

"""
Ejercicio 7
Guarda una contraseña como password. 
Crea un sistema de seguridad donde el ordenador muestra un mensaje 'Ordenador bloqueado. 
Contraseña incorrecta.' si el usuario falla la contraseña.
En caso contrario, que muestre por pantalla 'Bienvenid@...'.


password= 'gatitoschiquitos'

print('Ordenador Bloqueado')

passwordUser = str(input("Ingrese la contraseña: "))

if password == passwordUser:
    print('Bienvenid@...')
else: 
    print("Contraseña incorrecta.")
"""

"""
Ejercicio 8
Desarrollar un programa en Python que determine si el año introducido es un año bisiesto o no. Sabiendo que…

Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
El año es un año bisiesto (tiene 366 días).
El año no es un año bisiesto (tiene 365 días).
"""


"""
Ejercicio 9

Partiendo de la tarifa anual (que puede cambiar), 
nos piden que debemos calcular el precio de la tarifa de nuestro polideportivo, 
sabiendo las siguientes condiciones:

Criterio 1: Si es mayor de edad y está trabajando -> Paga el 100%
Criterio 2: Si es menor de edad y está trabajando -> Paga el 95%
Criterio 3: Si es mayor de edad y no está trabajando -> Paga el 75%
Criterio 4: Si es menor de edad y no está trabajando -> Paga el 50%


print('Bienvenido al polideportivo GatitosFit')

edad= int(input("Que edad tienes?\n"))
trabajo= str(input('Trabajas?\n')).lower()

if trabajo == 'si' or trabajo == 'no':
    print('Procesando tarifa...')
else:
    print('Por favor responder si o no')

if edad>18 and trabajo=='si':
    print('Paga el 100% de su tarifa')
elif 18 > edad and trabajo=='si':
    print("Paga el 95% de tarifa")
elif edad>18 and trabajo=='no':
    print("Paga el 75% de tarifa")
else:
    print('8Paga el 50% de tarifa')
"""

"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.

Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.

Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
menu = "Bienvenido a pizzería Bella Napoli\n Ingredientes vegetarianos: Pimiento y tofu.\nIngredientes no vegetarianos: Peperoni, Jamón y Salmón. \nSolo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas."

ingredientes=str(input('Desea que su pizza sea vegetariana?\n')).lower()

ingredientesPlus= str(input('Elegir ingredientes extras\n')).lower()

if ingredientes == "si":
    print(f'Pizza vegetariana con {ingredientesPlus}')

elif ingredientes == "no":
    print(f"Pizza comun con {ingredientesPlus}")
else:
    print('Hubo un error\nResponder la primera pregunta con si o no\n muchas gracias!')
