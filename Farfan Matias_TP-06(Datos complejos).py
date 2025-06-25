#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
agenda = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

#Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

#Verificar si existe
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")



#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingresá una frase: ")

#Separar en palabras
palabras = frase.lower().split()

#Obtener palabras únicas
palabras_unicas = set(palabras)

#Contar frecuencia de palabras
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

#Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", recuento)



#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
notas_alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = input(f"Ingresá 3 notas separadas por coma para {nombre}: ")
    notas_tupla = tuple(map(float, notas.split(",")))
    notas_alumnos[nombre] = notas_tupla

print("\nPromedios:")
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")



#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

#Aprobó ambos parciales
ambos = set()
for estudiante in parcial1:
    if estudiante in parcial2:
        ambos.add(estudiante)

#Aprobó solo uno
solo_uno = set()
for estudiante in parcial1:
    if estudiante not in parcial2:
        solo_uno.add(estudiante)
for estudiante in parcial2:
    if estudiante not in parcial1:
        solo_uno.add(estudiante)

#Aprobó al menos uno
al_menos_uno = set()
for estudiante in parcial1:
    al_menos_uno.add(estudiante)
for estudiante in parcial2:
    al_menos_uno.add(estudiante)

print("Aprobó ambos parciales:", ambos)
print("Aprobó solo uno de los dos:", solo_uno)
print("Aprobó al menos uno:", al_menos_uno)



#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock_productos = {
    "arroz": 10,
    "fideos": 5,
    "aceite": 3
}

#Ingreso del producto a consultar
producto = input("Ingresá el nombre del producto: ").lower()

#Verificamos si existe en el diccionario
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    
    #Consultamos si desea agregar unidades
    agregar = input(f"¿Querés agregar unidades a {producto}? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no existe en el stock.")
    agregar_nuevo = input(f"¿Querés agregar {producto} como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        nuevo_stock = int(input("¿Cuántas unidades querés ingresar?: "))
        stock_productos[producto] = nuevo_stock
        print(f"{producto} fue agregado con {nuevo_stock} unidades.")

#Mostrar estado final del stock
print("\n📦 Stock final:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant} unidades")


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación",
    ("viernes", "18:00"): "Gimnasio"
}

#Consultar actividad
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad agendada: {agenda[clave]}")
else:
    print("No hay actividad agendada en ese día y hora.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Invertir el diccionario: capital → país
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario invertido:")
print(capitales)