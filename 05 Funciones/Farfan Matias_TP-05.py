#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
print(list(range(0,101,4)))


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
lista=[1, 2, 3, 4, 5]
print(f"Penúltimo elemento: {lista[3]}")
print(f"Penúltimo elemento utilizando indexing: {lista[-2]}")


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
lista = []
lista.append("nombre")
lista.append("apellido")
lista.append("edad")
print(lista)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)
#Respuesta: en el programa dada la lista numeros realiza lo siguiente: primero con la función max busca el valor máximo en la lista (22), 
# luego aplica la función remove y elimina dicho dato para posteriormente imprimir por pantalla la lista actualizada.


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista = list(range(10, 31, 5))
print(f"Primeros dos elementos: {lista[0]}, {lista[1]}")

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "kangoo"
autos[2] = "ka"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.
dobles =[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)