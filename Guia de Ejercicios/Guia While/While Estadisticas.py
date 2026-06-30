#01
contador = 1

while contador <= 10:
    print(contador)
    contador += 1


#02
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1


#03
contador = 1
suma = 0

while contador <= 10:
    suma += contador
    contador += 1

print("La suma es:", suma)


#04
contador = 2
suma = 0

while contador <= 10:
    suma += contador
    contador += 2

print("La suma de los pares es:", suma)


#05
contador = 0
suma = 0

while contador < 5:
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1

promedio = suma / 5

print("Suma:", suma)
print("Promedio:", promedio)


#06
suma = 0
contador = 0

seguir = "s"

while seguir == "s":
    numero = int(input("Ingrese un número: "))

    suma += numero
    contador += 1

    seguir = input("¿Desea continuar? (s/n): ")

promedio = suma / contador

print("Suma:", suma)
print("Promedio:", promedio)


#07
suma_positivos = 0
producto_negativos = 1

seguir = "s"

while seguir == "s":
    numero = int(input("Ingrese un número: "))

    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        producto_negativos *= numero

    seguir = input("¿Desea continuar? (s/n): ")

print("Suma positivos:", suma_positivos)
print("Producto negativos:", producto_negativos)


#08
contador = 0

while contador < 10:
    numero = int(input("Ingrese un número: "))

    if contador == 0:
        maximo = numero
        minimo = numero
    else:
        if numero > maximo:
            maximo = numero

        if numero < minimo:
            minimo = numero

    contador += 1

print("Máximo:", maximo)
print("Mínimo:", minimo)


#Anexo 1
suma = 0
contador = 0

seguir = "s"

while contador < 5 or seguir == "s":

    numero = int(input("Ingrese un número: "))

    suma += numero
    contador += 1

    if contador >= 5:
        seguir = input("¿Desea ingresar otro número? (s/n): ")

promedio = suma / contador

print("Suma:", suma)
print("Promedio:", promedio)


#Anexo 2
suma = 0
contador = 0

seguir = "s"

while contador < 10 and (contador < 5 or seguir == "s"):

    numero = int(input("Ingrese un número: "))

    suma += numero
    contador += 1

    if contador >= 5 and contador < 10:
        seguir = input("¿Desea continuar? (s/n): ")

promedio = suma / contador

print("Suma:", suma)
print("Promedio:", promedio)


#Integrador While
suma_negativos = 0
suma_positivos = 0

contador_negativos = 0
contador_positivos = 0

mayor_positivo = None

total_numeros = 0

seguir = "s"

while seguir == "s":

    numero = int(input("Ingrese un número: "))

    total_numeros += 1

    if numero < 0:
        suma_negativos += numero
        contador_negativos += 1

    elif numero > 0:
        suma_positivos += numero
        contador_positivos += 1

        if mayor_positivo is None or numero > mayor_positivo:
            mayor_positivo = numero

    seguir = input("¿Desea continuar? (s/n): ")

# Promedio positivos
if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
else:
    promedio_positivos = 0

# Porcentaje negativos
if total_numeros > 0:
    porcentaje_negativos = (contador_negativos * 100) / total_numeros
else:
    porcentaje_negativos = 0

print("\nRESULTADOS")
print("Suma negativos:", suma_negativos)
print("Suma positivos:", suma_positivos)
print("Cantidad negativos:", contador_negativos)
print("Promedio positivos:", promedio_positivos)
print("Mayor positivo:", mayor_positivo)
print("Porcentaje negativos:", porcentaje_negativos, "%")


