TP_0

# =============================
# E/S DE DATOS
# =============================

# a) Se debe mostrar por consola (pantalla) un mensaje como el siguiente "Esto funciona 
# de maravilla".

print("Esto funciona de maravilla")

# b) Ingresar un dato por input y luego mostrarlo por consola.

dato = input("Ingresá un dato: ")
print(dato)

# c) Ingresar nombre y edad por input, luego mostrarlos concatenados.  
# Ejemplo: "Usted se llama Pedro y tiene 65 años."   

nombre = input("Ingrese su nombre ")
edad = input("Ingrese su edad ")
print("Usted se llama " + nombre + " y tiene " + edad + " años.")

# d) Ingresar dos números por input, transformarlos a enteros (int) y Sumarlos.  
# Mostar el resulto por consola.  
# Ejemplo: "la suma es 750". 

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))
print("La suma es", num1 + num2)

# e) Ingresar dos números por input, transformarlos a enteros (int), realizar la operación 
# aritmética de división, pero para obtener y mostrar el resto (operador módulo) entre 
# el dividendo (numero_uno) y el divisor (numero_dos).  
# Ejemplo: "El resto es 0."  

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese otro numero "))
print("El resto es", num1 % num2)

# f) Ingresar un importe por input, transformarlo a número real (float), luego mostrar el 
# importe ingresado, el 10% del mismo, y el importe con el incremento calculado. 

importe = float(input("Ingrese un importe: "))
aumento = importe * 0.10
print("Importe:", importe)
print("10%:", aumento)
print("Total:", importe + aumento)

# g) Ingresar un importe por input, transformarlo a número real (float), luego mostrar el 
# importe ingresado, el 25% del mismo, y el importe con el descuento calculado. 


importe = float(input("Ingrese un importe: "))
descuento = importe * 0.25
print("Importe:", importe)
print("25%:", descuento)
print("Total:", importe - descuento)


# =============================
# CONDICIONALES (IF / ELIF / ELSE)
# =============================

# a) Al ingresar un número por input, evaluar si el mismo es 1980, si es así mostrar el 
# mensaje "Este año se creó del videojuego Pac-Man" por consola. 

año = int(input("Ingrese un año: "))
if año == 1980:
    print("Este año se creó el videojuego Pac-Man")

# b) Al ingresar una edad por input se debe informar por consola si la persona es mayor 
# de edad, caso contrario no informar nada. 

edad = int(input("Ingrese una edad: "))
if edad >= 18:
    print("Mayor de edad")

# c) Al ingresar una edad por input se debe informar si la persona es mayor de edad, 
# caso contrario, informar que es un menor de edad.  

edad = int(input("Ingrese una edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# d) Al ingresar una edad por input, se debe informar si la persona es adolescente, edad 
# entre 13 y 17 años (inclusive), caso contrario, no informar nada. 

edad = int(input("Ingrese una edad: "))
if 13 <= edad <= 17:
    print("Adolescente")

# e) Al ingresar una edad por input, solo se debe informar si la persona NO es 
# adolescente. 

edad = int(input("Ingrese una edad: "))
if not (13 <= edad <= 17):
    print("No es adolescente")

# f) Al ingresar una edad por input, se debe informar si la persona es mayor de edad 
# (mayor a 17 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años). 

edad = int(input("Ingrese una edad: "))
if edad > 17:
    print("Mayor de edad")
elif 13 <= edad <= 17:
    print("Adolescente")
else:
    print("Niño")


# =============================
# MATCH
# =============================

# a) Ingresar un mes por input e informar por consola:  
# Si es Enero: "Que comiences bien el año!"  
# Si es Marzo: "A clases!"  
# Si es Julio: "Se vienen las vacaciones!"  
# Si es Diciembre: "Felices fiesta!" 

mes = input("Ingrese un mes: ").lower()
match mes:
    case "enero":
        print("Que comiences bien el año!")
    case "marzo":
        print("A clases!")
    case "julio":
        print("Se vienen las vacaciones!")
    case "diciembre":
        print("Felices fiestas!")

# b) Ingresar un mes por input e informar por consola: 
# Si estamos en Invierno: "Abrigate que hace frio."  
# Si aún no llego el Invierno: "Falta para el invierno."  
# Si ya paso el Invierno: "Ya pasamos el frio, ahora calor!"  
# Aclaración: Se debe tomar a Julio y Agosto como los meses de invierno.  

mes = input("Ingrese un mes: ").lower()
match mes:
    case "julio" | "agosto":
        print("Abrigate que hace frio.")
    case "enero" | "febrero" | "marzo" | "abril" | "mayo" | "junio":
        print("Falta para el invierno.")
    case _:
        print("Ya pasamos el frio, ahora calor!")

# c) Ingresar un mes por input e informar:  
# Si es Febrero: " Este mes no tiene más de 29 días."  
# Si no es Febrero: "Este mes tiene 30 o más días." 

mes = input("Ingrese un mes: ").lower()
match mes:
    case "febrero":
        print("Este mes no tiene más de 29 días.")
    case _:
        print("Este mes tiene 30 o más días.")

# d) Ingresar un mes por input e informar:  
# Si tiene 28 días.  
# Si tiene 30 días.  
# Si tiene 31 días.  

mes = input("Ingrese un mes: ").lower()
match mes:
    case "abril" | "junio" | "septiembre" | "noviembre":
        print("30 días")
    case "febrero":
        print("28 días")
    case _:
        print("31 días")

# e) Ingresar un numero entero que represente una hora del día e informar:  
# Si está entre las 7 y las 11 : "Es de mañana."

hora = int(input("Ingrese una hora: "))
match hora:
    case h if 7 <= h <= 11:
        print("Es de mañana")

# f) Ingresar un número entero que represente una hora del día e informar:  
# Si está entre las 7 y las 11 : "Es de mañana." 
# Si está entre las 12 y las 19 : "Es de tarde." 
# Si está entre las 20 y las 23 o entre las 0 y las 6 : "Es de noche." 
# Si no está entre las 0 y las 23 : "la hora no existe."

hora = int(input("Ingrese una hora: "))
match hora:
    case h if 7 <= h <= 11:
        print("Mañana")
    case h if 12 <= h <= 19:
        print("Tarde")
    case h if (20 <= h <= 23) or (0 <= h <= 6):
        print("Noche")
    case _:
        print("Hora inválida")

# g) Ingresar dos números por input, transformarlos a entero (int).  
# Luego seleccionar la opción:  
# Sumar 
# Restar 
# Multiplicar 
# Dividir (numero_uno / numero_dos)  
# Mostar el resulto por consola. 
# Ejemplo: "la suma es 750" 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
op = input("Ingrese la operación : ")
match op:
    case "suma":
        print(num1 + num2)
    case "resta":
        print(num1 - num2)
    case "multiplicacion":
        print(num1 * num2)
    case "division":
        print(num1 / num2)


# =============================
# FOR
# =============================

# a) Mostrar por consola 10 repeticiones con números de manera ascendente, desde el 1 
# hasta el 10.

for i in range(1, 11):
    print(i)

# b) Mostrar por consola 10 repeticiones con números de manera descendente, desde el 
# 10 hasta el 1. 

for i in range(10, 0, -1):
    print(i)

# c) Ingresar por input un número, convertirlo a entero (int), y repetir el mensaje "Hola 
# UTN FRA" tantas veces como el número ingresado.  
num = int(input("Ingrese un número: "))
for i in range(num):
    print("Hola UTN FRA")

# d) Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos 
# los números pares desde 1 hasta el número ingresado.

num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)

# e) Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos 
#los números impares desde 1 hasta el número ingresado.
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)

# f) Ingresar por input un número mayor a 0 (cero), y mostrar ese número por consola. 
# Repetir la operación una y otra vez, hasta que ingresemos  (cero), en ese caso 
#finalizar la ejecución del programa.

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    print(num)


# =============================
# WHILE
# =============================

# a) Mostrar por consola 10 repeticiones con números de manera ascendente, desde el 1 
# hasta el 10.

i = 1
while i <= 10:
    print(i)
    i += 1

# b) Mostrar por consola 10 repeticiones con números de manera descendente, desde el 
# 10 hasta el 1.

i = 10
while i >= 1:
    print(i)
    i -= 1

# c) Ingresar un número por input, y mostrarlo por consola. El número ingresado debe 
#estar comprendido entre 0 y 9 inclusive, caso contrario volver a pedirlo hasta que el 
# número ingresado esté dentro de ese rango. 

num = int(input("Ingrese un número: "))
while num < 0 or num > 9:
    num = int(input("Error. Reingresá: "))
print(num)

# d) Ingresar una letra por input, validar que la misma sea „F‟ o „M‟, caso contrario 
# volver a pedirla. Una vez validado el ingreso de la letra, mostrar por consola: 
# Si la letra ingresada es „F‟: “FEMERNINO” 
# Si la letra ingresa es „M‟: “MASCULINO”.

letra = input("Ingrese una letra (F o M): ").upper()
while letra != "F" and letra != "M":
    letra = input("Error. Reingresá: ").upper()
if letra == "F":
    print("FEMENINO")
else:
    print("MASCULINO")

# e) Ingresar cinco (5) números por input, e informar por consola la suma y el promedio 
# de los números ingresados.

suma = 0
i = 0
while i < 5:
    num = int(input("Ingrese un número: "))
    suma += num
    i += 1
print("Suma:", suma)
print("Promedio:", suma / 5)

# f) Ingresar tantos números por input como el usuario desee, e informar por consola la 
# suma y el promedio de los números ingresados.

suma = 0
cont = 0
num = int(input("Ingrese un número: "))
while num != 0:
    suma += num
    cont += 1
    num = int(input("Ingrese otro número: "))
if cont > 0:
    print("Suma:", suma)
    print("Promedio:", suma / cont)

# g) Ingresar tantos números por input como el usuario desee, e informar por consola la 
#suma de los números positivos,  y la multiplicación de los números negativos.

suma_pos = 0
mult_neg = 1
hay_neg = False
num = int(input("Ingrese un número: "))
while num != 0:
    if num > 0:
        suma_pos += num
    else:
        mult_neg *= num
        hay_neg = True
    num = int(input("Ingrese otro número: "))
print("Suma positivos:", suma_pos)
if hay_neg:
    print("Multiplicación negativos:", mult_neg)
