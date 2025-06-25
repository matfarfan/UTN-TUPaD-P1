#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(0, 101, 1):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
num = input("Ingrese un número entero: ")
digitos = len(num.lstrip("-"))
print(f"El número ingresado tiene {digitos} dígito/s")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
if num1>num2:
    suma=0
    for i in range(num2+1, num1):
        suma += i
    print(f"La suma de los números entre {num1} y {num2} es: {suma}")
elif num2>num1:
    suma=0
    for i in range(num1+1, num2):
        suma += i
    print(f"La suma de los números entre {num2} y {num1} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma=0
while num!=0:
    num=int(input("Ingrese un número a sumar(0 para salir): "))
    suma+=num
print(f"La suma total es {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_aleatorio = random.randint(0, 9)
print(numero_aleatorio)
num=float('-inf')
while num!=numero_aleatorio:
    num=int(input("Adivine el número aleatorio entre 0 y 9: "))

print(f"Excelente! Ha acertado el número aleatorio {num}")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.
for i in range(100, 0-1, -1):
    if i%2==0:
        print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
suma=0
num=int(input("Ingrese el número: "))
for i in range(0, num+1):
    suma+=i
print(f"La suma total es {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
contador=0
pares=0
impares=0
positivos=0
negativos=0
while contador<100:
    num=int(input("Ingrese un número: "))
    contador+=1
    if num%2==0:
        pares+=1
    else:
        impares+=1
    if num>=0:
        positivos+=1
    else:
        negativos+=1
print (f"Números pares: {pares}")
print (f"Números impares: {impares}")
print (f"Números negativos: {negativos}")
print (f"Números positivos: {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
from statistics import mean
mi_lista = []
contador=0
while contador<100:
    num=int(input("Ingrese un número: "))
    mi_lista.append(num)
    contador+=1
print(f"Media de la lista: {mean(mi_lista)}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = int(input("Ingrese un número: "))
invertido = 0
#Dentro del while, se extrae el último dígito del número,se agrega al final del número invertido, 
# y se elimina ese dígito del número original hasta que no queden más.
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print(f"Número invertido: {invertido}")