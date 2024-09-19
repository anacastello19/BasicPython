# # Lista de cadenas de texto
# frutas = ["manzana", "banana", "pera"]

# # Para mostrar la lista
# print(frutas)
# # Llamamos un elemento
# print(frutas[0])

# # Cambiamos el valor
# frutas[2]='uva'
# print(frutas)

# # Agregamos un elemento al final de la lista fruta con append
# frutas.append('Frutilla')
# print(frutas)

# # Agregamos un elemento con el puesto que elegimos
# frutas.insert(2,'Kiwi')
# print(frutas)

# # Elimina el primer elemento con un valor específico.
# frutas.remove('Kiwi')
# print(frutas)

# # Elimina y devuelve el elemento en una posición específica (si no se especifica, elimina el último).
# ultElem= frutas.pop()
# print('El elemento eliminado fue: '+ultElem)
# print(frutas)

# # Ordena los elementos de la lista de forma ascendente.
# abc=['g','d','a','e','b', 'c']
# abc.sort()
# print(abc)

# # Invierte el orden de los elementos.
# frutas.reverse()
# print(frutas)

# # Slicing:

# # Puedes extraer porciones de una lista utilizando slicing
# # Obtener los primeros 3 elementos

# print(abc[:3])

# # Obtener los elementos del índice 2 al 4 (excluyendo el 5)
# print(abc[2:5])


# """
# Crea una lista:

# Crea una lista de números del 1 al 10.
# Crea una lista mixta con números, cadenas y booleanos.
# """
# num=[1,2,3,4,5,6,7,8,9,10]

# mix=[1,5,9,'max','min',True, False]

# Crea una lista con los nombres de tus 5 películas favoritas.
pelis=['Rocky', 'Bastardos sin gloria', 'Hambre', 'Harry Potter', 'Shrek']

# Agrega una nueva película al final de la lista.
pelis.append('La Sirenita')

# Imprime la segunda película de la lista.
print(pelis[1])

# Ordena la lista alfabéticamente.
pelis.sort()
print(pelis)

# Invierte el orden de la lista.
pelis.reverse()
print(pelis)

# Crea una lista con los números del 1 al 10 y luego extrae los números pares.
num=[]

for i in range(1,11):
    num.append(i)
print(num)

num_par=[]
for numeros in num:
    # % = es el restro de la divicion
    if numeros % 2 ==0:
        num_par.append(numeros)
print(num_par)

# Crea una lista de listas para representar una matriz de 3x3.
matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Acceder a un elemento (5)
#matriz [fila][columna]
elemento= matriz[1][1]
print(f'Buscando elemento ... {elemento}')

# Crea una matriz dinamica
columnas= 4
filas=3

#Creamos una matriz vacia
matriz=[]

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(i* columnas + j +1)
    matriz.append(fila)
print(matriz)

# Escribe un programa que pida al usuario 5 números, 
# los guarde en una lista y luego calcule el promedio.

# num=[]

# while len(num)<5:
#     numeros= int(input('Ingrese un numero:\n'))
#     num.append(numeros)

# print(num)



# Ejercicio 2

# Pedir la puntuación media de las personas para cada asignatura de un curso a
# partir de un número de personas. Deberás iniciar los cursos para después añadir
# el número de alumnos y pedir las puntuaciones media. Ejemplo del programa resultado:

# Insertar la lista de los nombres de las asignaturas del instituto BigBayData.com

# El usuario introduce: Python,SQL,Hadoop,Js,Html,Css,Swift

# Genial. Ahora introduce las puntuaciones uno por uno en Python:

# Introducimos las puntuaciones de los alumnos por cada alumno para cada curso.

# Resultado de las evaluaciones este año:

# [Python, 12 alumnos. Nota media: 7.6, Suspensos: 2]

# [SQL, 12 alumnos. Nota media: 6.9, Suspensos: 1]


"""

Ejercicio 3
Imagina un sistema de nombres donde queremos identificar el nombre más común. Para ello primero pide al usuario que inserte nombres. Utiliza la estructura do-while.

Introduce los nombres... (-1 para terminar)

carmen,julia,juan,carmen,carmen,julia

carmen: 3,julia: 2,juan: 1

Ejercicio 4
Utiliza el ejercicio anterior y modifícalo para, una vez se añaden los usuarios, se eliminen los duplicados.

Ejercicio 5
Calcular la tabla de multiplicar de los 20 primeros números dado un número. La lista, según su posición, almacenará el resultado de la multiplicación.

Ejercicio 6
Haz un programa que inicialice una lista con los primeros 10 números primos. Después, ordenalos de mayor a menor.

Ejercicio 7
Simula una cesta de la compra. Después, una vez tengas la lista de la compra, elimina el último elemento. Después, invierte los elementos de la lista y muestra qué queda de resultado.

Pista: Utiliza la función pop()

Ejercicio 8
Añade las estadísticas de los primeros 10 pokemon en nuestra pokedex. Fíjate qué estadísticas quieres para todos los pokemon. Aquí algunas sugerencias: nombre, ataque, hp, defensa, velocidad, at_Esp, def_Esp

Después, utiliza la lista como una pokedex para consultarlo.

Ejercicio 9
Imagina construir un sistema de planning de vuelos de un aeropuerto cercano. Crea una planificación donde dentro contiene, por día de la semana, horario, compañia, duracion_estimada, tipo_avion. Utiliza una lista dentro de otra lista.

PD: Después de llenar los datos necesitarás ofrecer al usuario ver la información.

Ejercicio 10
Haz un sistema de ordenamiento de ayudas para tu comunidad. La idea es que insertes todos los emails que quieras para, aleatoriamente, ofrecer N ayudas. El objetivo es tener un sistema justo de ayudas para repartir entre la ciudadanía que se postula. Una vez lo tengas, desarrolla un sistema de envío automático por correo. ¿Serás capaz?
"""
