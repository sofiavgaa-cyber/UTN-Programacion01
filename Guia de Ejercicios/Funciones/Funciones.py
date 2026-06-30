# ---------------------------------------------------
# 1. Solicitar un número entero y retornarlo
# ---------------------------------------------------
def pedir_entero(mensaje="Ingrese un número entero: "):
    numero = int(input(mensaje))
    return numero


# ---------------------------------------------------
# 2. Solicitar un número flotante y retornarlo
# ---------------------------------------------------
def pedir_flotante(mensaje="Ingrese un número decimal: "):
    numero = float(input(mensaje))
    return numero


# ---------------------------------------------------
# 3. Solicitar una cadena y retornarla
# ---------------------------------------------------
def pedir_cadena(mensaje="Ingrese una cadena: "):
    cadena = input(mensaje)
    return cadena


# ---------------------------------------------------
# 4. Calcular área de un rectángulo
# ---------------------------------------------------
def calcular_area_rectangulo(base, altura):
    """
    Recibe base y altura.
    Retorna el área del rectángulo.
    """
    return base * altura


# ---------------------------------------------------
# 5. Calcular área de un círculo
# ---------------------------------------------------
def calcular_area_circulo(radio):
    """
    Recibe el radio.
    Retorna el área del círculo.
    """
    return pi * radio ** 2


# ---------------------------------------------------
# 6. Verificar si un número es par o impar
#    (imprime mensaje)
# ---------------------------------------------------
def mostrar_paridad(numero):
    if numero % 2 == 0:
        print("El número es PAR")
    else:
        print("El número es IMPAR")


# ---------------------------------------------------
# 7. Verificar si un número es par
#    (retorna True o False)
# ---------------------------------------------------
def es_par(numero):
    return numero % 2 == 0


# ---------------------------------------------------
# 8. Encontrar el máximo de tres números
# ---------------------------------------------------
def maximo_tres(num1, num2, num3):
    mayor = num1

    if num2 > mayor:
        mayor = num2

    if num3 > mayor:
        mayor = num3

    return mayor


# ---------------------------------------------------
# 9. Calcular potencia
# ---------------------------------------------------
def calcular_potencia(base, exponente):
    return base ** exponente


# ---------------------------------------------------
# 10. Verificar si un número es primo
# ---------------------------------------------------
def es_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


# ---------------------------------------------------
# 11. Mostrar números primos entre 1 y N
#    Retorna cantidad de primos encontrados
# ---------------------------------------------------
def mostrar_primos(limite):

    contador = 0

    for numero in range(2, limite + 1):

        if es_primo(numero):
            print(numero)
            contador += 1

    return contador


# ---------------------------------------------------
# 12. Tabla de multiplicar con parámetros opcionales
# ---------------------------------------------------
def tabla_multiplicar(numero, inicio=1, fin=10):

    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")


# ---------------------------------------------------
# 13. Funciones reutilizables con validaciones
# ---------------------------------------------------

def pedir_entero_validado(mensaje="Ingrese un número entero: "):

    while True:
        dato = input(mensaje)

        if dato.lstrip("-").isdigit():
            return int(dato)

        print("Error. Debe ingresar un número entero.")


def pedir_flotante_validado(mensaje="Ingrese un número decimal: "):

    while True:
        dato = input(mensaje)

        try:
            return float(dato)
        except ValueError:
            print("Error. Debe ingresar un número decimal válido.")


def pedir_cadena_validada(mensaje="Ingrese texto: "):

    while True:
        cadena = input(mensaje).strip()

        if len(cadena) > 0:
            return cadena

        print("Error. No puede estar vacía.")