#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número par: "))
if num%2==0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad<12:
    print("Usted pertenece a la categoria Niño/a")
elif edad>=12 and edad<18:
    print("Usted pertenece a la categoria Adolescente")
elif edad>=18 and edad<30:
    print("Usted pertenece a la categoria Adulto/a joven")
elif edad>=30:
    print("Usted pertenece a la categoria Adulto")
else:
    print("Edad incorrecta")
    
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contra = input("Ingrese una contraseña: ")
if 8 <= len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare 
#para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar valores
print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determinar el tipo de sesgo
if media > mediana > moda:
    print("Hay sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("Hay sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("No hay sesgo.")
    
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase=input("Ingrese una frase o palabra: ")
# Verificar si termina en vocal (minúscula o mayúscula)
if frase.lower().endswith(("a", "e", "i", "o", "u")):
    frase += "!"
    print("Resultado:", frase)
else:
    print("Resultado:", frase)
    
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Ingrese su nombre: ")
opcion=int(input("""Eliga la opción que desee ejecutar:  
                 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
                 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
                 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
                 Opción: """))

if opcion==1:
    nombre=nombre.upper()
    print(f"Nombre: {nombre}")
elif opcion==2:
    nombre=nombre.lower()
    print(f"Nombre: {nombre}")
elif opcion==3:
    nombre=nombre.title()
    print(f"Nombre: {nombre}")
else:
    print("La opción ingresada es incorrecta")
    
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las
#siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud=float(input("Ingrese la magnitud del terremoto: "))

if magnitud<3:
    print(f"La magnitud {magnitud} clasifica como: 'Muy leve' (imperceptible)")
elif 3<=magnitud<4:
    print(f"La magnitud {magnitud} clasifica como: 'Leve' (ligeramente perceptible)")
elif 4<=magnitud<5:
    print(f"La magnitud {magnitud} clasifica como:  'Moderado' (sentido por personas, pero generalmente no causa daños)")
elif 5<=magnitud<6:
    print(f"La magnitud {magnitud} clasifica como: 'Fuerte' (puede causar daños en estructuras débiles)")
elif 6<=magnitud<7:
    print(f"La magnitud {magnitud} clasifica como: 'Muy Fuerte' (puede causar daños significativos)")
elif 7<=magnitud:
    print(f"La magnitud {magnitud} clasifica como: 'Extremo' (puede causar graves daños a gran escala)")        

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año                 Estación en el hemisferio norte         Estación en el hemisferio sur
#Desde el 21 de diciembre
#hasta el 20 demarzo (incluidos)            Invierno                              Verano
#
#Desde el 21 de marzo 
#hasta el 20 de junio (incluidos)           Primavera                             Otoño
#
#Desde el 21 de junio 
#hasta el 20 de septiembre (incluidos)      Verano                                Invierno
#
#Desde el 21 de septiembre
#hasta el 20 de diciembre (incluidos)       Otoño                                 Primavera
#
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿En qué mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy?: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    print("Fecha inválida")
    
if hemisferio== "N":
    print(f"Usted se encuentra en: {estacion_norte}")
else:
    print(f"Usted se encuentra en: {estacion_sur}")
