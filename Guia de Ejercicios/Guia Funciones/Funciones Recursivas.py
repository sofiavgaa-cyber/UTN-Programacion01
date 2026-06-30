def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    Solicita un número entero validado.

    Parámetros:
    mensaje: Mensaje a mostrar al usuario.
    mensaje_error: Mensaje de error.
    minimo: Valor mínimo permitido.
    maximo: Valor máximo permitido.
    reintentos: Cantidad de intentos.

    Retorna:
    El número ingresado o None si se agotaron los intentos.
    """

    while reintentos > 0:
        dato = input(mensaje)

        if dato.lstrip("-").isdigit():
            numero = int(dato)

            if minimo <= numero <= maximo:
                return numero

        reintentos -= 1
        print(mensaje_error)

    return None


#01
def suma_naturales(numero:int) -> int:
    """
    Calcula la suma de los primeros números naturales.

    Parámetro:
    numero: Número hasta el cual sumar.

    Retorna:
    La suma de los números desde 1 hasta numero.
    """

    if numero == 1:
        return 1

    return numero + suma_naturales(numero - 1)

from Input import get_int

numero = get_int(
    "Ingrese un número: ",
    "Error. Ingrese un número válido.",
    1,
    1000,
    3
)

if numero is not None:
    resultado = suma_naturales(numero)
    print(f"La suma de los primeros {numero} números naturales es: {resultado}")


#02
def calcular_potencia(base:int, exponente:int) -> int:
    """
    Calcula una potencia mediante recursividad.

    Parámetros:
    base: Número base.
    exponente: Exponente.

    Retorna:
    base elevado a exponente.
    """

    if exponente == 0:
        return 1

    return base * calcular_potencia(base, exponente - 1)

from Input import get_int

base = get_int(
    "Ingrese la base: ",
    "Error.",
    -1000,
    1000,
    3
)

exponente = get_int(
    "Ingrese el exponente: ",
    "Error.",
    0,
    100,
    3
)

if base is not None and exponente is not None:
    resultado = calcular_potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")


#03
def suma_digitos(numero:int) -> int:
    """
    Calcula la suma de los dígitos de un número.

    Parámetro:
    numero: Número entero positivo.

    Retorna:
    La suma de todos sus dígitos.
    """

    if numero < 10:
        return numero

    return (numero % 10) + suma_digitos(numero // 10)

from Input import get_int

numero = get_int(
    "Ingrese un número positivo: ",
    "Error.",
    0,
    999999999,
    3
)

if numero is not None:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos es: {resultado}")


#04
def fibonacci(numero:int) -> int:
    """
    Calcula el término de Fibonacci indicado.

    Parámetro:
    numero: Posición de la sucesión.

    Retorna:
    El valor correspondiente en la sucesión de Fibonacci.
    """

    if numero == 0:
        return 0

    if numero == 1:
        return 1

    return fibonacci(numero - 1) + fibonacci(numero - 2)

from Input import get_int

numero = get_int(
    "Ingrese la posición de Fibonacci: ",
    "Error.",
    0,
    35,
    3
)

if numero is not None:
    resultado = fibonacci(numero)

    print(f"Fibonacci({numero}) = {resultado}")
