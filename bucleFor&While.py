import math
"""
Tabla de multiplicar:
Pide al usuario un número y muestra su tabla de multiplicar hasta el 10 utilizando un ciclo for anidado.

num= int(input('Ingrese el numero para ver su tabla de multiplicar hasta el 10:\n'))

for i in range(1, 11):
    print(i*num)
"""
"""
Suma de números pares:
Pide al usuario un número y suma todos los números pares desde 1 hasta ese número utilizando un ciclo while.

num= int(input('Ingrese un numero\n'))
#Nuestro iterador inicia en 2 esta variable va a ir mutando con la suma de los numeros
i=2
suma=0
#Mientras num sea mayor o igual que i el ciclo continua
while num >= i:
# Primer ciclo 0+2=2 Segundo ciclo 0+4
    suma+=i
    print(suma)
# Primer ciclo 2+2= 4 segundo ciclo 4+2= 6
    i+=2
#Este ciclo suma en par hasta que alcanzamos el num del usuario

print("La suma de los números pares hasta", num, "es:", suma)

"""
"""
Crea un programa que pida al usuario un número y 
calcule la suma de todos los números desde 1 hasta ese número utilizando un bucle for.

numUser=int(input('Ingrese un numero: '))

for i in range(1, numUser):
    i+=1
    print(i)


"""
"""
Adivinar un número:
Genera un número aleatorio entre 1 y 100. Pide al usuario que adivine el número. 
Utiliza un ciclo while para repetir la solicitud hasta que el usuario acierte. 
Dale pistas al usuario (mayor o menor).


numSecreto= 6
numUser=0

while numSecreto!= numUser:
    numUser = int(input("Ingrese el numero que crea que es el numero secreto: "))
    if numUser<numSecreto:
        print(f'El numero secreto es mayor que {numUser}')
    elif numUser>numSecreto:
        print(f"El numero secreto es menor que {numUser}")


print("Numero correto, muy bien perrita")
"""
"""
Pide al usuario un número y determina si es primo utilizando un ciclo for.

num=int(input('Ingrese un numero y te dire si es primo:\n'))
boolean=True
for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        boolean=False
        break
print(f'El numero {num} es primo {boolean}')
"""
"""
Ejercicio 1
Imprimir los números del 1 al 10.

for i in range(1, 11): 
    print(i)
    
"""

"""
Ejercicio 2
Calcular el factorial de un número.


n= int(input('Escriba el numero para calcular el factorial de este:\n'))

factorial= 1

for i in range(1, n+1):
    factorial*=i

print(f'El factorial de {n} es {factorial}')
"""

"""
Ejercicio 3
Partiendo de una frase imprimir palabra por palabra y un contador de palabras totales.


frase=str(input("Escriba una frase corta: \n"))

contador = 0

for palabra in frase.split(): #Split funcion para separar la frase
    contador+=1
    print(f'{contador} {palabra}')
"""    

"""
Ejercicio 4
Crea un algoritmo para la sucesión de Fibonacci. 
La sucesión de Fibonacci es la siguiente serie:

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

 El bucle for se ejecuta 89 veces (de 0 a 88).
En cada iteración, se imprime el valor de a.
Luego, se actualizan los valores de a y b. a toma el valor de b, y b toma el valor de a + b.

# Inicializamos los primeros dos números de la sucesión
a = 0
b = 1


# Usamos un bucle for para generar la sucesión
for i in range(0,12):
    print(a)
    # Actualizamos los valores de a y b
    a, b= b, a + b
"""

# Ejercicio 5
# Crea un algoritmo que dibuje un árbol dado un número, asumiendo que n >1. Para n = 3:

# *

# **

# ***

# n=3

# for i in  range(n):
#     espacios = " " * (n - i - 1)
#     # Asteriscos para formar el árbol
#     asteriscos = "*" * (2 * i + 1)
#     print(espacios + asteriscos)

"""
Ejercicio 6
Escribir el sumatorio de los números que se quiera hasta ingresar -1.

while True:
    resp=int(input('Ingrese un numero, si quieres terminar el juego ingresar -1\n'))
    
    if -1== resp:
        print('Fin del juego')
        break
"""
"""
Ejercicio 7
Tenemos la pantalla del móvil bloqueada. 
Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. 
Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario 'login correcto'. 
Sino, 'llamando al policía'.


pin= 123

intentos= 0

while intentos<3:
    pinUser = int(input("Ingrese el Pin:\n"))

    if pin == pinUser:
        print("Login Correcto")
        break
    else:
        print("Pin incorrecto")
        intentos+=1

if intentos==3:
        print("Llamando al policía")
"""
"""Ejercicio 8
Calcula la Hipotenusa. Para ello, pide al usuario que te de el valor de los catetos. 
Por si acaso, comprueba que los catetos son mayores a 0. 
Hasta que estos datos sean validados no calcular
.Formula de una hipotenusa de un triangulo a²+b²= c² 


print('Bienvenido\nListo para calcular la Hipotenusa de tu tringulo?\n')

catetoA = 0
catetoB = 0

while catetoA<=0 or catetoB<=0:
    catetoA = int(input("Ingrese el valor del cateto A:\n"))
    catetoB = int(input("Ingrese el valor del cateto B:\n"))

    if catetoA <= 0 or catetoB <= 0:
        print("Los valores de los catetos deben ser mayores a 0. Vuelve a intentarlo.")

#math.sqrt es para calcular la raiz cuadrada
resp= math.sqrt(catetoA**2 + catetoB**2) 

print(f"La Hipotenusa de tu triangulo es {resp:.2f}")
"""

"""
Ejercicio 9
Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos 'SAL' no se apaga.

Esta calculadora funciona de la siguiente manera:

Recogemos los datos A y B
Si operación es 1 calcula la raíz cuadrada de la suma de A y B
Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5



salirCalculadora=False

while not salirCalculadora:

    encenderCalcu=input('Para encender la calculadora escriba "si", para apagarla escriba "SAL":\n').lower()

    if  encenderCalcu=='sal' :
        print('Calculadora apagandose')
        salirCalculadora=True

    elif encenderCalcu=='si':
        opciones = int(
            input(
                "Calculadora encendida!\n Opcion 1: calcular la raíz cuadrada de la suma de A y B\nOpcion 2: calcula A / B. Vigilamos que B no sea 0...\nOpcion 3: calculamos la siguiente fórmula: ( A * B ) / 2.5:\n"
            )
        )
    
        a=int(input("Ingrese el valor de A:\n"))
        b=int(input("Ingrese el valor de B:\n"))

        if opciones==1:
            resp=math.sqrt(a+b)
        elif opciones==2:
            if b==0:
                print('Error b debe ser distinto de 0')
            else:
                resp= a/b
        elif opciones==3:
            resp=(a*b)/2.5
        else:
            print('Esa opcion no esta programada\nVuelve a intentarlo')
            continue

        print(f'Elegiste la opcion {opciones} y el calculo dio {resp}')
    else:
        print('Entrada no válida. Vuelve a intentarlo.')
"""


