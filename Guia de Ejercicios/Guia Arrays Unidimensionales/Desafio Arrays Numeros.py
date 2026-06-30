def es_positivo(numero:int) -> bool:
    """
    Determina si un número es positivo.
    """
    return numero > 0


def es_negativo(numero:int) -> bool:
    """
    Determina si un número es negativo.
    """
    return numero < 0


def es_par(numero:int) -> bool:
    """
    Determina si un número es par.
    """
    return numero % 2 == 0


def es_impar(numero:int) -> bool:
    """
    Determina si un número es impar.
    """
    return numero % 2 != 0

from Especificas import *


def cargar_numeros(cantidad:int) -> list:
    """
    Permite ingresar una cantidad determinada de números.
    """
    lista = []

    for i in range(cantidad):

        while True:

            numero = int(
                input(
                    f"Ingrese número ({i+1}/{cantidad}) [-1000 a 1000]: "
                )
            )

            if -1000 <= numero <= 1000:
                lista.append(numero)
                break

            print("Error. Debe estar entre -1000 y 1000.")

    return lista


def contar_positivos_negativos(lista:list) -> tuple:
    """
    Cuenta positivos y negativos.
    """
    positivos = 0
    negativos = 0

    for numero in lista:

        if es_positivo(numero):
            positivos += 1

        elif es_negativo(numero):
            negativos += 1

    return positivos, negativos


def sumar_pares(lista:list) -> int:
    """
    Retorna la suma de los números pares.
    """
    suma = 0

    for numero in lista:

        if es_par(numero):
            suma += numero

    return suma


def mayor_impar(lista:list):
    """
    Retorna el mayor número impar.
    """
    mayor = None

    for numero in lista:

        if es_impar(numero):

            if mayor is None or numero > mayor:
                mayor = numero

    return mayor


def listar_numeros(lista:list) -> None:
    """
    Muestra todos los números.
    """
    for numero in lista:
        print(numero)


def listar_pares(lista:list) -> None:
    """
    Muestra los números pares.
    """
    for numero in lista:

        if es_par(numero):
            print(numero)


def listar_posiciones_impares(lista:list) -> None:
    """
    Muestra los elementos que se encuentran
    en posiciones impares.
    """
    for i in range(len(lista)):

        if i % 2 != 0:
            print(lista[i])

from Array_Generales import *

numeros = []
datos_cargados = False

while True:

    print("\n===== MENÚ =====")
    print("1. Ingresar datos")
    print("2. Cantidad de positivos y negativos")
    print("3. Suma de los números pares")
    print("4. Mayor número impar")
    print("5. Listar números ingresados")
    print("6. Listar números pares")
    print("7. Listar números en posiciones impares")
    print("8. Salir")

    opcion = input("Ingrese opción: ")

    match opcion:

        case "1":

            numeros = cargar_numeros(10)
            datos_cargados = True

            print("Datos cargados correctamente.")

        case "2":

            if datos_cargados:

                positivos, negativos = (
                    contar_positivos_negativos(numeros)
                )

                print(f"Positivos: {positivos}")
                print(f"Negativos: {negativos}")

            else:
                print("Primero debe cargar datos.")

        case "3":

            if datos_cargados:

                suma = sumar_pares(numeros)

                print(f"Suma de pares: {suma}")

            else:
                print("Primero debe cargar datos.")

        case "4":

            if datos_cargados:

                mayor = mayor_impar(numeros)

                if mayor is not None:
                    print(f"Mayor impar: {mayor}")
                else:
                    print("No hay números impares.")

            else:
                print("Primero debe cargar datos.")

        case "5":

            if datos_cargados:

                print("\nNúmeros ingresados:")
                listar_numeros(numeros)

            else:
                print("Primero debe cargar datos.")

        case "6":

            if datos_cargados:

                print("\nNúmeros pares:")
                listar_pares(numeros)

            else:
                print("Primero debe cargar datos.")

        case "7":

            if datos_cargados:

                print("\nElementos en posiciones impares:")
                listar_posiciones_impares(numeros)

            else:
                print("Primero debe cargar datos.")

        case "8":

            print("Programa finalizado.")
            break

        case _:

            print("Opción inválida.")