#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y 
#mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num):
    #Caso base: El factorial de 0 es 1.
    #Esta es la condición que detiene la recursión.
    if num == 0:
        return 1
    else:
        #Caso recursivo
        return num* factorial(num-1)
    

num=int(input("Ingrese un número: "))

#se itera desde 1 hasta el numero ingresado
for i in range (1,num+1):
    print(factorial(i))


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
#Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(num):
    #Caso base para la serie de Fibonacci
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        #Paso recursivo: La suma de los dos números anteriores en la serie
        return fibonacci(num-1) + fibonacci(num-2)
    

num=int(input("Ingrese un número: "))

#se itera desde 0 hasta el numero ingresado
for i in range (0,num+1):
    print(fibonacci(i))


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando 
# la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(n, m):
    #Caso base: Cualquier número elevado a la potencia 0 es 1.
    if m==0:
        return 1
    else:
    #Caso recursivo: n^m = n * n^(m-1)
        return n * potencia(n, m-1)
    

print("Cálculo de potencia con recursividad")
n=int(input("Ingrese la base: "))
m=int(input("Ingrese el exponente: "))
resultado = potencia(n, m)
print(f"{n} elevado a la {m} es: {resultado}")


#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva 
#su representación en binario como una cadena de texto.Cuando representamos un número en binario, 
#lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
#Para convertir un número decimal a binario, se puede seguir este procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario
#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0 
#5 ÷ 2 = 2 resto: 1 
#2 ÷ 2 = 1 resto: 0 
#1 ÷ 2 = 0 resto: 1 
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def decimal_a_binario(decimal):
    #Caso base: Si el número es 0 o 1, su representación binaria es "0" o "1".
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    #La llamada recursiva construye la parte más significativa del binario
    #y luego se le concatena el dígito menos significativo (el resto actual)
    else:
        resto = decimal % 2
        cociente = decimal // 2
        return decimal_a_binario(cociente) + str(resto)
    
decimal=int(input("Ingrese un número entero positivo en base decimal: "))
binario = decimal_a_binario(decimal)
print(f"El numero {decimal} expresado en binario es: {binario}")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
#y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    #Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    #Comparamos el primer y el último carácter
    if palabra[0] == palabra[-1]:
        #Cada vez que la función se llama, trabaja con una versión más corta de la palabra,
        #hasta que queda una sola letra o ninguna. En ese punto, se detiene la recursión y empieza a devolver True hacia atrás.
        return es_palindromo(palabra[1:-1])
    else:
        return False

palabra = input("Ingrese una cadena de texto sin espacios ni tildes: ")
print(es_palindromo(palabra))


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
#devuelva la suma de todos sus dígitos. Restricciones:No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:suma_digitos(1234) → 10 (1 + 2 + 3 + 4) suma_digitos(9) → 9 suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n==0:
        return 0
    else:
        ultimo_digito=n%10
        return ultimo_digito + suma_digitos(n//10)
        
n = int(input("Ingrese un número entero positivo: "))
print(suma_digitos(n))


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
#en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva
#el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
      #Caso base: si no hay más niveles, se necesitan 0 bloques
    if n==0:
        return 0
    else:
        #Sumo los bloques del nivel actual y llamo recursivamente para el nivel superior
        return n+ contar_bloques(n-1)
    
n = int(input("Ingrese un número de los bloques del nivel más bajo: "))
print(contar_bloques(n))


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
#y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
#contar_digito(12233421, 2) → 3 
#contar_digito(5555, 5) → 4 
#contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    #Caso especial: si el número es 0 y el dígito buscado también es 0
    if numero == 0 and digito == 0:
        return 1
    #Caso base general: si el número es 0, pero el dígito no es 0
    elif numero == 0:
        return 0
    else:
        #Extraer el último dígito
        ultimo = numero % 10
        #Comparar el último dígito con el que buscamos
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Entrada del usuario
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (entre 0 y 9): "))
print(f"Cantidad de veces que aparece el dígito {digito}:", contar_digito(numero, digito))