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
numero = int(input("Ingrese un número: "))

contador = 0

while contador <= numero:
    print(contador)
    contador += 1


#04
numero = int(input("Ingrese un número: "))

contador = 0

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1


#05
suma = 0
contador = 0

while contador < 10:
    numero = int(input("Ingrese un número (0 para finalizar): "))

    if numero == 0:
        break

    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("Suma:", suma)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números.")


#06
contador = 1

while contador <= 10:
    if contador % 3 == 0:
        print(contador)

    contador += 1


#07
contador = 1

while contador <= 50:
    if contador % 2 == 0:
        print(contador)

    contador += 1


#08
numero = int(input("Ingrese un número: "))

fila = 1

while fila <= numero:
    columna = 1

    while columna <= fila:
        print(columna, end="")
        columna += 1

    print()
    fila += 1


#09
numero = int(input("Ingrese un número: "))

contador = 1
cantidad_divisores = 0

while contador <= numero:
    if numero % contador == 0:
        print(contador)
        cantidad_divisores += 1

    contador += 1

print("Cantidad de divisores:", cantidad_divisores)


#10
numero = int(input("Ingrese un número: "))

contador = 1
cantidad_divisores = 0

while contador <= numero:
    if numero % contador == 0:
        cantidad_divisores += 1

    contador += 1

if cantidad_divisores == 2:
    print("El número es primo")
else:
    print("El número no es primo")


#11
numero = int(input("Ingrese un número: "))

actual = 2
cantidad_primos = 0

while actual <= numero:

    divisores = 0
    contador = 1

    while contador <= actual:
        if actual % contador == 0:
            divisores += 1

        contador += 1

    if divisores == 2:
        print(actual)
        cantidad_primos += 1

    actual += 1

print("Cantidad de números primos encontrados:", cantidad_primos)